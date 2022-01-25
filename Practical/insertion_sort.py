#Que-04
def insertionsort_asc(arr):
    l=len(arr)
    for i in range(1,l):
        store=arr[i]
        j=i-1
        while j>=0 and store<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=store

#Que-05
def insertionsort_desc(arr):
    l=len(arr)
    for i in range(1,l):
        store=arr[i]
        j=i-1
        while j>=0 and store>arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=store

if __name__== '__main__':
    arr=input('Enter the array elements with spaces: ').split()
    arr=list(map(int, arr))
    arr1=arr
    print(f'Array initially: {arr}\n')
    insertionsort_asc(arr)
    print(f'The array in ascending order: {arr}\n')
    insertionsort_desc(arr1)
    print(f'The array in descending order: {arr1}')