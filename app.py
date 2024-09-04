import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

st.title("Vedanth's Chatbot")
user_input = st.text_input("Enter something:")

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{user_input}",
        }
    ],
    model="llama3-70b-8192",
)


st.write(chat_completion.choices[0].message.content)
