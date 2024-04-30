import streamlit as st
# from transformers import pipeline

# Load the conversational pipeline
# chatbot_pipeline = pipeline("conversational")

# Create a Streamlit app
st.title("Chatbot Application")

# Define a function to interact with the chatbot
def chat():
    user_input = st.text_input("You:", "")
    if user_input:
        # Generate response from the chatbot
        # response = chatbot_pipeline(user_input)[0]['generated_text']
        st.text_area("Chatbot:", value="Hello", height=200, max_chars=None, key=None)

# Call the chat function
chat()
