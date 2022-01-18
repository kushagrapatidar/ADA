from linear_search import linearsearch
n=int(input('Enter the number: '))
linearsearch(n)

from insertion_sort import insertionsort
arr=input('Enter the array elements with spaces: ').split()
arr=list(map(int, arr))
insertionsort(arr)
print(arr)