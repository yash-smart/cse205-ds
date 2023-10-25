# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class queue :
    def __init__(self) :
        self.lst = []
    def enqueue(self,element) :
        self.lst.append(element)
    def dequeue(self) :
        return self.lst.pop(0)
    def isempty(self) :
        return len(self.lst) == 0
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue()
        if (root) :
            q.enqueue(root)
        lst = []
        flag = True
        while not q.isempty() :
            temp = []
            n = len(q.lst)
            for i in range(n) :
                e = q.dequeue()
                temp.append(e.val)
                if (e.left) :
                    q.enqueue(e.left)
                if (e.right) :
                    q.enqueue(e.right)
            if (flag == True) :
                lst.append(temp)
                flag = False
            else :
                lst.append(temp[::-1])
                flag = True
        return lst