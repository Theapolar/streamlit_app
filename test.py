import openai
import os

api_key = "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"

openai.api_key = api_key

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60
)

print(response.choices[0].text.strip())
