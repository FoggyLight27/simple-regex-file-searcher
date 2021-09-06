# simple-regex-file-searcher
A quickly made regex powered python script to search for files on your PC.

Arguments: Your search term in regex, must be a full match for the file name. By default, this will search your entire C drive for a file by that name, and print the paths of all found files.

Made in Python 3.9.7

Known bugs: `ValueError: list.remove(x): x not in list` when attempting to use path= argument

