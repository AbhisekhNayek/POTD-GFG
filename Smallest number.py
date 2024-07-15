#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        ans = ""
        rem = s

        for i in range(1, d + 1):
            if i == 1:
                sum_remaining = (d - 1) * 9
                if sum_remaining + 9 < s:
                    return "-1"
                dig = max(1, s - sum_remaining)
                s -= dig
                ans += str(dig)
                continue
            
            dig = s - (d - i) * 9
            if dig <= 0:
                ans += "0"
            else:
                ans += str(dig)
                s -= dig

        return ans
        


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends
