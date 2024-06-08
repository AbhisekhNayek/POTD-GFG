class Solution:    
    def findExtra(self, n, a, b):
        left, right = 0, n-1
        while left<right:
            mid = left+(right-left)//2
            if a[mid]==b[mid]:
                left = mid+1
            else:
                right = mid
        return left
