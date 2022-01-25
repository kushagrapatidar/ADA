def binarysearch_iter(arr,x):
    if x>arr[-1] or x<arr[0]:
        return 0
    s=0
    e=len(arr)-1
    while True:
        i=s+(e-s)//2
        if arr[i]==x:
            return i+1
        elif arr[i]<x:
            s=i+1
        else:
            e=i-1

def binarysearch_rec(arr,s,e,x):
    if x>arr[-1] or x<arr[0]:
        return 0
    i=s+(e-s)//2
    if arr[i]==x:
        return i+1
    elif arr[i]<x:
        s=i+1
        return binarysearch_rec(arr,s,e,x)+1
    else:
        e=i-1
        return binarysearch_rec(arr,s,e,x)+1
    
if __name__=='__main__':
    arr=list(map(int, input('Enter the array elements with spaces: ').split()))
    x=int(input('Enter the element: '))
    idx_iter=binarysearch_iter(arr,x)
    idx_rec=binarysearch_rec(arr,0, len(arr)-1,x)
    print('\n')
    if idx_iter==0:
        print(f'Element {x} not found in array by iterative binary search')
    else:
        print(f'Element {x} found by iterative binary search at index: {idx_iter}')

    if idx_rec==0:
        print(f'Element {x} not found in array by recursive binary search')
    else:
        print(f'Element {x} found by recursive binary search at index: {idx_rec}')