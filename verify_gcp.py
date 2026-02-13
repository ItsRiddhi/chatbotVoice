import os
from google.cloud import texttospeech
from google.cloud import speech
# Dialogflow CX requires a slightly different import structure depending on version, 
# but generally google.cloud.dialogflowcx is the package.
from google.cloud import dialogflowcx_v3
from dotenv import load_dotenv

# Load Environment Variables from .env file
load_dotenv()

def verify_apis():
    print("Checking Google Cloud Environment...")

    # Check Env Var
    creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds:
        print("[ERROR] GOOGLE_APPLICATION_CREDENTIALS environment variable is NOT set.")
        return
    else:
        print(f"[OK] GOOGLE_APPLICATION_CREDENTIALS found: {creds}")

    # 1. Test Text-to-Speech
    try:
        tts_client = texttospeech.TextToSpeechClient()
        # Perform a lightweight list_voices call
        tts_client.list_voices()
        print("[OK] Google Cloud Text-to-Speech API is reachable.")
    except Exception as e:
        print(f"[FAIL] Text-to-Speech API Check Failed: {e}")

    # 2. Test Speech-to-Text
    try:
        stt_client = speech.SpeechClient()
        # No simple "list" method that's cheap, but instantiation is a good first step.
        # We can try seeing if we can create a recognizer or just pass.
        # Ideally we'd list operations or verify authentication.
        print("[OK] Google Cloud Speech-to-Text Client instantiated successfully.")
    except Exception as e:
        print(f"[FAIL] Speech-to-Text API Check Failed: {e}")

    # 3. Test Dialogflow CX
    try:
        # Just checking if we can instantiate the client. 
        # Actual calls need Project ID / Agent ID which might not be in env yet.
        cx_client = dialogflowcx_v3.AgentsClient()
        print("[OK] Dialogflow CX Client instantiated successfully.")
    except Exception as e:
        print(f"[FAIL] Dialogflow CX API Check Failed: {e}")

if __name__ == "__main__":
    verify_apis()
