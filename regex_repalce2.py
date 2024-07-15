import re
text = "one brown fox jumped over a white dog and palying with him"
pattern = [r"brown",r"white"]
replace = ["red", "black"]
for pattern, replace in zip(pattern, replace):
    newtext = re.sub(pattern,replace,text)
print("modified text:", newtext)