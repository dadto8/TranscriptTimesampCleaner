## **Transcript Timesamp Cleaner**

Python script to remove time / date stamps from vtt transcription files from Zoom.  easier to read when the timestamps are removed.

The python code has been converted to an exe with PyInstaller.

###  **Instructions**

place the exe file in a folder that's easy to find.  drop a VTT file in that directory.  

Example of raw transcrtion vtt file.
![Sample.vtt raw](/img/vtt-preclean.png)

Then double click vtt-cleanup.exe to run the cleaner, this will create a file in the same directory with -output.txt added to the filename.

Example of cleaned Transcription.
![sample.txt post process](/img/vtt-cleaned.png)

Code used in vtt-cleanup.py
```Python
import re
import os

# read file specified in command line
path = os.path.dirname(os.path.abspath(__file__))

# path = 'E:\\src\\Transcript Files\\test'
vtt_file = [f for f in os.listdir(path) if f.endswith(".vtt")]
# print(vtt_file[0])

# vtt file to strip date time stamps from
file = open(vtt_file[0], 'r')
input_vtt = file.read()

# regular expression to remove timestamps
regex = r"^[\d\s\n].*\n"
test_str = input_vtt
subst = ""

# output the results to a text file with the original filename plus output.txt
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
if result:
    output = open(vtt_file[0] + "-output.txt", "w+")
    output.write(result)
    output.close()
```
