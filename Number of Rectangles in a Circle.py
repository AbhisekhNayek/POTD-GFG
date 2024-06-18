#User function template for Python

import math

class Solution:

    def rectanglesInCircle(self, r):
        count = 0
        diameter_squared = (2 * r) ** 2

        # Iterate through all possible lengths from 1 to 2*r
        for length in range(1, 2 * r + 1):
            # Calculate the maximum width that can fit for a given length
            max_width = int(math.sqrt(diameter_squared - length ** 2))
            
            # Add the number of valid widths for the current length
            count += max_width
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends
