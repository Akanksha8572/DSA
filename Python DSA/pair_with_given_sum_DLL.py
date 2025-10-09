# Find the pairs with given sum in DLL
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
    # brute fource approch
    # def pairs(self,target):
    #     temp1 = self.head
    #     result = [ ]
    #     while temp1 is not None:
    #         temp2 = temp1.next
    #         while temp2 is not None:
    #             if temp1.val + temp2.val == target:
    #                 result.append([temp1.val,temp2.val])
    #             temp2 = temp2.next
    #         temp1 = temp1.next
    #     return result
    # TC = O(N(N+1)/2) and SC = O(1)
    # Better approch
    # def pairs(self,target):
    #     my_set = set()
    #     temp = self.head
    #     result = [ ]
    #     while temp is not None:
    #         remaining = target- temp.val
    #         if remaining in my_set:
    #             result.append([remaining,temp.val])
    #         my_set.add(temp.val)
    #         temp = temp.next
    #     return result
    # TC = O(N) and SC = O(N)
    # OPTIMAL WAY
    def pairs(self,target):
        result = [ ]
        left = self.head
        right = self.head
        while right.next is not None:
            right = right.next
        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val
            if total == target:
                result.append({left.val,right.val})
                left = left.next
                right = right.prev
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return result
    # TC = O(N)+ O(N = O(2N) = O(N)
    # SC = O(1)

dll = doublyLinked_list()
# Append elements
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)

print("Doubly Linked List:")
dll.traversal()
print()
print("Pairs with sum = 50:")
print(dll.pairs(50))
