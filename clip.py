"""
Usage:
    clip.py save <reference_name>
    clip.py load <reference_name>                  
    clip.py delete <reference_name>
    clip.py list  
"""

import shelve, pyperclip, sys
from docopt import docopt

def save_clipboard(name, mcbShelf):
    mcbShelf[name] = pyperclip.paste()

def load_name(name, mcbShelf):
    if name in mcbShelf:
        pyperclip.copy(mcbShelf[name])

def list_shelf(mcbShelf):
    dictionary = {}
    for x in mcbShelf.keys():
        # This is dangerous if you have a really large file, but I won't 
        dictionary[x] = mcbShelf[x]
    pyperclip.copy(str(dictionary))

def delete_key(name, mcbShelf):
    if name in mcbShelf:
        del mcbShelf[name]

if __name__ == "__main__":
    # Make this try catch finally, or atexit module???
    arguments = docopt(__doc__)
    mcbShelf = shelve.open('mcb')

    if (arguments["save"]):
        save_clipboard(arguments['<reference_name>'], mcbShelf)
    elif (arguments["load"]):
        load_name(arguments['<reference_name>'],  mcbShelf)
    elif (arguments["list"]):
        list_shelf(mcbShelf)
    else:
        # Has to be delete
        delete_key(arguments["<reference_name>"], mcbShelf)

    mcbShelf.close()