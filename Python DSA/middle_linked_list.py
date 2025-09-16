class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Define the SinglyLinkedList class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # def find_middle(self):
    #     n = 0
    #     temp = self.head

    #     # First pass: Count the nodes
    #     while temp is not None:
    #         n += 1
    #         temp = temp.next

    #     # Second pass: Go to the n//2-th node
    #     temp = self.head
    #     for i in range(n // 2):
    #         temp = temp.next

    #     if temp:
    #         print("Middle node value:", temp.val)
    #     else:
    #         print("List is empty.")
    def find_middle(self):
        slow = self.head 
        fast = self.head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        print(slow.val)
sll = SinglyLinkedList()

# Append elements
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
# Find and print the middle node
sll.find_middle()  
# TC = O(N+N/2) and SC = O(1)
# Optimal way
    
