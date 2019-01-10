import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/phwts/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/phwts/AppData/Local/Programs/Python/Python36/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['C:/Users/phwts/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll', 'C:/Users/phwts/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('upcinvisible.py', base=base, icon="uplay_icon.ico")
]

setup(name='Uplay Invisible Mode',
      version = '2.1.1',
      description = 'Enable an invisible mode for Uplay Client',
      options = dict(build_exe = buildOptions),
      executables = executables)
