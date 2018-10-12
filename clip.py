"""
Usage:
    clip.py save <reference_name> [<reference_value>]
    clip.py load <reference_name>                  
    clip.py delete <reference_name>
    clip.py list  
"""

import pyperclip, sys, json, os
from docopt import docopt

FILE_NAME = "clipboard.json"

def open_file():
    with open(FILE_NAME, 'r+') as file:
        return json.load(file)

def write_file(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=2)

def save_clipboard(name, dictionary, reference_value=pyperclip.paste()):
    dictionary[name] = reference_value

def load_name(name, dictionary):
    if name in dictionary:
        pyperclip.copy(dictionary[name])

def list_shelf(dictionary):
    pyperclip.copy(str(dictionary))

def delete_key(name, dictionary):
    if name in dictionary:
        del dictionary[name]

if __name__ == "__main__":
    # Make this try catch finally, or atexit module???
    arguments = docopt(__doc__)
    file_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(file_path)
    dictionary = open_file()

    if (arguments["save"]):
        save_clipboard(arguments['<reference_name>'], dictionary, arguments.get("<reference_value>"))
    elif (arguments["load"]):
        load_name(arguments['<reference_name>'],  dictionary)
        sys.exit()
    elif (arguments["list"]):
        list_shelf(dictionary)
        sys.exit()
    else:
        # Has to be delete
        delete_key(arguments["<reference_name>"], dictionary)

    write_file(dictionary)