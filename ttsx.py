import pyttsx3


engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

Text="Roads go ever ever on, Over rock and under tree, By caves where never sun has shone,By streams that never find the sea;"
engine.say(Text)
engine.runAndWait()