class Solution:
    def findMaxSum(self,n,m,arr):
        #code here
        res = -1
        
        for i in range(n - 2):
            for j in range(m - 2):
                temp = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
                res = max(res,temp)
        return res
