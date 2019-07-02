import re
import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
vtt_file = os.path.split(filename)[1]
outputFolder = os.path.split(filename)[0]
os.chdir(outputFolder)

# vtt file to strip date time stamps from
file = open(vtt_file, 'r')
input_vtt = file.read()

# regular expression to remove timestamps
regex = r"^[\d\s\n].*\n"
test_str = input_vtt
subst = ""

# output the results to a text file with the original filename plus output.txt
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
if result:
    output = open(vtt_file + "-output.txt", "w+")
    output.write(result)
    output.close()
