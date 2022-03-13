P=[]
M=[]
N=int(input('Number of Matrices: '))
for i in range(N):
    P+=list(map(int,input(f'Enter the number of rows and columns of {i+1} matrix with a space: ').split()))
    mat=[]
    print(f'Enter the elements of {i+1} matrix')
    for j in range(P[-2]):
        row=list(map(int,input(f'Enter the elements of {j+1} row with spaces: ').split()))
        mat.append(row)
    M.append(mat)
for i in range(N):
    [print(row) for row in M[i]]
    print('\n')