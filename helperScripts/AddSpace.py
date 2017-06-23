import re
import FindAndReplace

def bar(file):
    with open(file+".txt",'r') as f:
        content = f.readlines()
    with open(file+".txt",'w') as f:
        for line in content:
            f.write("" + line)
			

#f = raw_input("Name an input file: ")
#fo(f)
