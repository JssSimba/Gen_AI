import os
import tempfile
import streamlit as st
from streamlit_chat import message
from document_loader import ChatPDF

# Set the page title for the Streamlit app
st.set_page_config(page_title="ChatPDF")


def display_messages():
    """
    Display chat messages in the Streamlit app.
    """
    st.subheader("Chat")
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        # Display each message with the appropriate sender (user or assistant)
        message(msg, is_user=is_user, key=str(i))
    # Create an empty placeholder for the thinking spinner
    st.session_state["thinking_spinner"] = st.empty()


def process_input():
    """
    Process user input and get a response from the assistant.
    """
    if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
        # Get the user's input text
        user_text = st.session_state["user_input"].strip()
        with st.session_state["thinking_spinner"], st.spinner(f"Thinking"):
            # Get the assistant's response
            agent_text = st.session_state["assistant"].ask(user_text)

        # Append the user's input and the assistant's response to the message history
        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((agent_text, False))


def read_and_save_file():
    """
    Read and save the uploaded file, and ingest it into the assistant.
    """
    st.session_state["assistant"].clear()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

    for file in st.session_state["file_uploader"]:
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(file.getbuffer())
            file_path = tf.name

        # Ingest the file into the assistant
        with st.session_state["ingestion_spinner"], st.spinner(f"Ingesting {file.name}"):
            st.session_state["assistant"].ingest(file_path)
        # Remove the temporary file
        os.remove(file_path)


def page():
    """
    Define the main page layout and functionality of the Streamlit app.
    """
    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        st.session_state["assistant"] = ChatPDF()

    st.header("ChatPDF")

    st.subheader("Upload a document")
    st.file_uploader(
        "Upload document",
        type=["pdf"],
        key="file_uploader",
        on_change=read_and_save_file,
        label_visibility="collapsed",
        accept_multiple_files=True,
    )

    # Create an empty placeholder for the ingestion spinner
    st.session_state["ingestion_spinner"] = st.empty()

    # Display chat messages and input field
    display_messages()
    st.text_input("Message", key="user_input", on_change=process_input)


if __name__ == "__main__":
    page()