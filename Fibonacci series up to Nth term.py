class Solution:
    def series(self, n):
        # Code here
        a = 0
        b =1 
        fibo = []
        fibo.append(a)
        fibo.append(b)
        for i in range(0,n-1):
            c = fibo[i]+fibo[i+1]
            fibo.append(c%(10**9+7))
            
        return fibo    
