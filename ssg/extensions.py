import sys
import importlib
from pathlib import Path

def load_module(directory, name):
    sys[0] = sys.path.insert(directory)
    importlib.import_module(name)
    sys.path.pop(sys[0])
    
def load_directory(directory):
    for path in Path.rglob(".py"):
        load_module(directory.as_posix(),path.name)
        
def load_bundled():
    directory = Path(__file__).parent / "extensions"
    load_directory(directory)
    