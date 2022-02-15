def heapsort(arr):
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

def call_heapsort(arr):
    i=len(arr)
    
    while i>0:
        arr[:i]=heapsort(arr[:i])
        i-=1

if __name__=="__main__":
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    print('Initial Array:\n',arr,"\n")
    call_heapsort(arr)

    print('Sorted Array:\n',arr)

# Rough Work
    # Corresponding parent and first child node
    # 2:1:0
    # 4:3:1
    # 6:5:2
    # 8:7:3
    # i-1:((i-1)/2) #General Indexing 