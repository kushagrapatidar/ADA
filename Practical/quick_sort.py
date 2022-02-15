from random import randint

def pivot(start,end,arr):
    piv=randint(start,end)
    arr[start],arr[piv]=arr[piv],arr[start]
    return partition(start,end,arr)

def partition(start,end,arr):
    
    piv=arr[start]
    i=start
    j=end
    
    while i<j:
        
        while arr[i]<=piv and i<end: i+=1
        
        while arr[j]>piv and j>start: j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[j],arr[start]=arr[start],arr[j]
    
    return j

def quicksort(start,end,arr):
    if start<end:
        
        piv_index=pivot(start,end,arr)
        
        
        quicksort(start,piv_index-1,arr)
        quicksort(piv_index+1,end,arr)
        
    return arr

if __name__=="__main__":
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    print("Given array is\n",arr)
    arr=quicksort(0,len(arr)-1,arr).copy()
    print("Sorted array is:\n",arr)