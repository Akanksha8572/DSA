# find a cycle in the linked list , if cycle is there return true else return false
# brute approch
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
    # def cycle(self):
    #     temp = self.head
    #     my_set = set()
    #     while temp is not None:
    #         if temp in my_set:
    #             print(true)
    #         my_set.add(temp)
    #         temp = temp.next
    #     print(False)
    # TC = O(N),SC = O(N)
    # Optimal way
    def cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
      # TC = O(N),SC = O(1)
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
if sll.cycle():
    print("Cycle detected")
else:
    print("No cycle")