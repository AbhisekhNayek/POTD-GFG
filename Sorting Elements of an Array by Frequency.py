#User function Template for python3
 
class Solution:
    def sortByFreq(self,arr):
        temp = {}
        for i in arr: temp[i] = temp.get(i, 0)+1
        temp2 = [[i, temp[i]] for i in temp]
        temp2.sort(key = lambda i:(-i[1], i[0]))
        temp3 = []
        for x, y in temp2: temp3.extend([x]*y)
        return temp3



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends
