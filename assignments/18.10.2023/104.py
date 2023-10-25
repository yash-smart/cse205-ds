# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class queue:
    def __init__(self) :
        self.lst = []
    def enqueue(self,element) :
        self.lst.append(element)
    def dequeue(self) :
        return self.lst.pop(0)
    def isempty(self) :
        return len(self.lst) == 0
    def __len__(self) :
        return len(self.lst)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root) :
            q = queue()
            q.enqueue(root)
            lst = []
            while (not q.isempty()) :
                n = len(q.lst)
                for i in range(n) :
                    element = q.dequeue()
                    if (i == 0) :
                        lst.append([element.val])
                    else :
                        lst[-1].append(element.val)
                    if (element.left) :
                        q.enqueue(element.left)
                    if (element.right) :
                        q.enqueue(element.right)
            return len(lst)
        else :
            return 0