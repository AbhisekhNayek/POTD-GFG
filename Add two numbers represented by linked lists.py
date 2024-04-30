''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        summ1=""
        summ2=""
        while num1:
            summ1=summ1+str(num1.data)
            num1=num1.next
        while num2:
            summ2=summ2+str(num2.data)
            num2=num2.next
        temp=int(summ1)+int(summ2)
        summ1=str(temp)
        head=None
        for i in range(len(summ1)-1,-1,-1):
            temp=Node(int(summ1[i]))
            temp.next=head
            head=temp
        return head
