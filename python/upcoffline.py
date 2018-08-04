""" Uplay Invisible Mode """
#pylint: disable=C0103, C0111, C0410, C0301, C0412, W0611
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL
# import tkinter

def chkAdmin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not chkAdmin():
    print("The requested operation requires elevation (Run as administrator).")
    sys.exit()

def curSts():
    return [subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"', shell=True, stdout=DEVNULL, stderr=DEVNULL), \
    subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"', shell=True, stdout=DEVNULL, stderr=DEVNULL)]

def enable():
    subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=yes', shell=True, stdout=DEVNULL, stderr=DEVNULL)
    print("Rule Status Updated")
    print("Enabled:", "True" if curSts()[1] else "False")

def disable():
    subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no', shell=True, stdout=DEVNULL, stderr=DEVNULL)
    print("Rule Status Updated")
    print("Enabled:", "True" if curSts()[1] else "False")

print("Current Status")
print("Rule Added: " + "True" if curSts()[0] else "False")
print("Enabled:", "True" if curSts()[1] else "False")

while True:
    sts = input("\nChange Rule Status (0 = Disable, 1 = Enable, Return = Exit): ")
    if sts == "0":
        disable()
    elif sts == "1":
        enable()
    else:
        break
# tkinter._test()
