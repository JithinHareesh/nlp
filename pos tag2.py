from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
 
train_text=state_union.raw("D:\Review2\\tag.txt")
tokens = word_tokenize(train_text)
tokens_pos = pos_tag(tokens)  
print(tokens_pos)
