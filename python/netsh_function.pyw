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

def modify_rule(rule_name, state):
    """ Enable/Disable specific rule, 0 = Disable / 1 = Enable """
    subprocess.call(
        f"netsh advfirewall firewall set rule name={rule_name} new enable={'yes' if state else 'no'}", 
        shell=True, 
        stdout=DEVNULL, 
        stderr=DEVNULL
    )

netsh_call = lambda i: subprocess.call(i, shell=True, stdout=DEVNULL, stderr=DEVNULL)
check_rule = lambda: netsh_call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"')
status = lambda: netsh_call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"')
