from typing import List

class Solution:

    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
            left,right,ans=0,n-1,0
            while left<=right:
                mid=left+(right-left)//2
                if abs(ans-k)>abs(k-arr[mid]):ans=arr[mid]
                if abs(ans-k)==abs(k-arr[mid]):ans=max(ans,arr[mid])
                if arr[mid]>k:right=mid-1
                else: left=mid+1
            return ans
