class Solution:
    def firstElement (self, n):
        MOD = 10**9 + 7
        import numpy as np
        arr = np.array([[1, 1], [1, 0]], dtype=int)
        res = np.identity(2, dtype=int)
        while n:
            if n & 1:
                res = np.matmul(res, arr) % MOD
            arr = np.matmul(arr, arr) % MOD
            n >>= 1
        return res[1, 0]
