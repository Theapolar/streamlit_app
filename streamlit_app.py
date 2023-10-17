import streamlit as st
st.set_page_config(layout="wide", page_icon=None, initial_sidebar_state="auto", page_title=None, menu_items={'Get help': None, 'Report a bug': None, 'About': None})

import openai

def chatbot_response(skills_list):
    openai.api_key = "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"
    model = "gpt-4"
    max_tokens = 900

    prompt = f"The user has skills in or cares about {skills_list}...Generate a list of 10 highly creative and unique business ideas for solopreneurs incorporating best practices from various frameworks like Russel Brunson's 'value ladder,' Lean Startup's 'MVP' (Minimum Viable Product), and Value Proposition Design's 'customer job' concept. The ideas should align with their skills and interests, be actionable, require minimal capital, and offer quick returns. Keep the descriptions under one sentence. Also, list 5 concise skills or subjects they should focus on learning to excel in these services. make sure to fit 10 ideas an 5 skills to learn within max 900 tokens.No waste of words"

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

st.title("Aideas to monitize")

user_input = st.text_input("Enter your skills,interests,curiosities")
if st.button("Send"):
    if user_input.lower() == "bye":
        st.write("Goodbye! Have a great day!")
    else:
        response = chatbot_response(user_input)
        st.write("Chatbot:", response)
