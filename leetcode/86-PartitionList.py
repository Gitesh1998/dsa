from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(2)
# l1.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next = ListNode(2)
# l1.next.next.next.next.next.next = ListNode(9)



def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        newHead = ListNode(0)
        slow = newHead
        
        fastHead = ListNode(0)
        fast = fastHead
        while head != None:
            print(head.val)
            if head.val < x:
                print("here")
                slow.next = head
                slow = slow.next
            else:
                print("here1")

                fast.next = head
                fast = fast.next
                
                
            head = head.next
        
        slow.next = None
        fast.next = None
        
        slow.next = fastHead.next
        
        
        print()
        printLinkedList(newHead)
        print()
        printLinkedList(fastHead)
        print()
        return newHead.next  

printLinkedList(Solution().partition(l1, 6))
