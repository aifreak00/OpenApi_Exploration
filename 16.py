from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with Python code, and your task is to calculate its time complexity."
    },
    {
      "role": "user",
      "content": "def foo(n, k):\n        accum = 0\n        for i in range(n):\n            for l in range(k):\n                accum += i\n        return accum"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
completed_content = response.choices[0].message.content
print(completed_content)