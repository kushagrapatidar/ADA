def insertionsort_asc(arr):
    l=len(arr)
    print(arr)
    for i in range(1,l):
        store=arr[i]
        j=i-1
        while j>=0 and store<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=store

def insertionsort_desc(arr):
    l=len(arr)
    print(arr)
    for i in range(1,l):
        store=arr[i]
        j=i-1
        while j>=0 and store<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=store