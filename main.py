import os
import uuid
import logging
from src.document_processor import DocumentProcessor
from src.chatbot import *
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

def main():
    try:
        # Configuration
        pdf_path = 'data/fastapi_book.pdf'  # Path to your PDF
        persist_directory = 'stored_data'    # Directory to store processed data
        
        # Ensure persist_directory exists
        os.makedirs(persist_directory, exist_ok=True)
        
        # Initialize Document Processor
        doc_processor = DocumentProcessor()
        
        # Check if data is already processed
        if not os.listdir(persist_directory):
            vectorstore, splits = doc_processor.process_documents(pdf_path, persist_directory)
        else:
            # Load stored data
            vectorstore, splits = doc_processor.load_stored_data(persist_directory)
    
        load_dotenv(override=True)
        
        # Initialize LLM
        llm = ChatOpenAI(temperature=0)
        
        # Initialize Memory
        memory = MemorySaver()
        
        # Initialize ChatBot
        initialize_chatbot(vectorstore, llm, memory)
        
        # Run Chat Loop
        config = {"configurable": {"thread_id": str(uuid.uuid4())}}
        run_chat_loop(config)
    
    except Exception as e:
        print(f"AI: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()