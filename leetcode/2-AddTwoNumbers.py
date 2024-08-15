from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)


l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

l1 = ListNode(0)
l2 = ListNode(0)



def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


# printLinkedList(head)
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if l2 == None:
            return l1
        if l1 == None:
            return l2
        head = None
        current = None
        carry = 0
        while (l1 != None) and (l2 != None):
            if head == None:
                val = l1.val + l2.val + carry
                head = ListNode(val if val < 10 else val % 10)
                carry = 0 if val < 10 else val // 10
                current = head
                l1 = l1.next
                l2 = l2.next
                continue

            val = l1.val + l2.val + carry
            current.next = ListNode(val if val < 10 else val % 10)
            carry = 0 if val < 10 else val // 10
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            val = l1.val + carry
            current.next = ListNode(val if val < 10 else val % 10)
            carry = 0 if val < 10 else val // 10
            current = current.next
            l1 = l1.next

        while l2 != None:
            val = l2.val + carry
            current.next = ListNode(val if val < 10 else val % 10)
            carry = 0 if val < 10 else val // 10
            current = current.next
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)
        return head
    
    
printLinkedList(Solution().addTwoNumbers(l1, l2))
