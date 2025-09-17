# Reverse the linked list 
# brute fource approch 
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
# Define the Reversal(brute)
    # def reverse(self):
    #     temp = self.head
    #     stack = [ ]
    #     while temp is not None:
    #         stack.append(temp.val)
    #         temp = temp.next
    #     temp = self.head
    #     while temp is not None:
    #         e = stack.pop()
    #         temp.val = e
    #         temp = temp.next
# TC = O(2N) = O(N), SC = O(N)
# Define the Reversal(optimal)
    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev 
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
        # TC = (N), SC =O(1)
sll = SinglyLinkedList()
# Append elements
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
print("Original list:")
sll.print_list()

sll.reverse()

print("Reversed list:")
sll.print_list()

