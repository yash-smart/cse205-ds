# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        result = None
        temp = None
        carry = 0
        while (x) or (y) :
            s = 0
            if(x) :
                s += x.val
                x = x.next
            if (y) :
                s+= y.val
                y= y.next
            s += carry
            carry = 0
            if(result) :
                temp.next = ListNode(s%10)
                carry += s//10
                temp = temp.next
            else :
                result = ListNode(s%10)
                carry += s//10
                temp = result
        if(carry != 0) :
            temp.next = ListNode(carry)   
            
        return result