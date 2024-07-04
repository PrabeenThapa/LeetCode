# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


class Solution():
    def __init__(self):
        self.head = None

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")

    def insertAtEnd(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return 
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = Solution()
        s = 0
        current_node = head

        while current_node:
            if current_node.val == 0 and s > 0:
                a.insertAtEnd(s)
                s = 0
            else:
                s += current_node.val
            current_node = current_node.next

        return a.head

# Example usage
a = Solution()
a.insertAtEnd(0)
a.insertAtEnd(3)
a.insertAtEnd(1)
a.insertAtEnd(0)
a.insertAtEnd(4)
a.insertAtEnd(5)
a.insertAtEnd(5)
a.insertAtEnd(0)
print("Original List:")
a.printLL()

b = Solution()
new_head = b.mergeNodes(a.head)
b.head = new_head
print("Merged List:")
b.printLL()
