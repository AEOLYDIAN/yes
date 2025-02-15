import time
import os
from google import genai
import speech_recognition as sr
import subprocess
import signal
from playsound import playsound

os.environ['PYTHONWARNINGS'] = 'ignore'
os.environ['GPRC_VERBOSITY'] = 'ERROR'
os.environ['GLOG_minloglevel'] = '2'
os.environ['ALSA_LOG_LEVEL'] = '0'

API = 'AIzaSyCdx7oSFOXW2ZFfKbHLZwhfSUc2OrPeBOM'
client = genai.Client(api_key=API)
audio_path = "../temp_audio/output.mp3"
tracking_process = None  # Initialize tracking_process

def generate_voice(text):
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)
    playsound(audio_path)  # Using playsound for reliable audio playback
    os.remove(audio_path)

r = sr.Recognizer()

while(1):
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            print("Wait a moment")

            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.2)

            # Listen for user input
            audio2 = r.listen(source)

            # Recognize audio using Google API
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText == "open tracker":
                if tracking_process is None or tracking_process.poll() is not None:
                    print("Opening Tracker...")
                    generate_voice("Opening Tracker")
                    tracking_process = subprocess.Popen(['python', 'reddetect.py'])
                else:
                    print("Tracker is already running.")

            elif (MyText == "stop tracker" or MyText == "kill tracker") and tracking_process is not None:
                print("Stopping Tracker...")
                generate_voice("Stopping Object Tracking")
                os.kill(tracking_process.pid, signal.SIGTERM)  # Terminate the subprocess
                tracking_process = None  # Reset the process variable
                print("Tracking program stopped.")

            elif MyText == "go to sleep":
                print("Signing Off")
                generate_voice("OK GOODBYE, HAVE A GOOD DAY!!")
                if tracking_process is not None:
                    os.kill(tracking_process.pid, signal.SIGTERM)
                break

            else:
                response = client.models.generate_content(
                    model="gemini-2.0-flash", contents=MyText + ';be very very short'
                )
                text = response.text
                generate_voice(text)

                time.sleep(2)

    except sr.RequestError as e:
        print("Could not request results")

    except sr.UnknownValueError:
        print("Unknown error occurred")
