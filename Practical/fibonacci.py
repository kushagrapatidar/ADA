memo=list()
def fibonacci(n):
    if n in memo:
        return n
    if n==1:
        memo.append(n)
        return 0
    if n==2 or n==3:
        memo.append(n)
        return 1
    memo.append(fibonacci(n-1)+fibonacci(n-2))
    return fibonacci(n-1)+fibonacci(n-2)

print(memo)