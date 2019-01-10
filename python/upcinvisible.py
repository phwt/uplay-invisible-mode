""" Uplay Invisible mode - Enable invisible mode for Uplay client.
When enabled All online services will be disabled but in-game services will still accessible.
"""
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess, ctypes, sys, pathlib, webbrowser

netsh_call = lambda i: subprocess.call(i, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def check_admin():
    """ Prompt user with UAC dialog if the application is not run with administrator rights """
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        if getattr(sys, 'frozen', False):
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.executable, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def gui_main():
    """ Application's main GUI """
    main = Tk()
    main.resizable(0,0)
    main.title("")
    main.iconbitmap('uplay_icon.ico')

    menubar = Menu(main)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Settings", command=gui_settings)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=main.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    menubar.add_command(label="About", command=gui_about)
    main.config(menu=menubar)

    statusText, buttonText = StringVar(), StringVar()

    status = lambda: netsh_call('netsh advfirewall firewall show rule name="Uplay Invisible Mode" | findstr "No" | findstr /V "Edge"')
    toggle_rule = lambda: netsh_call(f'netsh advfirewall firewall set rule name="Uplay Invisible Mode" new enable={"yes" if not status() else "no"}')

    toggle_status = lambda: (statusText.set(f"Status: {'Enabled' if status() else 'Disabled'}"),\
                            buttonText.set('Enable' if not status() else 'Disable'),)
    toggle = lambda: (toggle_rule(), toggle_status())
    
    toggle_status()

    Label(main, text="Uplay Invisible Mode", font='Helvetica 11 bold').grid(row=0, column=0, padx=(30, 30), pady=(20, 10))
    Label(main, textvariable=statusText).grid(row=1, column=0)
    Button(main, textvariable=buttonText, command=toggle).grid(row=2, column=0, pady=(5, 20))

    main.mainloop()

def gui_setup():
    """ UI for rule checking and adding process """
    check_rule = lambda: netsh_call('netsh advfirewall firewall show rule name="Uplay Invisible Mode" | findstr "no rules"')

    while not check_rule():
        root = Tk()
        root.withdraw()

        messagebox.showinfo("Rule not found", "Please select \"upc.exe\" from your Uplay installation folder")
        filename = filedialog.askopenfilename(initialdir='C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher',
            title="Select upc.exe",
            filetypes=(("\"upc.exe\" Executable file","upc.exe"),)
        )

        if "upc.exe" not in filename.lower() or filename == "":
            if not messagebox.askretrycancel("Error", "Invalid file!"):
                return
            continue

        add_rule = lambda i: netsh_call(f'netsh advfirewall firewall add rule name="Uplay Invisible Mode" dir=out action=block enable=no program="{i}"')
        add_rule(pathlib.WindowsPath(filename))
        messagebox.showinfo("Rule added", "Setup is now complete. Please reopen the application")
        return False
    return True

def gui_settings():
    """ UI for application's settings """
    settings = Tk()
    settings.resizable(0,0)
    settings.title("Settings")
    settings.iconbitmap('uplay_icon.ico')

    delete_rule = lambda: netsh_call('netsh advfirewall firewall delete rule name="Uplay Invisible Mode"')

    def remove_rule():
        """ Remove "Uplay Invisible Mode" rule """
        delete_rule()
        messagebox.showinfo("Rule removed", "Rule removed. The application will now close")
        sys.exit()
    def change_location():
        """ Change "upc.exe" location """
        delete_rule()
        gui_setup()
        sys.exit()

    Label(settings, text="Settings", font='Helvetica 10 bold').grid(row=0, column=0, pady=(20, 10))
    Button(settings, text="Change \"upc.exe\" location", command=change_location).grid(row=1, column=0, padx=(40, 40))
    Button(settings, text="Remove \"Uplay Invisible Mode\" rule", command=remove_rule).grid(row=2, column=0, pady=(5, 20))

    settings.mainloop()

def gui_about():
    """ UI for application's about """
    about = Tk()
    about.resizable(0,0)
    about.title("About")
    about.iconbitmap('uplay_icon.ico')
    
    giturl = lambda: webbrowser.open("https://github.com/phwt/uplay-invisible-mode")

    Label(about, text="Uplay Invisible Mode - 2.1", font='Helvetica 10 bold').grid(row=0, column=0, pady=(20, 10))
    Label(about, text="By - phwt").grid(row=1, column=0)
    Button(about, text="View this project on GitHub", command=giturl).grid(row=1, column=0)
    Label(about, text="This project is not affiliated with Ubisoft Entertainment").grid(row=2, column=0, padx=(30, 30), pady=(5, 20))

    about.mainloop()

if __name__ == '__main__':
    check_admin()
    if gui_setup():
        gui_main()
