import sys
import os
from cx_Freeze import setup, Executable

files = ['db_manager', 'forest-dark', 'getpath', 'Login_Screen', 'Menu_Screen', 'Register_Screen', 'strings', 'users',
        'wipper.db', 'forest-dark.tcl', 'Login.py', 'Menu.py', 'Products.py', 'Records.py', 'Register.py', 'Clients.py', 'exit.png']

exe = Executable(script="login.py", base="Win32GUI")

setup(name="Wipper", version=1.0, options={"build.exe": {'include_files': files}}, executables=[exe])