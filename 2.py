from openai import OpenAI
client = OpenAI()

audio_file= open("speech.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(transcript)