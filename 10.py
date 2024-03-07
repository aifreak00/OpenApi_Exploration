from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."
    },
    {
      "role": "user",
      "content": "I hated the new Batman movie!"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print(response)