#!/usr/bin/env python3

from gtts import gTTS

text = "Hello Matt how is your christmas?"
tts = gTTS(text)
tts.save("/Users/nathanchilton/scripts/hi.mp3")
