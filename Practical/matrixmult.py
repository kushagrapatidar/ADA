P=[]
Matrices=[]
maxint=int(1e9+7)
N=int(input('Number of Matrices: '))
for i in range(N):
    P+=list(map(int,input(f'Enter the number of rows and columns of {i+1} matrix with a space: ').split()))
    mat=[]
    # print(f'Enter the elements of {i+1} matrix')
    # for j in range(P[-2]):
    #     row=list(map(int,input(f'Enter the elements of {j+1} row with spaces: ').split()))
    #     mat.append(row)
    # Matrices.append(mat)
    if len(P)>2 and P[-2]==P[-3]:
        del P[-3]
# for i in range(N):
#     [print(row) for row in Matrices[i]]
#     print('\n')
n=len(P)
if n!=N+1:
    print('The Matrices are not Multiplicable')
else:
    M=[]
    for i in range(N):
        lst=[]
        for j in range(N):
            lst.append(0)
        M.append(lst)
    print(P)
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            M[i][j] = maxint
            for k in range(i, j):
                num = M[i][k] + M[k + 1][j] + P[i-1]*P[k]*P[j]
                if num < M[i][j]:
                    M[i][j] = num
    [print(row) for row in M]