import sys

def matrixchainorder(p, i, j):
    if i == j:
        return 0
    _min = sys.maxsize
    for k in range(i, j):
        val = (matrixchainorder(p, i, k)+matrixchainorder(p, k + 1, j)+p[i-1]*p[k]*p[j])
        if val < _min:
            _min = val
    return _min

arr = [5, 4, 6, 2, 7]
n = len(arr)
print("Minimum number of multiplications is ",matrixchainorder(arr, 1, n-1))