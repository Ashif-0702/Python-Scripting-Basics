
#!/usr/bin/env python3

import platform
import os
import shutil
from datetime import datetime

# 1. Operating System Information
hostname = platform.node()
operating_system = platform.system()
os_version = platform.release()
username = os.getenv("USER", "Unknown")
current_time = datetime.now()

# 2. Processor Information
cpu_name = "Unknown"

try:
    with open("/proc/cpuinfo", "r") as cpu_file:
        for line in cpu_file:
            if "model name" in line:
                cpu_name = line.split(":", 1)[1].strip()
                break
except OSError:
    pass

cpu_cores = os.cpu_count()

# 3. RAM Information
total_ram = 0

try:
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemTotal:"):
                total_ram = int(line.split()[1]) / (1024 * 1024)
                break
except OSError:
    pass

# 4. Storage Information
storage_path = "/mnt/d" if os.path.exists("/mnt/d") else "/"
disk = shutil.disk_usage(storage_path)

total_storage = disk.total / (1024 ** 3)
free_storage = disk.free / (1024 ** 3)

# 5. Display System Report
print("=" * 40)
print("         SYSTEM INFORMATION")
print("=" * 40)

print(f"Hostname       : {hostname}")
print(f"Operating System: {operating_system}")
print(f"OS Version     : {os_version}")
print(f"Username       : {username}")
print(f"Date           : {current_time}")

print("-" * 40)
print("         HARDWARE SPECIFICATIONS")
print("-" * 40)

print(f"Processor      : {cpu_name}")
print(f"CPU Cores      : {cpu_cores}")
print(f"Total RAM      : {total_ram:.2f} GB")

print(f"Storage Drive  : {storage_path}")
print(f"Total Storage  : {total_storage:.2f} GB")
print(f"Free Storage   : {free_storage:.2f} GB")

print("=" * 40)
