import re
import urllib.request
from bs4 import BeautifulSoup
with urllib.request.urlopen("https://en.wikipedia.org/wiki/Cancer") as url:
    s = url.read()
soup=BeautifulSoup(s,"html.parser")
text=soup.get_text()
lines = text.split('\n');
for line in lines:
   searchObj = re.search( r'(.*) symptoms of (.*?) .*', line,re.M|re.I)
   if(searchObj):
      print ("searchObj.group() : ",searchObj.group())
      print ("searchObj.group(2) : ", searchObj.group(2))
  
   
