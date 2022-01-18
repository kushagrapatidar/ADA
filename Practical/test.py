import datetime, os
os.system('cls')

a = datetime.datetime.now()
from linear_search import linearsearch
n=int(input('Enter the number: '))
linearsearch(n)
b = datetime.datetime.now()
print(b-a)

# a = datetime.datetime.now()
# from insertion_sort import insertionsort
# arr=input('Enter the array elements with spaces: ').split()
# arr=list(map(int, arr))
# insertionsort(arr)
# print(arr)
# b = datetime.datetime.now()
# print(b-a)