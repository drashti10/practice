from gtts import gTTS
import os
text = "Drashti shah is greattt"
language='en'
tts = gTTS(text=text, lang=language, slow=False)
tts.save("output.mp3")
os.system("start output.mp3")

