# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self,tree,val,node) :
        if (tree) :
            if (tree.val == val) and (tree != node):
                return True
            elif (tree.val > val) :
                if (self.search(tree.left,val,node) == True) :
                    return True
            elif (tree.val < val) :
                if (self.search(tree.right,val,node) == True) :
                    return True
    def preorder(self,node,k,tree) :
        if (node) :
            # curr = node
            if (self.search(tree,k-node.val,node) == True) :
                return True
            if (self.preorder(node.left,k,tree) == True) :
                return True
            if (self.preorder(node.right,k,tree) == True) :
                return True
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if (self.preorder(root,k,root) == True) :
            return True
        else :
            return False