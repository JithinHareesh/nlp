import re
import urllib.request
from bs4 import BeautifulSoup
with urllib.request.urlopen("https://en.wikipedia.org/wiki/Cancer") as url:
    s = url.read()
soup=BeautifulSoup(s,"html.parser")
text=soup.get_text()
match = re.compile(r"symptoms\s*([^.]+|\S+)")
newstring=match.findall(text) 
with open("tag.txt", "w") as fo:
  print("Name of the file: ", fo.name)
  fo.seek(0, 2)
  str = fo.write(",".join(newstring))
with open("tag.txt", "r") as f1:
  f1.seek(0,0)
  for index in range(7):
    str = f1.readline()
fo.close()
