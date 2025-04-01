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
- OpenAI API Key

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

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run chat_pdf_app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your PDF documents using the file uploader.

4. Ask questions about the content of the uploaded PDFs in the chat interface.

## Project Structure

- `chat_pdf.py`: Contains the `ChatPDF` class for handling PDF ingestion and interaction with the chatbot.
- `chat_pdf_app.py`: Main Streamlit app file that defines the UI and chat functionality.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation (this file).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the GPT-3.5-turbo model.
- [Streamlit](https://streamlit.io/) for providing the framework to build the web application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

For any inquiries, please contact [your-email@example.com].

## Instructions for Developers

### Adding Comments to the Code

1. Open `chat_pdf.py` and `chat_pdf_app.py` files in your preferred code editor.
2. Add comments to the code for better readability and understanding.
3. Make sure to explain the purpose of each function and important code sections.

### Linting the Code

1. Install a linter like `flake8` or `pylint`:

   ```bash
   pip install flake8
   ```

2. Run the linter on your code files:

   ```bash
   flake8 chat_pdf.py chat_pdf_app.py
   ```

3. Fix any linting issues reported by the linter.

### Creating a README File

1. Open your preferred text editor and create a new file named `README.md`.
2. Add the following sections to the README file:
   - Project Title
   - Features
   - Setup
   - Prerequisites
   - Installation
   - Usage
   - Project Structure
   - License
   - Acknowledgements
   - Contributing
   - Contact
   - Instructions for Developers

3. Save the file and include it in your project repository.

### Uploading to GitHub

1. Navigate to your project directory in the terminal.
2. Initialize a new Git repository:

   ```bash
   git init
   ```

3. Add your files to the repository:

   ```bash
   git add .
   ```

4. Commit the changes:

   ```bash
   git commit -m "Initial commit"
   ```

5. Add the remote repository URL:

   ```bash
   git remote add origin https://github.com/your-username/ChatPDF.git
   ```

6. Push the changes to the remote repository:

   ```bash
   git push -u origin main
   ```