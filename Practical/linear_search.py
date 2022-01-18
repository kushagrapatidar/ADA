def linearsearch(n, idx=list(), arr=None):
    from random import randint
    if arr==None:
        arr=[randint(0,x+1) for x in range(1,101)]
        print(f'{arr}\n Length: {len(arr)} \n')
    
    for _ in arr:
        if _==n:
            idx.append(arr.index(_)+1)
            idx=linearsearch(n, idx, arr[idx[-1]:len(arr)])
    
    return(idx)
