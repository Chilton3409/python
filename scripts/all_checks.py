#!/usr/bin/env python3
#New file created
import os
def check_reboot():
    """Returns true if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")
def main():
    pass

main()
