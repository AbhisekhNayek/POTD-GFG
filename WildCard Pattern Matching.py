# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        # Code here
        
        from functools import lru_cache
        
        m, n = len(pattern), len(string)
        
        @lru_cache(None)
        def match(i, j):
            nonlocal m, n
            if i == m and j == n:
                return True
            if i == m and j < n:
                return False
            if j == n:
                if pattern[i] == '*':
                    return match(i+1, j)
                return False
            if pattern[i] == '*':
                return match(i+1, j) or match(i, j+1)
            if pattern[i] == '?' or pattern[i] == string[j]:
                return match(i+1, j+1)
            return False
        return match(0, 0)



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends
