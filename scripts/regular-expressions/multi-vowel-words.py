#!/usr/bin/env python3
#New file created
import re

def multt_vowel_words(text):
    pattern = r"\w*[aeiou]{3}\w*"
    result = re.findall(pattern, text)
    return result

print(multt_vowel_words("Life is beautiful"))
# ['beautiful']

print(multt_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multt_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']
