S1="ABCDEFGHIJ"
S2="BDGHCEJ"
n=len(S1)
m=len(S2)

LCS=[]

for i in range(m+1):
    lst=[]
    for j in range(n+1):
        lst.append(0)
    LCS.append(lst)

for i in range(1,m+1):
    for j in range(1,n+1):
        if S2[i-1]==S1[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+1
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])

i=m
j=n
Soln=""
while j>=0 and i>0:
    if LCS[i][j]==LCS[i-1][j]:
        i-=1
    else:
        Soln=S2[i-1]+Soln
        i-=1
        j-=1
print("String 1: "+S1)
print("String 2: "+S2)
print("Lowest Common Subsequence: "+Soln)