S1="ABCDEFGHIJ"
S2="BDGHCEJ"

n=len(S1)
m=len(S2)

LCS=[[0]*(n+1)]*(m+1)

# [print(row) for row in LCS]
# print("\n")

for i in range(1,m+1):
    for j in range(1,n+1):
        if S2[i-1]==S1[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+1
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
[print(row) for row in LCS]

#Alternative Method
# if min(n,m)==m:
#     S1,S2=S2,S1
#     m,n=n,m

# lst=[-1]

# for i in range(n):
#     if S1[i] in S2:
#         indx=S2.index(S1[i])
#         if indx>lst[-1]:
#             lst.append(indx)
# lst=lst[1:]
# [print(S2[i],end="") for i in lst]