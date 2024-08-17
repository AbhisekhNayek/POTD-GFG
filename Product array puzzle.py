#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        n = len(nums)
        if n==1:
            return [1]
        ans = [0]*n
        zeros = 0
        prod = 1
        for i in nums:
            if i>0:
                prod *= i
            else:
                zeros += 1
        if zeros>1:
            return ans
        elif zeros==1:
            ans[nums.index(0)] = prod
            return ans
        # no zeros
        for j in range(n):
            ans[j] = prod//nums[j]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends
