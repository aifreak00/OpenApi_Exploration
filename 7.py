from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speec.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="hi prathamesh ettam i hope you are fine"
)

response.stream_to_file(speech_file_path)