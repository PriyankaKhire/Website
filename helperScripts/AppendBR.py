import re
import FindAndReplace

#Run Add Space instead of running me.

def fo(file):
    with open(file+".txt",'r') as f:
        content = f.readlines()
    with open(file+".txt",'w') as f:
        for line in content:
            f.write(line + "</br>")

def foo(file):
    with open(file+".txt",'r') as inputf, open(file+"_output.txt",'w') as outputf:
        for line in inputf:
            outputf.write(line + "</br>")
    
    
