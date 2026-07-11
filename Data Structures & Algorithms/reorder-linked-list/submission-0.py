# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        prev = None
        cur = head2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        tail1 = dummy.next
        tail2 = prev

        while tail2:
            temp1 = tail1.next
            temp2 = tail2.next

            tail1.next = tail2
            tail2.next = temp1

            tail1 = temp1
            tail2 = temp2
         
    
