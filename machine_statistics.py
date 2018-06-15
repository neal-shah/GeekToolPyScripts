#!/usr/local/bin/python3

import subprocess
import re
import psutil

def bytes_to_mb(size_in_bytes):
    mb = size_in_bytes / 1024 / 1024
    return int(mb)


def tab_level(integer):
    numberCount = len(str(integer))
    tablevel = 1

    if numberCount == 3 or numberCount == 4:
        tablevel = 2
    elif numberCount == 2:
        tablevel = 1
    elif numberCount == 1:
        tablevel = 3

    return '\t' * tablevel


def get_memory_stats():
    totalMem = bytes_to_mb(psutil.virtual_memory().total)
    freeMem = bytes_to_mb(psutil.virtual_memory().free)
    activeMem = bytes_to_mb(psutil.virtual_memory().active)
    inactiveMem = bytes_to_mb(psutil.virtual_memory().inactive)

    print('\nMEMORY')
    print(str(totalMem) + tab_level(totalMem) + ':\tTotal Memory (MB)')
    print(str(freeMem) + tab_level(freeMem) + ':\tFree Memory (MB)')
    print(str(activeMem) + tab_level(activeMem) + ':\tActive Memory (MB)')
    print(str(inactiveMem) + tab_level(inactiveMem) + ':\tInactive Memory (MB)')


def get_cpu_stats():
    cores = psutil.cpu_count()
    cpu = psutil.cpu_percent(interval=1)
    
    print('\nCPU')
    print(str(cores) + tab_level(cores) + ':\tCores')
    print(str(cpu) + tab_level(cpu) + ':\tCPU (%)')


def get_battery_stats():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged == False: 
        plugged="On Battery"
    else: plugged="Plugged In"

    print('\nBATTERY')
    print(str(percent) + tab_level(percent) + ':\tLevel (%) | ' + plugged)

get_memory_stats()
get_cpu_stats()
get_battery_stats()