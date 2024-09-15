# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = cur = None
        carry_over = 0
        while (l1 or l2):
            sum = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry_over
            if (sum > 9):
                carry_over = int(sum / 10)
                sum %= 10
            else:
                carry_over = 0
            
            if (cur is None):
                result = ListNode(sum)
                cur = result
            else:
                cur.next = ListNode(sum)
                cur = cur.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if (carry_over > 0):
            cur.next = ListNode(carry_over)
            cur = cur.next

        cur.next = None
        return result