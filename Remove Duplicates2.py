#User function Template for python3
class Solution:
	def removeDups(self, str):
		ans = []
        for ele in str:
            if ele in ans:
                continue
            else:
                ans.append(ele)
        my_string = "".join(ans)
        
        return my_string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends
