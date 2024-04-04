class Solution:
    #Function to find sum of all possible substrings of the given string.
     def sumSubstrings(self,s):
        ans=sm1=sm0=0
        for ix,ve in enumerate(s):
            sm1=(sm0*10+int(ve)*(ix+1))%(10**9+7)
            ans=(ans+sm0)%(10**9+7)
            sm0=sm1
        return (ans+sm0)%(10**9+7)
