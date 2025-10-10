# Remove duplicates from a sorted DLL
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
# create a doubly linked list
class doublyLinked_list:
    def __init__(self):
        self.head = None
    #  insert at head
    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # append at last
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
    # traversal
    def traversal(self):
        if not self.head:
            print("DLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end= " ")
                curr = curr.next
    # remove duplicated from the sorted DLL
    def remove_duplicates(self):
        if self.head is None:
            return

        curr = self.head.next
        while curr:
            if curr.prev and curr.val == curr.prev.val:
                prev_node = curr.prev
                next_node = curr.next

                # Link prev and next to skip duplicate
                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node

                # move to next node (no change to head)
                curr = next_node
            else:
                curr = curr.next
dll = doublyLinked_list()
dll.append(10)
dll.append(20)
dll.append(20)
dll.append(30)
dll.append(30)
dll.append(30)
dll.append(40)

print("Original list:")
dll.traversal()

dll.remove_duplicates()
print("After removing duplicates:")
dll.traversal()
