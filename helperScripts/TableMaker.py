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
count = 0
for line in lines:
    if count%2 == 1:
        f.write('  <tr align="center" bgcolor="#C8C8C8"> \n')
    else:
        f.write('  <tr align="center"> \n')
    tds = re.split(r'\t+', line)
    for td in tds:
        if count == 0:
            f.write("    <th>"+td+"</th> \n")
        else:
            f.write("    <td>"+td+"</td> \n")
    f.write("  </tr> \n")
    f.write("\n")
    count+=1
f.write("</table> \n")
f.close()



