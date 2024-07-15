import re
text = "a brown fox jumped over a red dog and played with him"
pattern = r"brown"
#replace = "red"
newtext = re.sub(pattern,"red",text) #or  newtext = re.sub(pattern,replace,text)
print("modified text:", newtext)