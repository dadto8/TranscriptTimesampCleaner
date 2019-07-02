## **Transcript Timesamp Cleaner v2**

Python script to remove time / date stamps from vtt transcription files from Zoom.  easier to read when the timestamps are removed.

The python code has been converted to an exe with [PyInstaller](https://www.pyinstaller.org/).

###  **Instructions**

Place vtt-clean_v2.exe any place you want (preferably easy to find or access)


Example of raw transcrtion vtt file.
![Sample.vtt raw](/img/vtt-preclean.png)

Then double click vtt-cleanup.exe to run the cleaner, choose the file you want to clean from the dialog that comes up. after selecting the vtt file to be cleaned vtt-clean will make a new file with -output.txt at the end with only the text from the vtt file.

Example of cleaned Transcription.
![sample.txt post process](/img/vtt-cleaned.png)

Code used in vtt-cleanup.py
```Python
import re
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
vtt_file = os.path.split(filename)[1]
outputFolder = os.path.split(filename)[0]
os.chdir(outputFolder)

file = open(vtt_file, 'r')
input_vtt = file.read()

regex = r"^[\d\s\n].*\n"
test_str = input_vtt
subst = ""

result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
if result:
    output = open(vtt_file + "-output.txt", "w+")
    output.write(result)
    output.close()
```
