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




import copy
A = [[1,2,3],[6,3,2],[1,2,1],[1,0,9]]
B = copy.deepcopy(A)
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == 0:
            print(i,j)
            for r in range(len(A)):
                B[r][j] = 0
            for c in range(len(A[0])):
                B[i][c] = 0
print(B)