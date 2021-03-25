#!/usr/bin/env python3
import os
import datetime

def file_date(filename):
    #create the file in current directory
    os.mkdir(filename)
    timestamp = os.path.getmtime(filename)
    #convert the timestamp into a readable format, then into a string
    con = datetime.datetime.fromtimestamp(timestamp)
    only = con.date()
    #Return only the date portion
    return ("{}".format(only))

print(file_date("newfile.txt"))
#should be todays date in the format of yyyy-mm-dd