memo=[]
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n==1:
        memo[n]=0
        return memo[n]
    if n==2 or n==3:
        memo[n]=1
        return memo[n]
    memo[n]=fibonacci(n-1)+fibonacci(n-2)
    return memo[n]

n=int(input())
memo=[None]*(n+1)
print(fibonacci(n))