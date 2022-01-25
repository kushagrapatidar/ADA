import datetime, os
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

# #Insertion Sort
# from insertion_sort import insertionsort_desc,insertionsort_asc
# arr=input('Enter the array elements with spaces: ').split()
# arr=list(map(int, arr))
# arr1=arr
# print(f'Array initially: {arr}\n')
# insertionsort_asc(arr)
# print(f'The array in ascending order: {arr}\n')
# insertionsort_desc(arr1)
# print(f'The array in descending order: {arr1}')

# #Binary Search
# from binary_search import binarysearch_iter,binarysearch_rec
# arr=list(map(int, input('Enter the array elements with spaces: ').split()))
# x=int(input('Enter the element: '))
# idx_iter=binarysearch_iter(arr,x)
# idx_rec=binarysearch_rec(arr,0, len(arr)-1,x)
# print('\n')
# if idx_iter==0:
#     print(f'Element {x} not found in array by iterative binary search')
# else:
#     print(f'Element {x} found by iterative binary search at index: {idx_iter}')

# if idx_rec==0:
#     print(f'Element {x} not found in array by recursive binary search')
# else:
#     print(f'Element {x} found by recursive binary search at index: {idx_rec}')