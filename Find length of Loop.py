#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    
    def countNodesInLoop(self, head):
            #Your code here
            slow = fast = head  # Initialize two pointers, slow and fast, at the head
            count=1
            while fast and fast.next:
                # Move slow one node forward
                slow = slow.next
                # Move fast two nodes forward
                fast = fast.next.next
                # If slow and fast meet, a loop exists
                if slow == fast:
                    # Traverse the loop to find its length
                    while slow.next != fast:
                        slow = slow.next
                        count += 1
    
                    # Return the length of the loop
                    return count
    
            # If no loop is found, return 0
            else:
              return 0


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


def loop_here(head, pos):
    if pos == 0:
        return

    walk = head
    for _ in range(1, pos):
        walk = walk.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = walk


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        loop_here(head, k)
        ob = Solution()
        res = ob.countNodesInLoop(head)
        print(res)
        index += 2

# } Driver Code Ends
