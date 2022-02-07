def binarysearch_rec(arr,s,e,x):
    if x>arr[-1] or x<arr[0]:
        return 0
    i=s+(e-s)//2
    if arr[i]==x:
        return i+1
    elif arr[i]<x:
        s=i+1
        return binarysearch_rec(arr,s,e,x)
    else:
        e=i-1
        return binarysearch_rec(arr,s,e,x)