def mergesort(arr):
    if len(arr)>1: 
        mid=len(arr)//2
        
        L=arr[:mid]
        R=arr[mid:]
        
        mergesort(L)
        
        mergesort(R)
        print(R)
        
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:  
                arr[k]=L[i]
                i+=1

            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

if __name__=="__main__":
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    print("Given array is\n",arr)
    mergesort(arr)
    print("Sorted array is:\n",arr)