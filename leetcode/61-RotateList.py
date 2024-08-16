from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)



def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head


        count = 0
        temp = head
        while temp.next != None:
            count += 1
            temp = temp.next
        count += 1
        
        currCount = count - (k%count)
        print(currCount)

        tempN = head
        for _ in range(currCount-1):
            tempN = tempN.next
            
            
        print(temp.val, tempN.val)
        print()

        temp.next = head
        result = tempN.next
        tempN.next = None

        return result

printLinkedList(Solution().rotateRight(l1, 4))
