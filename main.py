from gtts import gTTS
import time
import os
from google import genai
import speech_recognition as sr
import subprocess


os.environ['PYTHONWARNINGS']='ignore'
os.environ['GPRC_VERBOSITY']='ERROR'
os.environ['GLOG_minloglevel']='2'
os.environ['ALSA_LOG_LEVEL']='0'



API='AIzaSyCdx7oSFOXW2ZFfKbHLZwhfSUc2OrPeBOM'
client = genai.Client(api_key=API)
audio_path="../temp_audio/output.mp3"

def generate_voice(text):
    
    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)
    os.system(audio_path)
    os.remove(audio_path)
    

r = sr.Recognizer() 



while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source:
            print("Wait a moment")
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText=="open tracker":
                print("Opening Tracker...")
                generate_voice("Opening Tracker")
                # Replace 'track_object.py' with your actual object tracking software/script
                tracking_process=subprocess.Popen(['python', 'reddetect.py'])

            elif MyText == "stop tracker" or MyText=="kill tracker" and tracking_process is not None:
                # Stop the subprocess using terminate()
                print("Stopping Tracker...")
                generate_voice("Stopping Object Tracking")
                tracking_process.terminate()  # Terminate the subprocess
                tracking_process = None  # Reset the process variable
                print("Tracking program stopped.")
            
            elif MyText=="go to sleep":
                
                print("Signing Off")
                generate_voice("OK GOODBYE, HAVE A GOOD DAY!!")
                break

            else:
                
                response = client.models.generate_content(
                        model="gemini-2.0-flash", contents=MyText+ ';be very very short'
                )
    
                text=response.text
                generate_voice(text)
                
                
                time.sleep(2)
            
    except sr.RequestError as e:
        print(f"Could not request results")
        
    except sr.UnknownValueError:
        print(f"unknown error occurred")











