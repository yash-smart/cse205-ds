# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 1
        curr = head
        while (curr.next != None) :
            len += 1
            curr = curr.next
        middle = None
        if (len%2 == 0) :
            middle = (len+1)//2+1
        else :
            middle = (len+1)//2
        curr = head
        for i in range(middle-1) :
            curr = curr.next
        return curr