import re
class Solution:
    def ExtractNumber(self,sentence):
        a = list(map(int,filter(lambda x : '9' not in x,re.findall(r'\d+',sentence))))
        return -1 if len(a) == 0 else max(a)




#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends
