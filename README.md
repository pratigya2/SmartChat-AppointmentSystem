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
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

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
git clone https://github.com/yourusername/https://github.com/pratigya2/SmartChat-AppointmentSystem.git
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
   You: my
   AI: Yes, your name is Pratigya Paudel. How can I assist you further, Pratigya?
   You: What are the main topics covered in the FastAPI Book?
   AI: [Detailed response based on the FastAPI Book content]
   You: bye
   AI: Thank you for chatting. Goodbye!
   ```

   *Type your messages after the `You:` prompt. To exit the chat, type `exit`, `quit`, or `bye`.*

## Usage

The Pratigya ChatBot serves two main purposes:

1. **Providing Information from the FastAPI Book**

   - **Query Examples:**
     - "What are the main topics covered in the FastAPI Book?"
     - "Explain federated learning as described in the FastAPI Book."
     - "Tell me about the YOLOv8 model from the FastAPI Book."

2. **Booking Appointments**

   - **How to Book:**
     - "I want to book an appointment on September 25th."
     - "Schedule a meeting for October 10th."
   
   - **Note:** Ensure you provide the date in a recognizable format. The chatbot will parse and confirm the booking.

### Managing User Information

The chatbot can store and recall user information such as name, phone number, and email. Initially, these details might be empty, and you can provide them as the conversation progresses.

- **Providing Information:**
  
  - "My name is Prajesh."
  - "My phone number is 9801234567."
  - "My email is prajesh@example.com."

- **Querying Stored Information:**
  
  - "Can you recall my name?"
  - "What is my registered email?"

## Troubleshooting

Encountering issues? Here's how to resolve common problems:

### 1. **Invalid OpenAI API Key**

**Error Message:**

```plaintext
openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Incorrect API key provided: ...', ...}}
```

**Solution:**

- **Verify API Key:**
  - Ensure your OpenAI API key is correct and starts with `sk-`.
  
- **Set API Key Correctly:**
  - Use a `.env` file or set it as an environment variable as described in the [Configuration](#configuration) section.

- **Regenerate API Key:**
  - If unsure, regenerate a new API key from [OpenAI's API Keys Page](https://platform.openai.com/account/api-keys).

### 2. **Pydantic Validation Errors**

**Error Message:**

```plaintext
ValidationError: 3 validation errors for User
name
  Field required [type=missing, input_value={}, input_type=dict]
...
```

**Solution:**

- **Ensure Optional Fields Have Defaults:**
  - Confirm that all optional fields in your Pydantic models are set with default values (`None`).

- **Review Model Definitions:**
  - Check `user_management.py` to ensure models are correctly defined.

### 3. **ChatBot Freezes During Document Processing**

**Symptom:**

The application hangs after loading and splitting documents.

**Solution:**

- **Reduce Number of Chunks:**
  - Increase `chunk_size` and decrease `chunk_overlap` in `document_processor.py` to process fewer chunks.

- **Monitor System Resources:**
  - Ensure your machine has sufficient CPU and memory.

- **Use a Different PDF:**
  - Test with a well-structured PDF to rule out PDF-specific issues.

### 4. **Tokenizers Parallelism Warning**

**Warning Message:**

```plaintext
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
```

**Solution:**

- **Set Environment Variable:**
  - As described in the [Configuration](#configuration) section, set `TOKENIZERS_PARALLELISM=false`.

## Contributing

Contributions are welcome! If you'd like to enhance the Pratigya ChatBot, follow these steps:

1. **Fork the Repository**

   Click on the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/Pratigya-ChatBot.git
   cd Pratigya-ChatBot
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

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **OpenAI**: For providing access to advanced language models.
- **LangChain Community**: For developing the LangChain framework.
- **Pydantic Developers**: For creating robust data validation tools.

---

*Feel free to customize this README to better fit the specifics of your project, including adding sections like "Roadmap", "FAQs", or "Contact Information" as needed.*