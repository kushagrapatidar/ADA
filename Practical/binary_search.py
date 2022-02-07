#Que-06

def binarysearch_iter(arr,n):
    if n>arr[-1] or n<arr[0]:
        return 0
    s=0
    e=len(arr)-1
    while True:
        i=s+(e-s)//2
        if arr[i]==n:
            return i+1
        elif arr[i]<n:
            s=i+1
        else:
            e=i-1

def binarysearch_rec(arr,s,e,n):
    if n>arr[-1] or n<arr[0]:
        return 0
    i=s+(e-s)//2
    if arr[i]==n:
        return i+1
    elif arr[i]<n:
        s=i+1
        return binarysearch_rec(arr,s,e,n)
    else:
        e=i-1
        return binarysearch_rec(arr,s,e,n)
    
if __name__=='__main__':
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    n=int(input('Enter the element: '))
    idx_iter=binarysearch_iter(arr,n)
    idx_rec=binarysearch_rec(arr,0, len(arr)-1,n)
    print('\n')
    if idx_iter==0:
        print(f'Element {n} not found in array by iterative binary search')
    else:
        print(f'Element {n} found by iterative binary search at index: {idx_iter}')

    if idx_rec==0:
        print(f'Element {n} not found in array by recursive binary search')
    else:
        print(f'Element {n} found by recursive binary search at index: {idx_rec}')