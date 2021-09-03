import os
from sys import argv
import re

def find(strRegex, startPath="C:\\", full=False, printTxts=False):
    regex = re.compile(strRegex, re.IGNORECASE)
    found = False
    for path, folders, files in os.walk(startPath):
        for file in files:
            if regex.match(file):
                print("Found " + path + "\\" + file)
                found = True
                if printTxts and ".txt" in file:
                    try:
                        with open(path + "\\" + file) as f:
                            for line in f:
                                print(line)
                    except Exception:
                        print("Failed to read txt file")
                if not full: return
    if not found: print("Couldn't find \"" + strRegex + '"')

input = " ".join(argv[1:])
find(input, full=True)