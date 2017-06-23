#Usage: copy code that has c,c++ questions and solutions
#Example:
#Q: Write fibonacci series
#Ans: The following is the program for fibo
# def foo(n):
#   if n == 1: return 1
#   if n==0: return 0
#   return foo(n-1)+foo(n-2)
#for above question answer put the question in (())
#answer in {{}}
#code in [[]]
#and this script will transform the above into html code 
import re

#Global variables
curlyCount = 0
squareCount = 0

#Find and replace all &"<> with html characters
def find_and_replace(input_file):
    f = open(input_file+".txt",'r')
    filedata = f.read()
    f.close()
    filedata = filedata.replace('&','&amp;')
    filedata = filedata.replace('"','&quot;')
    filedata = filedata.replace('<','&lt;')
    filedata = filedata.replace('>','&gt;')
    f = open(input_file+".txt",'w')
    f.write(filedata)
    f.close()
    

#Finds the parts of answer and captures them
def select_curly_braces(content, input_file, count):
    global curlyCount
    text = re.search('\{'+str(count)+'\{[\s\S]*\}'+str(count)+'\}', content)    
    if text is not None:
        text = text.group(0)
        rewrite_input_file(text, content, input_file)
        text = text[3:-3]
        if text.startswith("{"):
            text = text[1:]
        if text.endswith("}"):
            text = text[:-1]
        text = text.replace("\n","</br> \n")
        return "<p>"+text+"</p>\n</br>"
    else:
        return "-1"

#Finds all parts of the question and captures them
def select_circle_braces(content, input_file):
    text = re.search('\(\([\s\S]*\)\)', content)    
    if text is not None:
        text = text.group(0)
        rewrite_input_file(text, content, input_file)
        text = text[2:-2]
        text = text.replace("\n","</br> \n")
        return "<h4>"+text+"</h4>\n</br></br>\n\n"
    else:
        return "-1"

#Finds all parts of the code and captures them
def select_square_braces(content, input_file, count):
    text = re.search('\['+str(count)+'\[[\s\S]*\]'+str(count)+'\]', content)
    if text is not None:
        text = text.group(0)
        rewrite_input_file(text, content, input_file)
        text = text[3:-3]
        if text.startswith("["):
            text = text[1:]
        if text.endswith("]"):
            text = text[:-1]
        #text = text.replace("\n","</br> \n")
        return '\n<pre class="prettyprint">\n'+text+"</pre>\n</br>"
    else:
        return "-1"

#Remove initial empty lines
def remove_initial_empty_lines(input_file):
    with open(input_file+".txt", 'r') as f:
        contents = f.readlines()
    first_non_empty_line = False
    new_content = []
    for line in contents:
        if(first_non_empty_line):
            new_content.append(line)
            continue
        if line.split():
            first_non_empty_line = True
            new_content.append(line)
    with open(input_file+".txt",'w') as f:
        for line in new_content:
                f.write(line)
    
#replace the content with text
def rewrite_input_file(text, content, input_file):
    with open(input_file+".txt", 'w') as f:
        f.write(content.replace(text, ""))
    remove_initial_empty_lines(input_file)

#Writes in output file
def write_in_file(text):
    with open("output.txt",'a') as f:
        f.write(text)
        
def clear_output_file():
    with open("output.txt",'w') as f:
        f.write("")
        
def extract_text_circular(input_file):
    with open(input_file+".txt", 'r') as f:
        content = f.read()
    if(len(content) > 0):
        #Select circular brackets
        selected_text = select_circle_braces(content, input_file)
        if(selected_text != "-1"):
            #Write in file
            write_in_file(selected_text)        

def extract_text_curly(input_file, count):
    with open(input_file+".txt", 'r') as f:
        content = f.read()
    if(len(content) > 0):
        #Select {} brackets
        selected_text = select_curly_braces(content, input_file, count)
        if(selected_text != "-1"):
            write_in_file(selected_text)

def extract_text_square(input_file, count):
    with open(input_file+".txt", 'r') as f:
        content = f.read()
    if(len(content) > 0):
        #Select [] brackets
        selected_text = select_square_braces(content, input_file, count)
        if(selected_text != "-1"):
            write_in_file(selected_text)

def make_unique_delimiters(input_file):
    global curlyCount, squareCount
    with open(input_file+".txt", 'r') as f:
        contents = f.readlines()
    new_content = []
    for line in contents:
        if "{{" in line:
            new_content.append(line.replace("{{", "{"+str(curlyCount)+"{"))
            continue
        if "}}" in line:
            new_content.append(line.replace("}}", "}"+str(curlyCount)+"} \n"))
            curlyCount+=1
            continue
        if "[[" in line:
            new_content.append(line.replace("[[", "["+str(squareCount)+"["))
            continue
        if "]]" in line:
            new_content.append(line.replace("]]", "]"+str(squareCount)+"] \n"))
            squareCount+=1
            continue
        new_content.append(line)
    #Write the file line by line
    with open(input_file+".txt",'w') as f:
        for line in new_content:
            f.write(line)
        
            

def extract_text(input_file, squareBracketsCount, curlyBracketsCount):
    global curlyCount, squareCount
    if(squareBracketsCount == squareCount and curlyBracketsCount==curlyCount):
        return
    with open(input_file+".txt", 'r') as f:
        content = f.read()
    if(len(content) > 0):
        #Find out what the line starts with
        if content.startswith("(("):
            extract_text_circular(input_file)
        if content.startswith("{"):
            extract_text_curly(input_file, curlyBracketsCount)
            curlyBracketsCount+=1
        if content.startswith("["):
            extract_text_square(input_file, squareBracketsCount)
            squareBracketsCount+=1
        #Recurse
        extract_text(input_file, squareBracketsCount, curlyBracketsCount)   



#Main Program
input_file = "input"
#Now i convert {{ to {0{ and }} to }0} making them unique.
make_unique_delimiters(input_file)
#Clears the output file by deleting contents in it
clear_output_file()
#Find and replace all &"<> with html characters in the input file
find_and_replace(input_file)
extract_text(input_file, 0,0)
print "Total number of Solution snipets : "+str(curlyCount)
print "Total number of code snipets : "+str(squareCount) 

#Next write code to make table and list

#copy past the questuion from google doc of programing practice into input file
#put the main question in (())
#put the answer in {{}}
#put the code in [[]]
#put the table/list in ??

