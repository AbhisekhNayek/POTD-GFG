#User function Template for python3

from typing import List

class Solution:
     def findOrder(self, alien: List[str], N: int, K: int) -> str:
        # Your implementation here
        from collections import deque, defaultdict
        g = defaultdict(set)
        for i in range(1, len(alien)):
            for frm, to in zip(alien[i-1], alien[i]):
                if frm != to:
                    g[frm].add(to)
                    break
        
        seen = set()
        orders = deque()
        def dfs(n):
            seen.add(n)
            for nbr in g[n]:
                if nbr not in seen:
                    dfs(nbr)
            orders.appendleft(n)
        for k in list(g.keys()):
            if k not in seen:
                dfs(k)
        return orders
        # Your implementation here




#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends
