#!/usr/bin/env python3
# new file created
#Python script that automatically uploads feedback in the form of a text file to a running web server.
import os
import glob
import requests
import json
#exam "http://external-ip/feedback/"
#corpwebs address is shown in first post through REST endpoint.
os.chdir('/data/feedback')
os.listdir()
for file in glob.glob("*.txt"):
    file = open(file)
    title = file.readline().strip()
    name = file.readline().strip()
    date = file.readline().strip()
    feedback = file.read()
    feedback_without_newline = feedback.replace("\n", " ")
    data = {"title": title, "name": name, "date": date,
            "feedback": feedback_without_newline}
            
    # now we need to send the data in the form of an http request.
    #external-ip will be or ip address on the vm
    response = requests.post("http://external-ip/feedback", data=data).raise_for_status()
    file.close()
