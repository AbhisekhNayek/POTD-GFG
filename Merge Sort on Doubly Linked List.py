class Solution():
    def sortDoubly(self,head):
        li=[]
        temp=head
        while temp:
            li.append(temp.data)
            temp=temp.next
        li.sort()
        l3=DoublyLinkedList()
        for i in li:
            l3.append(i)
        return l3.head
