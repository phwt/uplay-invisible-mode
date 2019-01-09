""" Uplay Invisible mode - Enable invisible mode for Uplay client.
When enabled All online services will be disabled but in-game services will still accessible.
"""
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
import pathlib

from netsh_function import *

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

    Label(main, text="Uplay Invisible Mode", font='Helvetica 11 bold').grid(row=0, column=0, padx=(30, 30), pady=(20, 10))
    Label(main, text=f"Status: {'Enabled' if status() else 'Disabled'}").grid(row=1, column=0)
    Button(main, text='Enable' if not status() else 'Disable').grid(row=2, column=0, pady=(5, 20))

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
        
        add_rule(file_path=pathlib.WindowsPath(filename))
        messagebox.showinfo("Rule added", "Setup is now complete. Please reopen the application")
        return False
    return True

if __name__ == '__main__':
    check_admin()
    if gui_setup():
        gui_main()
