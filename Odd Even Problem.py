from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        res=0
        d=Counter(s)
    
        for i in d:
            if d[i]%2==ord(i)%2:
                res+=1
        if res%2==0:
            return "EVEN"
        return "ODD"
