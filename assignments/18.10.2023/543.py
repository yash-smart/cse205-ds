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
        return self.lst == []
class Solution:
    def height(self,tree) :
        if (tree) :
            q = queue()
            q.enqueue(tree)
            count = 0
            while not q.isempty() :
                n = len(q.lst)
                for i in range(n) :
                    e = q.dequeue()
                    if (e.left) :
                        q.enqueue(e.left)
                    if (e.right) :
                        q.enqueue(e.right)
                count += 1
            # count -= 1
            return count
        else :
            return 0
    def preorder(self,tree,lst) :
        if (tree) :
            lst.append(self.height(tree.right) + self.height(tree.left))
            self.preorder(tree.right,lst)
            self.preorder(tree.left,lst)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lst = []
        self.preorder(root,lst)
        return max(lst)