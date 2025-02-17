# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        new_head = old_tail.next
        old_tail.next = None
        
        for _ in range(n - k % n - 1):
            head = head.next
        
        new_head = head
        current = head
        while current.next:
            current = current.next
        current.next = head
        
        return new_head