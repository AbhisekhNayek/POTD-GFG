class Solution:
    
    def findUnion(self,arr1,arr2,n,m):
        # code here 
        r = set(arr1)
        x = set(arr2)
        return sorted(r.union(x))
