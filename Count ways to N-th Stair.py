class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    
    def countWays(self, n):

        return n // 2 + 1
