import re 
import urllib.request
from bs4 import BeautifulSoup
with urllib.request.urlopen("https://en.wikipedia.org/wiki/Cancer") as url:
    s = url.read()
soup=BeautifulSoup(s,"html.parser")
text=soup.get_text()
newstring=(text.encode('ascii', 'ignore')).decode("utf-8")

with open("foo.txt", "r+") as fo:
  print("Name of the file: ", fo.name)
  fo.seek(0, 2)
  line = fo.write( newstring )
  fo.seek(0,0)
  for index in range(7):
    line = fo.readline()
    print(index, line)
fo.close()
                          
err_occur = []                         
pattern = re.compile("symptoms",re.IGNORECASE) 
try:                              
 with open ('foo.txt', 'rt') as in_file:          
    for linenum, line in enumerate(in_file):        
      if pattern.search(line) != None:          
         err_occur.append((linenum, line.rstrip('\n'))) 
 for linenum, line in err_occur:              
    print("Line ", linenum, ": ", line, sep='')  
except FileNotFoundError:                   
        print("Input file not found.")     


    
    
