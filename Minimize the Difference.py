class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        pre,suf=[],[]
        mi,ma=arr[0],arr[0]
        for i in range(n-k):
            mi=min(mi,arr[i])
            ma=max(ma,arr[i])
            pre.append([mi,ma])
        
        mi,ma=arr[-1],arr[-1]
        for i in range(n-1,k-1,-1):
            mi=min(mi,arr[i])
            ma=max(ma,arr[i])
            suf.append([mi,ma])
        suf=suf[::-1]
        # print(pre,suf)
        i,j=-1,0
        ans=float("inf")
        while(j<=n-k):
            if(i==-1):
                dif=suf[j][1]-suf[j][0]
                ans=min(ans,dif)
            elif(j==n-k):
                dif=pre[i][1]-pre[i][0]
                ans=min(ans,dif)
            else:
                p,s=pre[i],suf[j]
                dif=max(p[1],s[1])-min(p[0],s[0])
                ans=min(ans,dif)
            i+=1
            j+=1
        return(ans)
