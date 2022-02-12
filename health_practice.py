#!/usr/bin/env python3
# New file created
import psutil
#import emails
import os
import sys
import shutil
import socket

# check cpu_usage is greater than 80%


def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        error_message = "Error --CPU Usage is over 80%"
        return error_message
    else:
        return "Cpu usage is at {}%".format(cpu_usage)

# check if disk space is below 20%


def disk_space():
    disk_usage = shutil.disk_usage("/")
    disk_total = disk_usage.total
    disk_free = disk_usage.used
    total_space = disk_free/disk_total * 100
    if total_space > 20:
        error_message = "Error --Available disk space is lower than 20%"
        return error_message
    else:
        return "Disk usage is at {}".format(total_space)

# Report an error if available memory is less than 500mb


def memory_space():
    available = psutil.virtual_memory().available
    available_in_mb = available / 1024 ** 2
    if available_in_mb < 500:
        error_message = "Error --Available memory is less than 500MB."
        return error_message
    else:
        return "There is {} available in MB.".format(available_in_mb)

# Report an error if the hostname localhost is not resolved to '127.0.0.1'


def check_localhost():
    host = socket.gethostbyname('localhost')
    if not host:
        error_message = "Error --localhost cannot be resolved to 127.0.0.1"
        return error_message
    else:
        return "host's name is {}.".format(host)



def main():
    #sender = "automation@example.com"
    #receiver = "{}@example.com".format(os.environ.get('USER'))

    error_message = cpu_check(), disk_space(), memory_space(), check_localhost()

    subject = error_message
    print(subject)
    #body = "Please check your system and resolve the isssue as soon as possible"
    #message = emails.generate_email_without_attachment(
        #sender=sender, recipient=receiver, subject=subject, body=body)
    #emails.send(message)


if __name__ == "__main__":
    main()
