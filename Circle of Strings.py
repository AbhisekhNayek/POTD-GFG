#User function Template for python3
from collections import defaultdict
class Solution:
    def isCircle(self, arr):
        # code here
        
        def char_to_ind(c):
            return ord(c)-ord('a')
            
        
        in_=[0]*26
        out_=[0]*26
        
        g = defaultdict(list)
        
        for s in arr:
            f = char_to_ind(s[0])
            l = char_to_ind(s[-1])
            in_[f]+=1
            out_[l]+=1
            g[f].append(l)
            
        if in_!=out_:
            return 0
        
        visited = set()
        st=[char_to_ind(arr[0][0])]
        
        while st:
            
            c = st.pop()
            
            if c not in visited:
               visited.add(c)
               for i in g[c]:
                   st.append(i)
        
        if len(visited)!=len(g):
            return 0
        
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends
