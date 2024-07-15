import re
text = "MUKTI is a devops engineeer"
Pattern = r"MUKTI"
match = re.match(Pattern, text) # here like 're.search()' it is 're.match()' expression predefined by python
if match:
    print("match successful:",match.group()) # -same like 'search.group()' match .group() ' python predefind
else:
    print("no match found")