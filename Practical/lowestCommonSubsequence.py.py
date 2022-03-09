S1="ABCDEFGHIJ"
S2="BDGHCEJ"
n=len(S1)
m=len(S2)

# LCS=[[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
LCS=[]

for i in range(m+1):
    lst=[]
    for j in range(n+1):
        lst.append(0)
    LCS.append(lst)
# [print(row) for row in LCS]
# print("\n")

for i in range(1,m+1):
    for j in range(1,n+1):
        if S2[i-1]==S1[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+1
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
[print(row) for row in LCS]

