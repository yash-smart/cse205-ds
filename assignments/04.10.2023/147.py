# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionsort(self,list) :
        for i in range(len(list)) :
            key = list[i]
            j = i-1
            while (j>=0) and (key < list[j]) :
                list[j+1] = list[j]
                j-=1
            list[j+1] = key
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        lst1 = []
        while (h) :
            lst1.append(h.val)
            h = h.next
        self.insertionsort(lst1)
        return_list = ListNode(lst1[0])
        node = return_list
        for j in range(1,len(lst1)) :
            node.next = ListNode(lst1[j])
            node = node.next
        return return_list
        