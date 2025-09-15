# Singly Linked list creation, append, traversal, deletion
# Creation
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# Append to Singly linked list
class SinglyLinkedList:
    def __init__(self)-> None:
        self.head = None
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
# TC = O(N) and SC = O(1) 
# traversal 
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end= " ")
                curr = curr.next
## TC = O(N) and SC = O(1)
# Insert at specific position 
    def inser_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next == self.head
            self.head == new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next 
                count += 1
            prev_node.next = new_node
            new_node.next = current
# TC = O(N) and SC = O(1)
# Delete 
    def delete(self,val):
        temp = self.head
        if temp.val == val:
            self.head = temp.next
            del temp
            return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                    found = True
                    break
                prev = temp
                temp = temp.next 
            if found == True:
                prev.next = temp.next
                return
            else:
                print("Node not fount")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.inser_at(100,2)
sll.delete(20)
sll.traversal()




