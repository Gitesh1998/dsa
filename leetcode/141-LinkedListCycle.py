from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next


def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next

# printLinkedList(head)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list = set()
        while head!=None:
            if head in list:
                return True
            list.add(head)
            head = head.next
        return True
print(Solution().hasCycle(head))