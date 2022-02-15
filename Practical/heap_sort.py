def max_heapsort(arr):
    n=len(arr)-1
    
    for j in range(2):
        i=n
        
        while i>0:
            
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
            
            if arr[i-1]>arr[(i-1)//2]:
                arr[i-1],arr[(i-1)//2]=arr[(i-1)//2],arr[i-1]
            i-=2
            
    return arr

def min_heapsort(arr):
    n=len(arr)-1
    
    for j in range(2):
        i=n
        
        while i>0:
            
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
            
            if arr[i-1]<arr[(i-1)//2]:
                arr[i-1],arr[(i-1)//2]=arr[(i-1)//2],arr[i-1]
            i-=2
            
    return arr

def call_min_heapsort(arr):
    i=len(arr)
    
    while i>0:
        arr[:i]=min_heapsort(arr[:i])
        i-=1
    return arr

def call_max_heapsort(arr):
    i=len(arr)
    
    while i>0:
        arr[:i]=max_heapsort(arr[:i])
        i-=1
    return list(reversed(arr))

if __name__=="__main__":
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    print('Initial Array:\n',arr,"\n")
    arr_max=call_max_heapsort(arr.copy())
    print('Sorted Array by Max Heap:\n',arr_max)
    arr_min=call_min_heapsort(arr.copy())
    print('Sorted Array by Min Heap:\n',arr_min)

# Rough Work
    # Corresponding parent and first child node
    # 2:1:0
    # 4:3:1
    # 6:5:2
    # 8:7:3
    # i-1:((i-1)/2) #General Indexing 