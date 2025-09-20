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

    def cycle(self):
        temp = self.head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                print(temp)
                return temp
            my_set.add(temp)
            temp = temp.next
        print(None)
        return None
    def cycle2(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return False

print("Test 1: No cycle")
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
result = ll.cycle2()
print(result)  # Expected: False

print("\nTest 2: With cycle")
ll2 = SinglyLinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)

# Create cycle: last node points back to second node
first = ll2.head
second = first.next
third = second.next
third.next = second  # Creates the cycle

result = ll2.cycle2()
print(result.val if result else result)
