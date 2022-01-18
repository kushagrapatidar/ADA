def linearsearch(n):
    from random import randint
    arr=[randint(0,x+1) for x in range(1,101)]
    print(f'{arr}\n Length: {len(arr)} \n')
    if n in arr:
        idx=arr.index(n)+1
        print(f"{n} found in the list: Index- {idx}")
    else:
        print(f'{n} not found in the list')
        
def linearsearch2(n):
    from random import randint
    arr=[randint(0,x+1) for x in range(1,101)]
    print(f'{arr}\n Length: {len(arr)} \n')
    idx=list()
    for _ in range(len(arr)):
        if arr[_]==n:
            idx.append(_)
    
    return(idx)