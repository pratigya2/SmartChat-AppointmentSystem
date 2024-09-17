# Smart Chat Appointment System

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the ChatBot](#running-the-chatbot)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Smart Chat Appointment System** is an intelligent conversational agent designed to assist users by providing detailed information from the FastAPI book and managing appointment bookings. Leveraging advanced natural language processing and machine learning techniques, the chatbot can comprehend user queries, retrieve relevant data from processed documents, and interact seamlessly to enhance user experience.

## Features

- **Document Understanding**: Processes and understands content from the FastAPI book using advanced NLP techniques.
- **Appointment Booking**: Allows users to book appointments by specifying dates.
- **User Information Management**: Collects and stores user details such as name, phone number, and email.
- **Contextual Responses**: Maintains conversation history to provide context-aware replies.
- **Robust Error Handling**: Handles errors gracefully with comprehensive logging for easy debugging.
- **Secure API Integration**: Utilizes OpenAI's API securely by managing API keys through environment variables.

## Technologies Used

- **Python 3.12**
- **LangChain**: A framework for developing applications powered by language models.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Chroma**: A vector database for storing and querying document embeddings.
- **OpenAI API**: Provides access to advanced language models for generating responses.
- **PyPDF & PDFPlumber**: Libraries for PDF processing.
- **Virtualenv**: For creating isolated Python environments.

## Prerequisites

Before setting up the Smart Chat Appointment System, ensure you have the following installed on your system:

- **Python 3.12**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes bundled with Python)
- **Git**: Version control system (optional, for cloning the repository)

## Installation

Follow the steps below to set up the Smart Chat Appointment System on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SmartChat-AppointmentSystem.git
cd SmartChat-AppointmentSystem
```

*Replace `yourusername` with your actual GitHub username if applicable.*

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3.12 -m venv chatbot_env
```

### 3. Activate the Virtual Environment

- **macOS/Linux:**

  ```bash
  source chatbot_env/bin/activate
  ```

- **Windows (Command Prompt):**

  ```cmd
  chatbot_env\Scripts\activate.bat
  ```

- **Windows (PowerShell):**

  ```powershell
  chatbot_env\Scripts\Activate.ps1
  ```

### 4. Install Dependencies

Ensure you have the latest version of `pip` and install the required packages.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Download and Process the PDF file
I have used FastAPI book as my document. You can replace any pdf file you intend to use as document. 

*Note: Ensure that the PDF file is placed in the `data/` directory.*

## Configuration

### 1. Set Up Environment Variables

Securely manage sensitive information like API keys by setting them as environment variables.

#### Using a `.env` File (Recommended)

1. **Create a `.env` File**

   In the root directory of your project, create a file named `.env` and add the following:

   ```plaintext
   OPENAI_API_KEY=sk-your-openai-api-key
   ```

   *Replace `sk-your-openai-api-key` with your actual OpenAI API key.*
You can view .env_example for your reference.

2. **Load Environment Variables in `main.py`**

   Ensure that your `main.py` loads the `.env` file:

   ```python
   # main.py

   import os
   from dotenv import load_dotenv

   load_dotenv()  # Load variables from .env

   # Rest of your imports and code...
   ```

3. **Install `python-dotenv`**

   Ensure `python-dotenv` is included in your `requirements.txt` and installed:

   ```bash
   pip install python-dotenv
   ```

## Running the ChatBot

After completing the installation and configuration steps, you're ready to run the Smart Chat Appointment System.

1. **Ensure the Virtual Environment is Activated**

   ```bash
   # macOS/Linux
   source chatbot_env/bin/activate

   # Windows (Command Prompt)
   chatbot_env\Scripts\activate.bat

   # Windows (PowerShell)
   chatbot_env\Scripts\Activate.ps1
   ```

2. **Run the ChatBot**

   ```bash
   python main.py
   ```

   **Expected Output:**

   ```plaintext
   AI: Hello! I'm here to help you. I can provide information from the FastAPI book or set an appointment date for you.
   ```

3. **Interact with the ChatBot**

   After initialization, you can start interacting with the chatbot via the terminal.

   **Example Interaction:**

   ```plaintext
   AI: Hello! I'm here to help you. I can provide information from the FastAPI book or set an appointment date for you.
   You: my name is pratigya paudel.
   AI: I have stored your name as Pratigya Paudel. Could you please provide your phone number and email address as well?
   You: can you set me an appointment
   AI: Sure, I can help you with that. Please provide me with the date you would like to schedule the appointment for.
   You: tomorrow
   AI: Before I can book the appointment for tomorrow, could you please provide me with your phone number and email address?
   ```

   *Type your messages after the `You:` prompt. To exit the chat, type `exit`.*

## Usage

The Smart Chat Appointment System serves two main purposes:

1. **Providing Information from the FastAPI Book**

   - **Query Examples:**
     - "What are the main topics covered in the FastAPI Book?"
     - "Explain federated learning as described in the FastAPI Book."
     - "Tell me about the Prometheus from the FastAPI Book."

2. **Booking Appointments**

   - **How to Book:**
     - "I want to book an appointment on coming saturday."
     - "Schedule a meeting for tomorrow."
   
   - **Note:** The chatbot will parse any form of date and confirm the booking.

### Managing User Information

The chatbot can store and recall user information such as name, phone number, and email. Initially, these details might be empty, and you can provide them as the conversation progresses.

- **Providing Information:**
  
  - "My name is Pratigya."
  - "My phone number is 9883783923."
  - "My email is pratigya@example.com."

- **Querying Stored Information:**
  
  - "Can you recall my name?"
  - "What is my registered email?"

## Contributing

Contributions are welcome! If you'd like to enhance the Pratigya ChatBot, follow these steps:

1. **Fork the Repository**

   Click on the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/pratigya2/SmartChat-AppointmentSystem
   cd SmartChat-AppointmentSystem
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes**

   Implement your enhancements or bug fixes.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add feature: Your Feature Description"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request**

   Navigate to the original repository and create a pull request from your fork.

### Guidelines

- **Code Quality:** Ensure your code follows Python best practices and is well-documented.
- **Testing:** Include tests for new features or bug fixes.
- **Documentation:** Update the README or other documentation as necessary.

## License

This project is licensed under the [Apache License 2.0](LICENSE). See the [LICENSE](LICENSE) file for details.