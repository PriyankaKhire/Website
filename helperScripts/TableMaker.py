import re

#Run me dont run anything else
#Make sure that the table has tabs instead of spaces

file = raw_input("Enter input file name:")
f = open(file+".txt",'r')
filedata = f.read()
f.close()

#Find and replace
filedata = filedata.replace('&','&amp;')
filedata = filedata.replace('"','&quot;')
filedata = filedata.replace('<','&lt;')
filedata = filedata.replace('>','&gt;')



#Table maker
f = open(file+"_table.txt",'w')
f.write('<table align="center" cellpadding="10" style="margin: 0 auto; border-collapse: collapse;"> \n')
lines = filedata.split("\n")
for line in lines:
    f.write('  <tr align="center"> \n')
    tds = re.split(r'\t+', line)
    for td in tds:
        f.write("    <td>"+td+"</td> \n")
    f.write("  </tr> \n")
    f.write("\n")
f.write("</table> \n")
f.close()



