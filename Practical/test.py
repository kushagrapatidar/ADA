import datetime, os
os.system('cls')

# Linear Search -1
# a = datetime.datetime.now()
# from linear_search import linearsearch
# n=int(input('Enter the number: '))
# linearsearch(n)
# b = datetime.datetime.now()
# print(b-a)

# Insertion Sort
# a = datetime.datetime.now()
# from insertion_sort import insertionsort
# arr=input('Enter the array elements with spaces: ').split()
# arr=list(map(int, arr))
# insertionsort(arr)
# print(arr)
# b = datetime.datetime.now()
# print(b-a)

#Linear Search -2
from linear_search import linearsearch2, find_freq
n=int(input('Enter the number: '))
idx_lst=linearsearch2(n)
if idx_lst==None:
    print(f'{n} not found in the list')
else:
    print(f"{n} found in the list:\nIndex- {idx_lst}")