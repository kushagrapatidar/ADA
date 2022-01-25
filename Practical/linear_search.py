import os
os.system('cls')

#Que-01
def linearsearch(n):
    from random import randint
    arr=[randint(0,x+1) for x in range(1,101)]
    print(f'{arr}\n')# Length: {len(arr)} \n')
    if n in arr:
        idx=arr.index(n)+1
        print(f"{n} found in the list: Index- {idx}")
    else:
        print(f'{n} not found in the list')

#Que-02
def linearsearch2(n):
    from random import randint
    arr=[randint(0,x+1) for x in range(1,101)]
    print(f'{arr}\n')# Length: {len(arr)} \n')
    idx=list()
    for _ in range(len(arr)):
        if arr[_]==n:
            idx.append(_+1)
    
    return(idx)

#Que-03
def find_freq(n):
    idx_lst=linearsearch2(n)
    if idx_lst==None:
        return 0
    else:
        return len(idx_lst)

if __name__== '__main__':
    n1=int(input('Enter the number: '))
    linearsearch(n1)
    
    print('\n'*2)
    n2=int(input('Enter the number: '))
    idx_lst=linearsearch2(n2)
    if idx_lst==None:
        print(f'{n2} not found in the list')
    else:
        print(f"{n2} found in the list:\nIndex- {idx_lst}")
    
    print('\n'*2)
    n3=int(input('Enter the number: '))
    frequency=find_freq(n3)
    print(f'Frequency of occurrence of {n3} in the list: {frequency}')