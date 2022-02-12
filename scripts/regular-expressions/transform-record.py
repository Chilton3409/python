#!/usr/bin/env python3
#New file created
import re   

def tranform_record(record):
    new_record = re.sub(r"\b(\d{3}-\d{3}-?\d{4})\b", r"+1-\1", record)
    return new_record

print(tranform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(tranform_record("Eli Jones,684-3481127,IT specialist"))
#Eli Jones,+1-684-3481127,It specialist