class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        carry = 0
        root = head

        while l1 or l2:
            s1 = l1.val if l1 else 0
            s2 = l2.val if l2 else 0
            s = s1 + s2 + carry
            carry = s // 10

            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)
        
        return root.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
result = s.addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next
