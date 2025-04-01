# ChatPDF

ChatPDF is a Streamlit application that allows users to upload PDF documents and interact with a conversational chatbot to ask questions based on the contents of the uploaded documents. The chatbot uses OpenAI's GPT-3.5-turbo model to provide answers based on the context provided by the PDF documents.

## Features

- Upload PDF documents and ingest their content.
- Ask questions about the content of the uploaded PDFs.
- Interactive chat interface with conversational memory.
- Supports multiple PDF uploads.

## Setup

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI API Key (optional for OpenAI version)
- Ollama Llama model (for free version)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ChatPDF.git
   cd ChatPDF
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Using OpenAI API

1. Run the Streamlit app:

   ```bash
   streamlit run chat_pdf.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your PDF documents using the file uploader.

4. Ask questions about the content of the uploaded PDFs in the chat interface.

### Using Ollama Llama Model

1. Run the Streamlit app:

   ```bash
   streamlit run chat_pdf_ollama.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your PDF documents using the file uploader.

4. Ask questions about the content of the uploaded PDFs in the chat interface.