from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(9)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(8)
l1.next.next.next.next.next = ListNode(1)



def mergeSortedList(l1, l2):
    head = ListNode(0)
    curr = head
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        curr = curr.next

    while l1:
        curr.next = ListNode(l1.val)
        curr = curr.next
        l1 = l1.next
    while l2:
        curr.next = ListNode(l2.val)
        curr = curr.next
        l2 = l2.next
    return head.next


def findMid(l1):
    if not l1:
        return None
    if not l1.next:
        return l1

    current = l1
    while l1.next and l1.next.next:
        current = current.next
        l1 = l1.next.next

    return current


def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


def divide(l1):
    if not l1:
        return None
    if not l1.next:
        return l1
    mid = findMid(l1)
    temp = mid.next
    mid.next = None
    temp1 = divide(l1)
    temp2 = divide(temp)

    temp = mergeSortedList(temp1, temp2)
    return temp


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = divide(head)
        return temp


printLinkedList(Solution().sortList(l1))
