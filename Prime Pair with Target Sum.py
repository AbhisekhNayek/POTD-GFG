from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        if n < 2:
            return [-1, -1]
    
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        for a in range(2, n):
            if is_prime[a] and is_prime[n - a]:
                return [a, n - a]
        
        return [-1, -1]
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends
