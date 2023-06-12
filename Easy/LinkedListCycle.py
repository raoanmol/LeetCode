# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checker = set()
        pointer = head

        while pointer != None:
            if pointer in checker:
                return True
            checker.add(pointer)
            pointer = pointer.next

        return False

# OR

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fPointer = head
        sPointer = head

        while (fPointer != None) and (fPointer.next != None):
            fPointer = fPointer.next.next
            sPointer = sPointer.next

            if fPointer == sPointer:
                return True

        return False
