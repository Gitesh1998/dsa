from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(3)
# list1.next.next.next = ListNode(4)
# list1.next.next.next.next = ListNode(5)
# list1.next.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next.next = ListNode(9)


def printLinkedList(head):
    while head != None:
        print(head.val)
        head = head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        start = 1
        stack = []

        prev = None
        current = head

        while current != None:
            if start == left:
                temp = current
                while start <= right:
                    stack.append(temp)
                    temp = temp.next
                    start += 1
                if left == 1:
                    result = stack[-1]
                    te = stack.pop()
                    while len(stack) > 0:
                        te.next = stack.pop()
                        te = te.next
                    te.next = temp
                    return result

                while len(stack) > 0:
                    prev.next = stack.pop()
                    prev = prev.next

                prev.next = temp
                return head

            start += 1
            prev = current
            current = current.next

        return True


printLinkedList(Solution().reverseBetween(list1, 1, 1))
