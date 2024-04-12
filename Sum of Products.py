class Solution:
    def pairAndSum(self, n, arr):
        #code here
        r = 0
        for i in range(32):
            cnt = 0
            for e in arr:
                if (1<<i)&e != 0:
                    cnt += 1
            r += 2**i*cnt*(cnt-1)//2
        return r
