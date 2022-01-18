def linearsearch(n):
    from random import randint,shuffle
    arr=[randint(0,x+1) for x in range(1,101)]
    print(f'{arr}\n{len(arr)}')
    
    idx=None
    for _ in arr:
        if _==n:
            idx=arr.index(_)+1
            print(f"{n} found: Index- {idx}")
            break
    if idx==None:
        print(f'{n} not Found')