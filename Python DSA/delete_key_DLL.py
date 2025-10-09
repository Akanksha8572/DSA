#  Delete all the occurrence of key in DLL 
# only optimal way
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
    def delete_key(self,key):
        if self.head is None and self.head.val == key:
            return None
        temp = self.head
        prev = None
        new_head = self.head
        while temp is not None:
            if temp.val == key:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            prev = temp
            temp = temp.next
            # TC = O(N) and SC = O(1)
dll = doublyLinked_list()
# Append elements
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(20)
dll.append(40)
dll.append(20)
dll.traversal()
print()
dll.delete_key(20)
dll.traversal()
print()