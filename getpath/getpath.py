import inspect
from pathlib import Path
import subprocess


current_frame = inspect.currentframe()
caller_frame = inspect.getouterframes(current_frame, 2)
script_name = Path(caller_frame[-1].filename).stem

OUTPUT_PATH = Path(__file__).parent.parent

def getPath():
    match script_name:
        case "Login":
            assets_path = OUTPUT_PATH

        case "Register":
            assets_path = OUTPUT_PATH / 'Register_Screen' / 'build' / 'assets' / 'frame0'

        case "Menu":
            assets_path = OUTPUT_PATH / 'Wipper_Menu' / 'build' / 'assets' / 'frame0'

        case other:
            print("huh?", OUTPUT_PATH)

    return assets_path


def register_screen():
    goto_path = OUTPUT_PATH / 'Register.py'
    subprocess.Popen(["python", str(goto_path)])

def wipper_menu():
    goto_path = OUTPUT_PATH / 'Menu.py'
    subprocess.Popen(["python", str(goto_path)])

def login_screen():
    goto_path = OUTPUT_PATH / 'Login.py'
    subprocess.Popen(["python", str(goto_path)])
