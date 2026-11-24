#!/usr/bin/env python3

import platform  
import os 
from datetime import datetime

# Collect system information
hostname = platform.node()
operating_system = platform.system()
os_version = platform.release()
username = os.getenv("USER")
current_time = datetime.now()

# Display system report
print("==============================")
print("       SYSTEM INFORMATION")
print("==============================")

print(f"Hostname : {hostname}")
print(f"OS       : {operating_system}")
print(f"Version  : {os_version}")
print(f"Username : {username}")
print(f"Date     : {current_time}")

print("==============================")
