class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
     def max_Books(self, n, k, arr):
        #code here
        from itertools import groupby
        gs = groupby(arr, key=lambda x: x <= k)
        sums = [sum(e) for f, e in gs if f]
        return max(sums) if sums else 0
