
#!/usr/bin/env python3

import platform
import os
import shutil
import ctypes
from datetime import datetime


def get_cpu_name():
    if platform.system() == "Windows":
        try:
            import winreg

            key_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                return winreg.QueryValueEx(key, "ProcessorNameString")[0].strip()
        except OSError:
            return platform.processor() or "Unknown"

    try:
        with open("/proc/cpuinfo", "r") as cpu_file:
            for line in cpu_file:
                if "model name" in line:
                    return line.split(":", 1)[1].strip()
    except OSError:
        pass

    return platform.processor() or "Unknown"


def get_total_ram_gb():
    if platform.system() == "Windows":
        class MemoryStatusEx(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        status = MemoryStatusEx()
        status.dwLength = ctypes.sizeof(status)
        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            raise ctypes.WinError()
        return status.ullTotalPhys / (1024 ** 3)

    try:
        with open("/proc/meminfo", "r") as mem_file:
            for line in mem_file:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) / (1024 * 1024)
    except OSError:
        pass

    return None


# 1. Operating System Information
hostname = platform.node()
operating_system = platform.system()
os_version = platform.release()
username = os.getenv("USERNAME", os.getenv("USER", "Unknown"))
current_time = datetime.now()

# 2. Processor Information
cpu_name = get_cpu_name()
cpu_cores = os.cpu_count()

# 3. RAM Information
total_ram = get_total_ram_gb()

# 4. Storage Information
if operating_system == "Windows":
    storage_path = os.path.abspath(os.sep)
else:
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
if total_ram is None:
    print("Total RAM      : Unavailable")
else:
    print(f"Total RAM      : {total_ram:.2f} GB")

print(f"Storage Drive  : {storage_path}")
print(f"Total Storage  : {total_storage:.2f} GB")
print(f"Free Storage   : {free_storage:.2f} GB")

print("=" * 40)

# specs viewer tool
# let's make it more user-friendly by adding a simple menu to view specific informations lets try itgit pull orgin main --allow-unrelated-historiesgit pull orgin main --allow-unrelated-historiesgit pull orgin main --allow-unrelated-historiesgit pull orgin main --allow-unrelated-histories