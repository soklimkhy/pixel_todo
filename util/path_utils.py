import sys, os

def resource_path(relative_path):
    """Return path compatible with PyInstaller .exe or dev run."""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def base_dir():
    """Return the folder where todolist_app.exe or main.py is running."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.abspath(".")

CONFIG_PATH = os.path.join(base_dir(), "config.json")