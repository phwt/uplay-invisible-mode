""" Uplay Invisible mode - Enable invisible mode for Uplay client.
When enabled All online services will be disabled but in-game services will still accessible.
"""
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess, ctypes, os, sys
from subprocess import Popen, DEVNULL

def mainUI():
    """ Main application UI """
    kill = lambda: main.destroy()
    chkAdmin()
    if not chkRule():
        sys.exit()

    main = Tk()
    main.resizable(0,0)

    Label(main, text="Status: ").grid(row=0, column=0, padx=(30, 30), pady=(20, 10))
    Button(main, text="Hello").grid(row=1, column=0, padx=(30, 30), pady=(0, 20))

    main.mainloop()

def chkAdmin():
    """ Display error dialog if the application does not run with elevated permission """
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def status():
    """ Return if the rule is enabled or not """
    cmd = 'netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"'
    return subprocess.call(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)

def chkRule():
    """ Check for rule existence if not prompt user to set up the rule """
    # return True
    if not subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"',\
     shell=True, stdout=DEVNULL, stderr=DEVNULL):
        messagebox.showwarning("Rule not found",\
        'Please proceed to set up. \n(The application will prompt you to select the "upc.exe" file)')
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',title = "Select upc.exe",filetypes = (("Executable file","*.exe"),))
        print(root.filename)
        subprocess.call("netsh advfirewall firewall add rule name=\"UplayOfflineMode\" dir=out action=block enable=no program=" + root.filename, shell=True, stdout=DEVNULL, stderr=DEVNULL)
        messagebox.showinfo("Rule added", "Setup is now complete. Please reopen the application")
        return False
    return True



mainUI()
# root = Tk()
# root.filename = filedialog.askopenfilename(initialdir = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',title = "Select upc.exe",filetypes = (("Executable file","*.exe"),))
# print(root.filename)
# messagebox.showinfo("Title", "a Tk MessageBox")
