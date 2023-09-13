# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self) :
        self.lst = []
    def len_linked_list(self,List) :
        curr = List
        len = 0
        if (List) :
            len = 1
            while (curr.next!=None) :
                len+=1
                curr = curr.next
        return len
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = self.len_linked_list(head)
        if (len==n) :
            head = head.next
            return head
        if(len>1) :
            c=1
            d = head
            while (c!=len-n) :
                d = d.next
                c+=1
            t = d.next
            d.next = d.next.next
            t.next = None
            return head
        elif (len == 1) and (n==1) :
            return None
        elif (len==1) and (n!=1) :
            return head
        
        else :
            return head