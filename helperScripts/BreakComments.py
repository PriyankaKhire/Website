import re

def insertNewlines(text, lineLength):
    if(len(text) <= lineLength):
        return text
    else:
        return re.sub("(.{"+ str(lineLength) +"})", "\\1\n//", text, 0, re.DOTALL)


file_name = raw_input("Input File name: ")

with open(file_name+".txt") as f:
    content = f.readlines()

with open(file_name+".txt", "w") as f:
    for line in content:
        if(line.startswith( '//' )):
            f.write(insertNewlines(line, 30))
        else:
            f.write(line)
