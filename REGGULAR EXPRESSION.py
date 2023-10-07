import re
text="Regular expressions are a powerfull tool for text processing They can be used for pattern matching,tokenizaion,and more"
word_pattern=r'\w+'
words=re.findall(word_pattern,text)
print(words)
