class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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

    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        points = []
        position = 1
        prev, curr = head, head.next

        while curr.next:
            next_node = curr.next
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                points.append(position)
            prev, curr = curr, next_node
            position += 1

        if len(points) < 2:
            return [-1, -1]

        min_distance = min(points[i] - points[i - 1] for i in range(1, len(points)))
        max_distance = points[-1] - points[0]

        return [min_distance, max_distance]

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

min_dist, max_dist = a.nodesBetweenCriticalPoints(a.head)
print("Min dist:", min_dist)
print("Max dist:", max_dist)
