#!/usr/bin/env python3
import os
from gtts import gTTS
cwd = os.getcwd()
os.mkdir('mp3')
text = "Hello Matt how is your christmas?"
tts = gTTS(text)
tts.save("mp3/hi.mp3")
