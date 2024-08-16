from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(2)
# l1.next.next.next.next = ListNode(3)
# l1.next.next.next.next.next = ListNode(4)
# l1.next.next.next.next.next.next = ListNode(5)



def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


def findDuplicate(head):
    if head == None:
        return {
            "length": 0,
            "current": head 
        }
    elif head.next == None:
        return {
            "length": 1,
            "current": head
        }
    elif head.val == head.next.val:
        while head.next != None and head.val == head.next.val:
            head = head.next
        
        return {
            "length": 2,
            "current": head
        }
    return {
        "length": 1,
        "current": head
    }

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        temp = newHead
        while head != None:
            result = findDuplicate(head)
            if result["length"] == 1:
                newHead.next = head
                newHead = newHead.next
            if result["length"] == 2:
                head = result["current"]
            head = head.next
        newHead.next = None
        return temp.next 
    
printLinkedList(Solution().deleteDuplicates(l1))
