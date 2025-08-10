from openai import OpenAI

# -------------------------------
# Setup your OpenAI API client
# -------------------------------
# Replace <YOUR_OPENAI_API_KEY> with your actual key
client = OpenAI(api_key="<YOUR_OPENAI_API_KEY>")

# -------------------------------
# Send a test message to OpenAI
# -------------------------------
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

# -------------------------------
# Print the AI's response
# -------------------------------
print(completion.choices[0].message.content)
