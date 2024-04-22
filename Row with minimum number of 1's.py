class Solution:
    def minRow(self,n,m,a):
        #code here
        g = []
        for i in a:
            g.append(sum(i))
        p = min(g)
        r = []
        for j in range(0,len(g)):
            if p == g[j]:
                r.append(j+1)
        return r[0]
