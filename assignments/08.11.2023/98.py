# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,val,dxn) :
        if (node) :
            if (dxn == 1) :
                if (node.val <= val) :
                    return False
                if (self.traversal(node.left,val,1) == False) :
                    return False
                if (self.traversal(node.right,val,1) == False) :
                    return False
            else :
                if (node.val >= val) :
                    return False
                if (self.traversal(node.left,val,0) == False) :
                    return False
                if (self.traversal(node.right,val,0) == False) :
                    return False
    def preorder(self,node) :
        if (node) :
            if (self.traversal(node.left,node.val,0) == False) :
                return False
            if (self.traversal(node.right,node.val,1) == False) :
                return False
            if (self.preorder(node.left) == False) :
                return False
            if (self.preorder(node.right) == False) :
                return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if (self.preorder(root) == False) :
            return False
        else :
            return True