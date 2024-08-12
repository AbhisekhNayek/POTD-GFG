#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        def kth(arr1, arr2, i, j, m, n, k):
            if m > n:
                return kth(arr2, arr1, j, i, n, m, k)
            
            if m == 0:
                return arr2[j+k-1]
            
            if k == 1:
                return min(arr1[i], arr2[j])
                
            k1 = min(m, k//2)
            k2 = k-k1
            if arr1[i+k1-1] < arr2[j+k2-1]:
                return kth(arr1, arr2, i+k1, j, m-k1, n, k-k1)
            else:
                return kth(arr1, arr2, i, j+k2, m, n-k2, k-k2)
            
        n = len(arr1)+len(arr2)
        if n&1 != 0:
            return kth(arr1, arr2, 0, 0, len(arr1), len(arr2), n//2+1)
        else:
            e1 = kth(arr1, arr2, 0, 0, len(arr1), len(arr2), n//2)
            e2 = kth(arr1, arr2, 0, 0, len(arr1), len(arr2), n//2+1)
            return e1+e2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends
