import nltk
import csv


File = open('D:\Review2\\tag.txt')
lines = File.read()
sentences = nltk.sent_tokenize(lines) 
nouns = []

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)
print(nouns)            
##a=str(nouns)
##with open("fnoun.txt", "w") as fo:
##  print("Name of the file: ", fo.name)
##  fo.seek(0, 2)
##  str = fo.write(a)
##with open("fnoun.txt", "r") as f1:
##  f1.seek(0,0)
##  for index in range(7):
##    str = f1.readline()
##fo.close()
##p=open('Book1.csv')
##ids=list(csv.reader(p,delimiter=","))
##for i in range(0,len(nouns)):
##   for j in ids:
##       if(nouns[i]==j[0]):
##            print(nouns[i],":",j[1])
##            


