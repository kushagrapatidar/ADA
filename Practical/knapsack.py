def knapsack(W, w, v, n):
    if n == 0 or W == 0:
        return 0
    if (w[n-1] > W):
        return knapsack(W, w, v, n-1)
    else:
        return max(
            v[n-1] + knapsack(W-w[n-1], w, v, n-1),knapsack(W, w, v, n-1))
v = [60, 100, 120]
w = [10, 20, 30]
W = 40
n = len(v)
print(v)
print(knapsack(W, w, v, n))