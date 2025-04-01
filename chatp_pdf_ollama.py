from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
# from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Raise an error if the API key is not found
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Set the OpenAI API key in the environment variables
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


class ChatPDF:
    vector_store = None
    retriever = None
    chain = None
    memory = None

    def __init__(self):
        # Initialize the chat model
        self.model = ChatOllama(model="llama3:8b")
        # Initialize the text splitter with chunk size and overlap
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
        # Initialize conversation buffer memory
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Define the prompt template for the chatbot
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] You are a helpful chatbot that answers questions based on the context provided.
            Be conversational and engaging. Refer to previous parts of the conversation if relevant.
            If the context doesn't contain the answer, say that you don't know.
            Use your expertise to answer generic questions, refer to the document provided to you to answer questions related to the document.
            Answer in English and respond to the questions. [/INST] </s> 
            [INST] Question: {question} 
            Context: {context} 
            Chat History: {chat_history}
            Answer: [/INST]
            """
        )

    def ingest(self, pdf_file_path: str):
        # Load the PDF document
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        # Split the document into chunks
        chunks = self.text_splitter.split_documents(docs)
        # Filter complex metadata from chunks
        chunks = filter_complex_metadata(chunks)

        # Initialize the vector store with the document chunks and OpenAI embeddings
        self.vector_store = FAISS.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())
        # Initialize the retriever with similarity score threshold
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )

        # Create a Conversational Retrieval Chain
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.model,
            retriever=self.retriever,
            memory=self.memory,
            get_chat_history=lambda h: h,
            return_source_documents=False,
        )

    def ask(self, query: str):
        # Check if the conversational chain is initialized
        if not self.chain:
            return "Please, add a PDF document first."

        # Get the response from the conversational chain
        result = self.chain({"question": query})
        return result["answer"]

    def clear(self):
        # Clear the vector store, retriever, chain, and memory
        self.vector_store = None
        self.retriever = None
        self.chain = None
        self.memory.clear()