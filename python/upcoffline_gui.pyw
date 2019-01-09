""" Uplay Invisible mode - Enable invisible mode for Uplay client.
When enabled All online services will be disabled but in-game services will still accessible.
"""
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess, ctypes, sys, pathlib

netsh_call = lambda i: subprocess.call(i, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

check_rule = lambda: netsh_call('netsh advfirewall firewall show rule name="Uplay Invisible Mode" | findstr "no rules"')
status = lambda: netsh_call('netsh advfirewall firewall show rule name="Uplay Invisible Mode" | findstr "No" | findstr /V "Edge"')
add_rule = lambda i: netsh_call(f'netsh advfirewall firewall add rule name="Uplay Invisible Mode" dir=out action=block enable=no program={i}')
toggle_rule = lambda: netsh_call(f'netsh advfirewall firewall set rule name="Uplay Invisible Mode" new enable={"yes" if not status() else "no"}')

def check_admin():
    """ Prompt user with UAC dialog if the application is not run with administrator rights """
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def gui_main():
    """ Application's main GUI """
    main = Tk()
    main.resizable(0,0)
    main.title("")
    main.iconbitmap('uplay_icon.ico')

    def toggle():
        toggle_rule()
        statusText.set(f"Status: {'Enabled' if status() else 'Disabled'}")
        buttonText.set('Enable' if not status() else 'Disable')

    statusText, buttonText = StringVar(), StringVar()
    
    statusText.set(f"Status: {'Enabled' if status() else 'Disabled'}")
    buttonText.set('Enable' if not status() else 'Disable')

    Label(main, text="Uplay Invisible Mode", font='Helvetica 11 bold').grid(row=0, column=0, padx=(30, 30), pady=(20, 10))
    Label(main, textvariable=statusText).grid(row=1, column=0)
    Button(main, textvariable=buttonText, command=toggle).grid(row=2, column=0, pady=(5, 20))

    main.mainloop()

def gui_setup():
    """ UI for rule checking and adding process """
    while not check_rule():
        root = Tk()
        root.withdraw()

        messagebox.showinfo("Rule not found", "Please select \"upc.exe\" from your Uplay installation folder")
        filename = filedialog.askopenfilename(initialdir='C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',
            title="Select upc.exe",
            filetypes=(("Executable file","*.exe"),)
        )

        if "upc.exe" not in filename.lower() or filename == "":
            if not messagebox.askretrycancel("Error", "Invalid file!"):
                return
            continue
        
        add_rule(pathlib.WindowsPath(filename))
        messagebox.showinfo("Rule added", "Setup is now complete. Please reopen the application")
        return False
    return True

if __name__ == '__main__':
    check_admin()
    if gui_setup():
        gui_main()
