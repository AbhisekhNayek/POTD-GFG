import bisect
class Solution:
    def countElements(self, a, b, n, query, q):
        
        b.sort()
            
        return [bisect.bisect_right(b, a[q1]) for q1 in query]
