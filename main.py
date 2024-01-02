from pathlib import Path
from os import listdir
import json
import generators.MapGenerator as MG

OPERATING_HOME = str(Path.home()) + "\\My Games\\Blue Ocean"

print("Hello World. Operating in Source Directory " + OPERATING_HOME)
print("Performing Integrity Check on Source Directory.")
Path(OPERATING_HOME).mkdir(parents=True, exist_ok=True)

sub_files = listdir(OPERATING_HOME)

# GENERATION SEQUENCE
if not sub_files:
    print("OPERATING_HOME is empty. Creating settings file with base settings.")
    settings_file = open(OPERATING_HOME + "\\settings.json", "w")
    settings_file.write(json.dumps([{'difficulty': 1, 'fullscreen': 'False', 'autosave': 'False'}], separators=(',', ':')))
    print("settings.json generated with default settings.")
    print("Generating data folders...")
    Path(OPERATING_HOME + "\\maps").mkdir(parents=True, exist_ok=True)
    print("Done.")

print(sub_files)