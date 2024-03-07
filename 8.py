# from openai import OpenAI

# client = OpenAI(
#     # Set your API key here
#     # api_key="Your API Key",
# )

# audio_file_path = "EarningsCall.mp3"

# with open(audio_file_path, 'rb') as audio_file:
#     transcription = client.audio.transcriptions.create(
#         model="whisper-1",
#         file=audio_file,
        
#     )
# print(transcription)


from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)
from docx import Document

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcription['text']