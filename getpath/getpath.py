import inspect
from pathlib import Path

def getPath():
    current_frame = inspect.currentframe()
    caller_frame = inspect.getouterframes(current_frame, 2)
    script_name = Path(caller_frame[-1].filename).stem

    OUTPUT_PATH = Path(__file__).parent.parent

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
