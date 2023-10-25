# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,p,q) :
        if (p) and (q) :
            if (p.val != q.val) :
                return False
            if (self.preorder(p.left,q.left) == False) :
                return False
            if (self.preorder(p.right,q.right) ==False) :
                return False
        elif (p) and (not q) :
            return False
        elif (not p) and (q) :
            return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (self.preorder(p,q) == False) :
            return False
        else :
            return True