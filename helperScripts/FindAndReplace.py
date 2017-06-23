from AppendBR import fo
from AddSpace import bar

#Run Append BR instead of running me.

file = raw_input("Enter input file name:")
f = open(file+".txt",'r')
filedata = f.read()
f.close()

filedata = filedata.replace('&','&amp;')
filedata = filedata.replace('"','&quot;')
filedata = filedata.replace('<','&lt;')
filedata = filedata.replace('>','&gt;')

f = open(file+".txt",'w')
f.write(filedata)
f.close()

f = open(file+"_output.txt",'w')
f.write(filedata)
f.close()

fo(file)
bar(file)
