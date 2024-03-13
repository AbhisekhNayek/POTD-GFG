class Solution:
    def matrixDiagonally(self,mat):
        # code here
        r,c=len(mat),len(mat[0])
        ans=[]
        down=False
        for j in range(c):
            i=0  #upper half triangle
            arr =[]
            
            while j-i>=0 and i<r and j-i<c:
                arr.append(mat[i][j-i])
                i+=1
            if down==False:
                arr.reverse()
            ans.extend(arr)
            down=True if down==False else False
            

        for i in range(1,r):
            j=c-1  #lower half triangle
            arr = []
            while (i+(c-1-j))<r and j>=0 :
                arr.append(mat[i+(c-1-j)][j])
                j-=1
            if down==False:
                arr.reverse()
            ans.extend(arr)
            down=True if down==False else False
         
        return ans
