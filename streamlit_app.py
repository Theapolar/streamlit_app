import os
import streamlit as st
import openai

st.set_page_config(layout="wide", page_icon=None, initial_sidebar_state="auto", page_title=None, menu_items={'Get help': None, 'Report a bug': None, 'About': None})

def chatbot_response(skills_list):
    openai.api_key = os.getenv("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")
    model = "gpt-4"
    max_tokens = 900
    prompt = f"The user has skills in or cares about {skills_list}..."
    # rest of your code

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    message = response['choices'][0]['message']['content']
    return message.strip()

st.title("Ideas to Monetize")

user_input = st.text_input("Enter your skills, interests, curiosities")
if st.button("Send"):
    if user_input.lower() == "bye":
        st.write("Goodbye! Have a great day!")
    else:
        response = chatbot_response(user_input)
        st.write("Chatbot:", response)
