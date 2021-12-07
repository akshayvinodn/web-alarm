from gtts import gTTS
from playsound import playsound
text="hello"
ts=gTTS(text,lang='en')
ts.save("voice.mp3")
playsound("voice.mp3")