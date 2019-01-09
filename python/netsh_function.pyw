""" Uplay Invisible mode - netsh_function
Store function which using netsh functionality
"""
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def add_rule(rule_name="UplayOfflineMode", file_path="C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\upc.exe"):
    """ Add rule to Windows Firewall """
    subprocess.call(
        f"netsh advfirewall firewall add rule name={rule_name} dir=out action=block enable=no program={file_path}", 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    # print(f"Rule {rule_name} for {file_path} added")

def modify_rule(rule_name, state):
    """ Enable/Disable specific rule, 0 = Disable / 1 = Enable """
    # state, message = ("yes", "Enabled") if state else ("no", "Disabled")
    subprocess.call(
        f"netsh advfirewall firewall set rule name={rule_name} new enable={'yes' if state else 'no'}", 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )
    # print(f"Rule {rule_name} {message}")

def check_rule():
    """ Return if the rule exist or not """
    return subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"',
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL
    )

def status():
    """ Return if the rule is enabled or not """
    return not subprocess.call("netsh advfirewall firewall show rule name='UplayOfflineMode' | findstr 'No' | findstr /V 'Edge'",
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL
    )

# check_admin()
# filename = "K:\\upc.exe"
# add_rule(file_path=filename)
# add_rule("UplayOfflineMode", "K:\\upc.exe")
# print(check_rule())
# print(status())
