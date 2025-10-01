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
    # insert at specific position
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < position-1:
                curr = curr.next
                count += 1
            if curr is None:
                print("Position out of bounds, appending at the end.")
                return
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
    # traversal
    def traversal(self):
        if not self.head:
            print("DLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end= " ")
                curr = curr.next
    # delete head
    def delete_head(self):
        if not self.head:
            print("DLL is empty")
            return
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
    # delete end
    def delete_end(self):
        if not self.head:
            print("DLL is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.prev.next = None
    # delete specific value
    def delete_value(self,val):
        if not self.head:
            print("DLL is empty")
            return
        curr = self.head
        while curr is not None:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:  # If head needs to be removed
                    self.head = curr.next
                return
            curr = curr.next
        print("Value not found in the list")
dll = doublyLinked_list()
dll.insert_at_head(10)
dll.append(20)
dll.append(30)
dll.insert_at(25,2)
dll.traversal()
print()
dll.delete_head()
dll.traversal()
print()
dll.delete_end()
dll.traversal()
print()
dll.delete_value(25)
dll.traversal()
print()
dll.delete_value(100)  # Value not found   
dll.traversal()
print()