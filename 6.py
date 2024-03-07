from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-2",
  prompt="sam altman",
  size="1024x1024",
  quality="standard",
  n=1,
)
image_url = response.data[0].url
print(response)
# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)