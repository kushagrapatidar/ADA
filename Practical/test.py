from os import system
from time import sleep
system('cls')
from linear_search import linearsearch
n=int(input('Enter the number: '))
linearsearch(n)

sleep(4)
system('cls')
# from insertion_sort import insertionsort
# arr=input('Enter the array elements with spaces: ').split()
# arr=list(map(int, arr))
# insertionsort(arr)
# print(arr)