from typing import Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
        new_tail = new_head = cur = head
        prev = None
        while cur.next != tail:
            new_head = cur.next
            cur.next = prev
            prev = cur
            cur = new_head

        cur.next = prev
        new_head = cur
        new_tail.next = None

        return [new_head, new_tail]


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #Look ahead k
        cur = head 
        reversed_head = reversed_tail = None

        while True:
            count = 0
            new_head: ListNode = cur    
            print(f'new head: {new_head.val}')

            while cur != None and count < k:
                count += 1
                cur = cur.next

            if count == k:
                [new_head, new_tail] = self.reverseList(new_head, cur)

                if reversed_head is None:
                    reversed_head = new_head
                    reversed_tail = new_tail
                else:
                    reversed_tail.next = new_head
                    reversed_tail = new_tail
            else:
                if reversed_head is None:
                    return new_head
                else:
                    reversed_tail.next = new_head
                    return reversed_head

    def printList(self, head: ListNode):
        result = []

        while head != None:
            result.append(head.val)
            head = head.next
        
        print(result)


sol = Solution()

head = cur = ListNode(1)

for i in range(2, 8):
    cur.next = ListNode(i)
    cur = cur.next

#print(sol.reverseList(head, None)[0].val)
sol.printList(sol.reverseKGroup(head, 2))


            


