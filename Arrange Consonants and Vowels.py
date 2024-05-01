class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
       #len=0
        temp=head
        vowels=['a','e','i','o','u']
        v=Node(-1)
        vp=v
        c=Node(-1)
        vc=c
        while(temp!=None):
            if(temp.data  in vowels):
                vp.next=Node(temp.data)
                vp=vp.next
            else:
                vc.next=Node(temp.data)
                vc=vc.next
            temp=temp.next
        vp.next=c.next
        return v.next
