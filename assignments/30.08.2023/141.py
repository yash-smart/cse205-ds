# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lst1 = []
        x = head
        while (x) :
            if (x not in lst1) :
                lst1.append(x)
                x = x.next
            else :
                return True
        return False