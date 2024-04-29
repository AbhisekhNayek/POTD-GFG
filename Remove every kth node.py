class Solution:
    def deleteK(self, head, k):
        if k==1:
            return None
        
        s=head
        cnt=0
        
        while s is not None:
            cnt+=1
            if cnt==k-1:
                cnt=0
                if s.next:
                    s.next=s.next.next
                    
            s=s.next
        
        return head
