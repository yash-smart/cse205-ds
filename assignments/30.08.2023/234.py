# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1 = ''
        d = head
        while (d):
            str1 += str(d.val)
            d = d.next
        if (str1 == str1[::-1]) :
            return True
        else :
            return False