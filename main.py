import os
from sys import argv
import re

def find(strRegex, startPath, find_first_only=False, print_txts=False, verbose=False):
    regex = re.compile(strRegex, re.IGNORECASE)
    matches = []
    for path, folders, files in os.walk(startPath):
        for file in files:
            if regex.match(file):
                if verbose: print("Found " + path + "\\" + file)
                if print_txts and ".txt" in file:
                    try:
                        with open(path + "\\" + file) as f:
                            for line in f:
                                print(line)
                    except Exception:
                        print("Failed to read " + file)
                matches.append(path + "\\" + file)
                if find_first_only: return matches
    if not matches and verbose: print("Couldn't find \"" + strRegex + '"')
    return matches

if __name__ == "__main__":
    args = argv[1:]
    path = "C:\\"
    verbose = False
    print_txts = False
    for arg in argv[1:]:
        arg = arg.lower()
        if arg == "-p":
            args.remove(arg)
            print_txts = True
        elif arg == "-v":
            args.remove(arg)
            verbose = True
        elif arg.startswith("path="):
            args.remove(arg)
            path = arg.removeprefix("path=")
    input = " ".join(args)
    output = find(input, path, verbose=verbose, print_txts=print_txts)
    if not verbose:
        for path in output:
            print("Found " + path)