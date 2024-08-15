from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(7)




def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        for _ in range(n):
            current = current.next
        if current == None:
            return head.next
        temp = head
        while current.next != None:
            current = current.next
            temp = temp.next
        if n == 1:
            temp.next = None
            return head
        temp.next = temp.next.next
        return head


    
printLinkedList(Solution().removeNthFromEnd(l1, 5))
