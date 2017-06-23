#Run me dont run anything else

file = raw_input("Enter input file name:")
f = open(file+".txt",'r')
filedata = f.read()
f.close()

#Find and replace
filedata = filedata.replace('&','&amp;')
filedata = filedata.replace('"','&quot;')
filedata = filedata.replace('<','&lt;')
filedata = filedata.replace('>','&gt;')

#UL List Maker
ul_choice = raw_input("Do you want ul ? y or n\n")
if(ul_choice == "y"):
    ultype = raw_input("Enter UL type: disc  circle  square  none\n")
    ul = open(file+"_unorderedList.txt",'w')
    ul.write('<ul style="list-style-type:'+ultype+'"> \n')
    lines = filedata.split("\n")
    for line in lines:
        ul.write('  <li>'+line+'</li> \n')
    ul.write('</ul> \n')
    ul.close()

#OL List Maker
ol_choice = raw_input("Do you want ol ? y or n\n")
if(ol_choice == "y"):
    oltype = raw_input("Enter OL type: 1  A  a  I  i\n")
    ol = open(file+"_orderedList.txt",'w')
    ol.write('<ol type="'+oltype+'"> \n')
    lines = filedata.split("\n")
    for line in lines:
        ol.write('  <li>'+line+'</li> \n')
    ol.write('</ol> \n')
    ol.close()
