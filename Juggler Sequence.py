class Solution:
    def jugglerSequence(self, n):
        res = [n]
        while n!=1:
            n = int(n**0.5) if not n%2 else int(n**1.5)
            res.append(n)
        return res
