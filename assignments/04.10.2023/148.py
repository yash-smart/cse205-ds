# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergesort(self,arr) :
        if (len(arr)>1) :
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergesort(L)
            self.mergesort(R)
            i=j=k=0
            while (i<len(L)) and (j<len(R)) :
                if (L[i]<=R[j]) :
                    arr[k] = L[i]
                    i+=1
                else :
                    arr[k] = R[j]
                    j+=1
                k+=1
            while (i<len(L)) :
                arr[k] = L[i]
                i+=1
                k+=1
            while (j<len(R)) :
                arr[k] = R[j]
                j+=1
                k+=1
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        h = head
        while(h) :
            lst1.append(h.val)
            h = h.next
        self.mergesort(lst1)
        if (lst1) :
            new = ListNode(lst1[0])
            node = new
            for i in range(1,len(lst1)) :
                node.next = ListNode(lst1[i])
                node = node.next
            return new