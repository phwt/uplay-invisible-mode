from cx_Freeze import setup, Executable

base = None    

executables = [Executable("upcoffline_gui.pyw", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Uplay Invisible Mode",
    options = options,
    version = "2.0",
    executables = executables
)
