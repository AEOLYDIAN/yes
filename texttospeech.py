from gtts import gTTS
import time

text="There once was a cat with a hat, who rode on the back of a bat, the bat flew so high, it nearly touched the sky, but the cat said, 'This is too flat!' The cat then ate cake made of cheese, and chased after clouds in the breeze, it tripped on a shoe, and then, out of the blue, it danced with some very small fleas!"

tts = gTTS(text=text, lang="en")

# Save as an MP3 file
tts.save("output.mp3")

# Play the audio (optional)
import os
os.system("start output.mp3")  
time.sleep(2)

os.remove("start output.mp3")