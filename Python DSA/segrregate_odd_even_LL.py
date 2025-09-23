# Segrregate odd and even nodes in LL
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

    # # Brute-force approach to rearrange nodes in odd-even position order
    # def odd_even(self):
    #     if self.head is None or self.head.next is None:
    #         return self.head

    #     odd_values = []
    #     even_values = []

    #     temp = self.head
    #     is_odd = True

    #     # Traverse and collect odd and even position values
    #     while temp:
    #         if is_odd:
    #             odd_values.append(temp.val)
    #         else:
    #             even_values.append(temp.val)
    #         is_odd = not is_odd
    #         temp = temp.next

    #     # Combine them
    #     values = odd_values + even_values

    #     # Assign values back to nodes
    #     temp = self.head
    #     index = 0
    #     while temp and index < len(values):
    #         temp.val = values[index]
    #         index += 1
    #         temp = temp.next

    #     return self.head
    # TC = O(N), SC =  O(N)
    # Optimal way
    def odd_even(self):
        if self.head is None or self.head.next is None:
            return self.head

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return self.head
sll = SinglyLinkedList()
for i in range(1, 6):  # Creates list: 1 -> 2 -> 3 -> 4 -> 5
    sll.append(i)

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

print("Original List:")
print_list(sll.head)

sll.odd_even()

print("After Odd-Even Rearrangement:")
print_list(sll.head)
# TC = O(N/2)~O(n) and SC = O(1)