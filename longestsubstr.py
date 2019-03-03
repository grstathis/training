__author__ = 'stathis'

string = "aabbfffeeewertuuiirrrrrrr"
longest_substr = ""

for i in range(len(string)):
    lsubstr = ""
    maxset = set()
    for s in string[i:len(string)]:
        maxset.add(s)
        if(len(maxset)) > 2:
            break
        else:
            lsubstr=lsubstr+s
    if len(lsubstr) > len(longest_substr):
        longest_substr = lsubstr

print("longest_substr of string",string,"is",longest_substr)
