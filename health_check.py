#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket
from email.message import EmailMessage

# Critical limits that trigger alerts for easy access
cpu_max_limit = 80
min_disk_space = 20
min_memory = 500
local_host_up = True

def generate_error_report(alert_generated): 
    """ function used to generated an EmailMessage object for sending"""    # to be moved to emails.py ? 
    msg = EmailMessage()
    # msg["From"]='automation@example.com'    
    msg["From"]='weetabix4@gmail.com'
    msg["To"]= 'russfrancis99@gmail.com' # to comment out
    # msg["To"]= 'username from connection panel'

    msg["Subject"]= alert_generated
    msg.set_content("Please check your system and resolve the issue as soon as possible")
    return msg

# For testing only. Comment out when tests are working.  
# cpu_use_pc = 55
# available_disk_space_pc = 12
# available_memory_MB = 600
# local_host_up = True

def check_cpu():
    return psutil.cpu_percent(interval=1) > cpu_max_limit

def check_diskspace():
    total, used, free = shutil.disk_usage('/') # should I use root? 
    free_percent = free / total * 100
    return free_percent < min_disk_space

def check_memory():
    # Get available memory using psutil.virtual_memory()[1]  note: this returns a named
    available_memory = psutil.virtual_memory()[1]
    #convert to megabytes
    available_memory_megabytes = available_memory / (1024 ** 2)
    return available_memory_megabytes < min_memory 

def check_localhost():
    # Diagnose whether lcoal_host is up and running using? 
    localhost = socket.gethostbyname('localhost')
    return localhost== "127.0.0.1"


def health_check():
# Complete the script to check the system statistics every 60 seconds,
# and trigger sending of appropriate alert if issue detected.  
    if  check_cpu():
        alert = (f"Error-CPU usage is over {cpu_max_limit}%")
        emails.send_gmail(generate_error_report(alert))
    
    elif check_diskspace():
        alert = (f"Error-Available disk space is less than {min_disk_space}%")
        emails.send_gmail(generate_error_report(alert))

    elif check_memory():
        alert = (f"Error - available memory is less that {min_memory} MB")
        emails.send_gmail(generate_error_report(alert))
    
    elif not check_localhost():   # note assume local host is up/true and only trigger when down (ie not true)
        alert = ("Error - localhost cannot be resolved to 127.0.0.1")
        emails.send_gmail(generate_error_report(alert))
    else: alert ="Health Check complete. All tests passed"
    # for debugging only
    print(alert)
    return None 
    
if __name__=="__main__":
    alert = health_check()
