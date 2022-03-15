file_size=list(map(int,input().split()))
# print(min(file_size))
M=0
while len(file_size)>1:
    num1=min(file_size)
    num1_idx=file_size.index(num1)
    del file_size[num1_idx]
    num2=min(file_size)
    num2_idx=file_size.index(num2)
    del file_size[num2_idx]
    sum=num1+num2
    M+=sum
    file_size.insert(0, sum)
print(M)