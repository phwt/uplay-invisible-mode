""" Uplay Invisible mode - Enable invisible mode for Uplay client.
When enabled All online services will be disabled but in-game services will still accessible.
"""
from tkinter import *
from tkinter.ttk import *
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def mainUI():
    """ Main application UI """
    main = Tk()
    main.resizable(0,0)
    kill = lambda: main.destroy()

    if not chkAdmin(): #Display error message if not running with administratpr rights
        pass
    if not chkRule(): #Proceed to rule adding if rule not present in Windows Firewall
        pass

    Label(main, text="Status: ").grid(row=0, column=0, padx=(30, 30), pady=(20, 10))
    Button(main, text="Hello").grid(row=1, column=0, padx=(30, 30), pady=(0, 20))

    main.mainloop()

def chkAdmin():
    """ Display error dialog if the application does not run with elevated permission """
    try:
        isAdmin = os.getuid() == 0
    except AttributeError:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not isAdmin:
        errDialog = Tk()
        errDialog.resizable(0,0)

        kill = lambda: errDialog.destroy()
        Label(errDialog, text="The requested operation requires elevation.\nPlease start the application with administratpr rights.").grid(row=0, column=0, padx=(30, 30), pady=(20, 0))
        Button(errDialog, text="Exit", command=kill).grid(row=2, column=0, padx=(30, 30), pady=(10, 20))

        errDialog.mainloop()
        return False
    return True

def chkStatus():
    """ Return if the rule is enabled or not """
    cmd = 'netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"'
    return subprocess.call(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)

def chkRule():
    pass

mainUI()