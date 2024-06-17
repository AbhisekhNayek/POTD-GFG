#User function Template for python3

class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        dx1 = q1[0] - p1[0]
        dx2 = q2[0] - p2[0]
        dy1 = q1[1] - p1[1]
        dy2 = q2[1] - p2[1]
        r0 = dy2 * (q2[0] - p1[0]) - dx2 * (q2[1] - p1[1])
        r1 = dy2 * (q2[0] - q1[0]) - dx2 * (q2[1] - q1[1])
        r2 = dy1 * (q1[0] - p2[0]) - dx1 * (q1[1] - p2[1])
        r3 = dy1 * (q1[0] - q2[0]) - dx1 * (q1[1] - q2[1])
        return 'true' if r0 * r1 <= 0 and r2 * r3 <= 0 else 'false'
   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)

# } Driver Code Ends
