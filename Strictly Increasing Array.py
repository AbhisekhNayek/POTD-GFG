class Solution:
	def min_operations(self,nums):
        # Code here
        n = len(nums)
        LIS = [1] * n  # Initialize LIS array with 1 for all indices
    
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and (i - j) <= (nums[i] - nums[j]):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
    
        # Length of the LIS gives the minimum number of changes needed
        return n - max(LIS)
