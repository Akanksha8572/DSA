# Remove N-th node from end of singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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
# brute force approch, tc = O(N), sc = O(1)
    # def remove_nth_from_end(self, n):
    #     # Step 1: Find length
    #     length = 0
    #     temp = self.head
    #     while temp:
    #         length += 1
    #         temp = temp.next

    #     # Step 2: If removing head
    #     if n == length:
    #         self.head = self.head.next
    #         return self.head

    #     # Step 3: Traverse to node before the one to delete
    #     position_to_stop = length - n - 1  # stop one before
    #     temp = self.head
    #     for _ in range(position_to_stop):
    #         temp = temp.next

    #     # Step 4: Remove node
    #     if temp.next:
    #         temp.next = temp.next.next

    #     return self.head
# optimal approch, tc = O(N), sc = O(1)
    def remove_nth_from_end(self, n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return self.head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


# Example usage:
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original list:")
ll.print_list()

ll.remove_nth_from_end(2)
print("List after removing 2nd node from end:")
ll.print_list()
