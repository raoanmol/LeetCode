# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curNode = node

        while node.next != None:
            node.val = node.next.val
            curNode = node
            node = node.next

        curNode.next = None
        
