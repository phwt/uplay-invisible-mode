from cx_Freeze import setup, Executable

base = None    

executables = [Executable("upcoffline.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Uplay Invisible Mode",
    options = options,
    version = "0.1",
    executables = executables
)