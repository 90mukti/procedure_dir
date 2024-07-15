import re # regular expressin 're' it is used for serching phrase ina asentence declared by python in built 'import' used for to import any function from library

text = "i am mukti a devops engineer"

Pattern = r"devops" # 'r' when is used meeans the searched phrease or pattern format is 'r"<phrase>"' =<pattern> pattern name can be anything like here  tom = r"devops"
Search = re.search(Pattern,text) # 're.search'(the serched object, inside the big expression) means  
if Search:
    print("Pattern is sucess:",Search.group()) # object stored in 'search.group()'.
else:
    print("Pattern doesn't found")