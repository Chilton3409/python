#!/usr/bin/env python3
import os
from gtts import gTTS
cwd = os.getcwd()
os.mkdir('mp3')
text = "Hello, how are you today?"
tts = gTTS(text)
tts.save("mp3/hi.mp3")
