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
