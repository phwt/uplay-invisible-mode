""" Uplay Invisible Mode """
#pylint: disable=C0103, C0111, C0410, C0301, C0412, W0611
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def chkAdmin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not chkAdmin():
    print("The requested operation requires elevation (Run as administrator).")
    sys.exit()

def addRule():
    if not os.path.isfile('C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\upce.exe'):
        print("\"upc.exe\" is not located in its default location")
        print("(Default: \"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\upc.exe\")")
        print("\nPlease enter full path to \"upc.exe\"")
        input("> ")
    print("Adding \"UplayOfflineMode\" to Windows Firewall Outbound Rules")

if not subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineModee" | findstr "no rules"', shell=True, stdout=DEVNULL, stderr=DEVNULL):
    addRule()

sys.exit()

def curSts():
    print("Enabled:", "True" if subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"',\
     shell=True, stdout=DEVNULL, stderr=DEVNULL) else "False")

print("Current Status")
curSts()

while True:
    sts = input("\nChange Rule Status (0 = Disable, 1 = Enable, Return = Exit): ")
    if sts == "0":
        subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no', shell=True, stdout=DEVNULL, stderr=DEVNULL)
    elif sts == "1":
        subprocess.call('netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=yes', shell=True, stdout=DEVNULL, stderr=DEVNULL)
    else:
        break
    print("Rule Status Updated")
    curSts()
