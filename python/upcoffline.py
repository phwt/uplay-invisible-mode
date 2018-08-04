""" Uplay Invisible Mode """
#pylint: disable=C0103, C0111, C0410, C0301
import subprocess, ctypes, os, sys
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
    """ Return current status of the rule"""
    return [subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"', shell=True), \
    subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"', shell=True)]
# subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no', shell=True)

def enable():
    subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=yes', shell=True)
    print("Enabled: " + "True" if curSts()[1] else "False")

def disable():
    subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no', shell=True)
    print("Enabled: " + "True" if curSts()[1] else "False")

print("Current Status")
print("Rule Added: " + "True" if curSts()[0] else "False")
print("Enabled: " + "True" if curSts()[1] else "False")
disable()
# tkinter._test()
