import datetime, os
from Practical.insertion_sort import insertionsort_asc, insertionsort_desc
os.system('cls')

# Linear Search -1
# from linear_search import linearsearch
# n=int(input('Enter the number: '))
# linearsearch(n)

# #Linear Search - 2
# from linear_search import linearsearch2
# n=int(input('Enter the number: '))
# idx_lst=linearsearch2(n)
# if idx_lst==None:
#     print(f'{n} not found in the list')
# else:
#     print(f"{n} found in the list:\nIndex- {idx_lst}")

# #Linear Search - 3
# from linear_search import find_freq
# n3=int(input('Enter the number: '))
# frequency=find_freq(n3)
# print(f'Frequency of occurrence of {n3} in the list: {frequency}')

#Insertion Sort
from insertion_sort import insertionsort_desc
arr=input('Enter the array elements with spaces: ').split()
arr=list(map(int, arr))
insertionsort_desc(arr)
print(arr,'\n'*2)
