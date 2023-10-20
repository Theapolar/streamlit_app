import os
import streamlit as st
import openai

# Retrieve the API key from Streamlit's secrets
api_key = st.secrets["openai"]["api_key"]

# Set the API key for OpenAI
openai.api_key = api_key

# Set Streamlit settings
st.set_page_config(layout="wide", page_icon=None, initial_sidebar_state="auto", page_title=None, menu_items={'Get help': None, 'Report a bug': None, 'About': None})


def chatbot_response(skills_list):
    model = "gpt-4"
    max_tokens = 900
    prompt = f"The user has skills in or cares about {skills_list}... Generate a list of 10 highly creative and unique business ideas for solopreneurs. Incorporate best practices from various frameworks like Russel Brunson's 'value ladder,' Lean Startup's 'MVP' (Minimum Viable Product), and Value Proposition Design's 'customer job' concept. The ideas should not only align with their skills and interests but also be actionable, require minimal capital, and offer quick returns."
    
    # Create chat completion
    response = openai.ChatCompletion.create(
        model=model,
        api_key=api_key,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    
    message = response['choices'][0]['message']['content']
    return message.strip()


# Streamlit interface
st.title("Ideas to Monetize")
user_input = st.text_input("Enter your skills, interests, curiosities")

if st.button("Send"):
    if user_input.lower() == "bye":
        st.write("Goodbye! Have a great day!")
    else:
        response = chatbot_response(user_input)
        st.write("Chatbot:", response)
