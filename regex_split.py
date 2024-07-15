import re 
text = "banana,orange,apple,sapota,papaya"
pattern = r","
split = re.split(pattern,text)
print("split rsult:", split)