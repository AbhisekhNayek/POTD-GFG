#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        inc, dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = dec+1
            elif nums[i] < nums[i-1]:
                dec = inc+1
            # id nums[i] == nums[i-1], then inc and dec will be no changes.
        return max(dec, inc)

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends
