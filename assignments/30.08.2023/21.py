# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        result = ListNode()
        d = result
        while True :
            if(h1) and (h2) :
                if (h1.val < h2.val) :
                    d.next = ListNode(h1.val)
                    h1 = h1.next
                    d = d.next
                else :
                    d.next = ListNode(h2.val)
                    h2 = h2.next
                    d=d.next
            elif(h1) :
                d.next = h1
                break
            else :
                d.next = h2
                break
        return result.next