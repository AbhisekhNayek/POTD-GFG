#User function Template for python3
class Solution:
    def bracketNumbers(self, S):
        # code here
        count=0
        ans=[]
        st=[]
        
        for x in S:
            if(x=='('):
                count+=1
                ans.append(count)
                st.append(count)
            elif(x==')'):
                ans.append(st[-1])
                st.pop()
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends
