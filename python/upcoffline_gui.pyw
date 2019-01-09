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
        sys.exit()

def addRule(file_path="K:\\upc.exe", rule_name="UplayOfflineMode"):
    """ Add rule to Windows Firewall """
    subprocess.call("netsh advfirewall firewall add rule name="+ rule_name +" dir=out action=block enable=no program=" + file_path, shell=False, stdout=DEVNULL, stderr=DEVNULL)
    print("Rule", rule_name, "for", file_path, "added")

def modifyRule(state, rule_name="UplayOfflineMode"):
    """ Enable/Disable specific rule, 0 = Disable / 1 = Enable """
    if state:
        subprocess.call("netsh advfirewall firewall set rule name="+ rule_name +" new enable=yes", shell=False, stdout=DEVNULL, stderr=DEVNULL)
        print("Rule", rule_name, "Enabled")
    else:
        subprocess.call("netsh advfirewall firewall set rule name="+ rule_name +" new enable=no", shell=False, stdout=DEVNULL, stderr=DEVNULL)
        print("Rule", rule_name, "Disabled")

def status():
    """ Return if the rule is enabled or not """
    cmd = 'netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "No" | findstr /V "Edge"'
    return subprocess.call(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)

def chkRule():
    """ Check for rule existence if not prompt user to set up the rule """
    # return True
    if not subprocess.call('netsh advfirewall firewall show rule name="UplayOfflineMode" | findstr "no rules"',\
     shell=True, stdout=DEVNULL, stderr=DEVNULL):
        filename = ""
        while filename == "":
            messagebox.showinfo("Rule not found", "Please select \"upc.exe\" from your Uplay installation folder")
            filename = filedialog.askopenfilename(initialdir = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',title = "Select upc.exe",filetypes = (("Executable file","*.exe"),))
        messagebox.showinfo("", "netsh advfirewall firewall add rule name=\"UplayOfflineMode\" dir=out action=block enable=no program=\"" + filename.replace("\\", "\\\\") + "\"")
        subprocess.call("netsh advfirewall firewall add rule name=\"UplayOfflineMode\" dir=out action=block enable=no program=\"" + filename.replace("/", "\\") + "\"", shell=True, stdout=DEVNULL, stderr=DEVNULL)
        messagebox.showinfo("Rule added", "Setup is now complete. Please reopen the application")
        return False
    return True



# mainUI()
# chkAdmin()

chkRule()

# filename = filedialog.askopenfilename(initialdir = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher', title="Select upc.exe", filetypes=(("Executable file","*.exe"),))
# print(filename)

# addRule()

# this = Tk()
# addme = lambda: addRule
# Button(this, text="Addme", command=addRule).pack()
# this.mainloop()
# subprocess.call("netsh advfirewall firewall add rule name=\"UplayOfflineMode\" dir=out action=block enable=no program=\"C:/Users/phwt/Desktop/logisim-win-2.7.1.exe\"", shell=True, stdout=DEVNULL, stderr=DEVNULL)
# root = Tk()
# root.filename = filedialog.askopenfilename(initialdir = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',title = "Select upc.exe",filetypes = (("Executable file","*.exe"),))
# print(root.filename)
# messagebox.showinfo("Title", "a Tk MessageBox")
