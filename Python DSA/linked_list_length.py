# Find the length of loop in linked list 
# brute approch
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Define SinglyLinkedList class with corrected `cycle()` method
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
    # def loop_length(self):
    #     temp = self.head
    #     travel = 0
    #     my_dict = dict()
    #     while temp is not None:
    #         if temp in my_dict:
    #             return travel - my_dict[temp]
    #         my_dict[temp] = travel
    #         travel += 1
    #         temp = temp.next 
    #     return 0
    # TC = O(N), SC =(N)
# OPTIMAL way
    def loop_length(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next 
                    count += 1
                return count
        return 0
    # TC = O(N), SC =O(1)

# Create a list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle starts again at node with value 3)
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

# Create loop manually
loop_start = sll.head.next.next  # Node with value 3
end = sll.head
while end.next is not None:
    end = end.next
end.next = loop_start  # Create the cycle

print(sll.loop_length()) 
# TC = O(N), SC =(N)





