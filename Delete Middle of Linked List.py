#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    
    def deleteMid(self,head):
        if not head or not head.next:
            return head
        temp=head
        count=0
        
        while temp:
            count+=1
            temp=temp.next
        count=(count//2)+1
        temp=head
        
        while count>2:
            temp=temp.next
            count-=1
        temp.next=temp.next.next
        
        return head
