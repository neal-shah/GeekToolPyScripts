#!/usr/local/bin/python3

import subprocess
import re
import psutil

def bytes_to_mb(size_in_bytes):
    mb = size_in_bytes / 1024 / 1024
    return int(mb)


def tab_level(memoryInt):
    numberCount = len(str(memoryInt))
    tablevel = 1

    if numberCount == 3 or numberCount == 4:
        tablevel = 2

    return '\t' * tablevel


totalMem = bytes_to_mb(psutil.virtual_memory().total)
freeMem = bytes_to_mb(psutil.virtual_memory().free)
activeMem = bytes_to_mb(psutil.virtual_memory().active)
inactiveMem = bytes_to_mb(psutil.virtual_memory().inactive)

print(str(totalMem) + tab_level(totalMem) + ":\tTotal Memory (MB)")
print(str(freeMem) + tab_level(freeMem) + ":\tFree Memory (MB)")
print(str(activeMem) + tab_level(activeMem) + ":\tActive Memory (MB)")
print(str(inactiveMem) + tab_level(inactiveMem) + ":\tInactive Memory (MB)")