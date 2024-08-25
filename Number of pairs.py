#User function Template for python3

class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        a = len(arr)
        b = len(brr)
        x = [i ** (1 / i) for i in arr]
        y = [i ** (1 / i) for i in brr]
        x.sort()
        y.sort()
        c, j = 0, 0
        for i in range(a):
            while j < b and x[i] > y[j]:
                j += 1
            c += j
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends
