from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
# list1.next.next.next = ListNode(9)
# list1.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next.next = ListNode(9)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
# list2.next.next.next = ListNode(9)

list1 = None
list2 = ListNode(1)


def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list2 == None:
            return list1
        if list1 == None:
            return list2
        head = ListNode(0)
        current = head
        while (list1 != None) and (list2 != None):
            
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next

        while list1 != None:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next
            
            
        while list2 != None:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next    
                        
        return head.next



printLinkedList(Solution().mergeTwoLists(list1, list2))
