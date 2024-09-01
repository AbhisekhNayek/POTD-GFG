#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        l1=len(arr1)
        l2=len(arr2)
        x1=x2=0
        mx=0
        sm1=sm2=0
        while x1<l1 or x2<l2:
            if x1<l1 and x2<l2:
                if arr1[x1]<arr2[x2]:
                    sm1+=arr1[x1]
                    x1+=1
                elif arr1[x1]>arr2[x2]:
                    sm2+=arr2[x2]
                    x2+=1
                else:
                    sm1+=arr1[x1]
                    sm2+=arr2[x2]
                    x1+=1
                    x2+=1
                    mx+=max(sm1,sm2)
                    sm1=sm2=0
            elif x1<l1:
                sm1+=arr1[x1]
                x1+=1
            else:
                sm2+=arr2[x2]
                x2+=1
        mx+=max(sm1,sm2)
        return mx



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends
