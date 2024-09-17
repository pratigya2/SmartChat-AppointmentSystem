import os
import uuid
import logging
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from pydantic import EmailStr
from langchain_core.tools import tool
from langchain.tools.retriever import create_retriever_tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from src.user_management import User, UserInput
from src.appointment_management import Appointment
from src.utils import parse_date



# Global variables
vectorstore = None
llm = None
memory = None
qa_user = User(name = None, phone_no = None, email = None)
appointment = Appointment(user=qa_user, dates = None)
conversation_history = []

def get_user():
    return qa_user

def initialize_chatbot(vectorstore_param, llm_param, memory_param):
    global vectorstore, llm, memory
    vectorstore = vectorstore_param
    llm = llm_param
    memory = memory_param

def validate_user_info(user):
    """
    Checks if the user has provided all required information to make an appointment.
    Returns a prompt with missing information if applicable.
    """
    # Dictionary of required user information
    required_info = {
        "Name": user.name,
        "Phone Number": user.phone_no,
        "Email": user.email,
    }

    missing_info = [field for field, value in required_info.items() if not value]

    if missing_info:
        prompt = f"The user is missing the following information: {', '.join(missing_info)}."
        flag=True
    else:
        prompt = "The user has entered all the required information. Thank them and tell them they can make appointments now."
        flag=False

    return prompt, flag

@tool()
def book_appointment(date):
  """
  Check if the entered date is already booked for job appointment.

  Args:
    date: the date entered in the format YYYY-MM-DD
  """
  qa_user = get_user()
  resp, flag = validate_user_info(qa_user)
  if flag:
    return resp
  if appointment.dates and date in appointment.dates:
    return "The day is already booked."
  else:
    appointment.dates = [date]
    return "The day has been booked"

@tool()
def parse_date_tool(input_date: str) -> str:
    """
    Parses the user-provided date into YYYY-MM-DD.
    """
    try:
        formatted_date = parse_date(input_date)
        return f"Date parsed successfully: {formatted_date}"
    except ValueError as e:
        return str(e)

@tool(args_schema=UserInput)
def store_user_info(name: Optional[str] = None, phone_no: Optional[str] = None, email: Optional[EmailStr] = None) -> str:
    """
    Store user information such as name, phone number, and email.
    """
    update_data = {k: v for k, v in locals().items() if v is not None}
    if not update_data:
        return "No information provided to update."

    try:
        qa_user = get_user()
        updated_user = User(**{**qa_user.model_dump(), **update_data})

        # If validation passes, update qa_user
        qa_user.model_validate(updated_user.model_dump())

        # Update qa_user with the new data
        for key, value in update_data.items():
            setattr(qa_user, key, value)

        resp, _ = validate_user_info(qa_user)
        return resp
    except ValueError as e:
        return f"Validation failed: {str(e)}"



def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

def run_chat_loop(config):
    global conversation_history
    system_prompt = SystemMessage(content="You are a helpful assistant designed to gather user information.")
    initial_ai_message = AIMessage(content="Hello! I'm here to help you. I can provide information from the FastAPI book or set an appointment date for you.")
    conversation_history = [system_prompt, initial_ai_message]

    print(f"AI: {initial_ai_message.content}")

    retriever_tool = create_retriever_tool(    
        vectorstore.as_retriever(),
        "fastapi_retriever",
        "Searches and returns excerpts from the FastAPI Book."
    )
    tools = [retriever_tool, book_appointment, store_user_info, parse_date_tool]
    agent_executor = create_react_agent(llm, tools, checkpointer=memory)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                farewell_message = "Thank you for chatting. Goodbye!"
                print(f"AI: {farewell_message}")
                conversation_history.append(HumanMessage(content=user_input))
                conversation_history.append(AIMessage(content=farewell_message))
                break

            user_message = HumanMessage(content=user_input)
            conversation_history.append(user_message)
            response_stream = agent_executor.stream({"messages": user_message}, config=config, stream_mode="values")
            print_stream(response_stream)

        except KeyboardInterrupt:
            farewell_message = "Chatbot terminated by user. Goodbye!"
            print(f"\nAI: {farewell_message}")
            break
        except Exception as e:
            print(f"AI: An unexpected error occurred: {e}")



# Main function to run the chatbot
def main(vectorstore_param, llm_param, memory_param, config):
    initialize_chatbot(vectorstore_param, llm_param, memory_param)
    run_chat_loop(config)