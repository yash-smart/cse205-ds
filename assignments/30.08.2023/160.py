# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self,head) :
        d = head
        count = 0
        while d :
            count += 1
            d = d.next
        return count
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = self.length(headA)
        len2 = self.length(headB)
        diff = len1-len2 if len1>len2 else len2-len1
        if (len1 != len2) :
            d = headA if len1>len2 else headB
            d2 = headB if (len1>len2) else headA
            for i in range(diff) :
                d = d.next
            while (d) and (d2) :
                if (d == d2) :
                    return d
                else :
                    d = d.next
                    d2 = d2.next
        else :
            d = headA
            d2 = headB
            while (d) and (d2) :
                if(d == d2) :
                    return d
                else :
                    d = d.next
                    d2 = d2.next