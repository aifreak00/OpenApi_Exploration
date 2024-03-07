from openai import OpenAI
client = OpenAI()

try:
    with open("C:/Users/ASUS/Downloads/Music/mlk.flac", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    print(transcript)
except Exception as e:
    print(f"An error occurred: {e}")