from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        arr.sort()  

        left = 0
        right = 1  

        while left < n and right < n:  
            if left != right and abs(arr[left] - arr[right]) == x:
                return 1
            elif abs(arr[left] - arr[right]) < x:  
                right += 1
            else: 
                left += 1

            if left == right:  
                right += 1

        return -1 
