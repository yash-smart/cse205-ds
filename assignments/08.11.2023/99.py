# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal2(self,node,val,dxn) :
        if (node) :
            if (dxn == 1) :
                if (node.val <= val) :
                    return False
                if (self.traversal2(node.left,val,1) == False) :
                    return False
                if (self.traversal2(node.right,val,1) == False) :
                    return False
            else :
                if (node.val >= val) :
                    return False
                if (self.traversal2(node.left,val,0) == False) :
                    return False
                if (self.traversal2(node.right,val,0) == False) :
                    return False
    def preorder2(self,node) :
        if (node) :
            if (self.traversal2(node.left,node.val,0) == False) :
                return False
            if (self.traversal2(node.right,node.val,1) == False) :
                return False
            if (self.preorder2(node.left) == False) :
                return False
            if (self.preorder2(node.right) == False) :
                return False

    def check(self, root: Optional[TreeNode]) -> bool:
        if (self.preorder2(root) == False) :
            return False
        else :
            return True
    def preorder(self,node,val,dxn) :
        if (node) :
            if (dxn == 1) :
                if (node.val <= val) :
                    return node
            if (dxn == 0) :
                if (node.val >= val) :
                    return node
            x = self.preorder(node.left,val,dxn)
            if (x) :
                return x
            y = self.preorder(node.right,val,dxn)
            if (y) :
                return y
    def traversal(self,node) :
        if (node) :
            x = self.preorder(node.left,node.val,0)
            if (x) :
                temp = node.val
                node.val = x.val
                x.val = temp
                return True
            y = self.preorder(node.right,node.val,1)
            if (y) :
                temp = node.val
                node.val = y.val
                y.val = temp
                return True
            if(self.traversal(node.left)) :
                return True
            if (self.traversal(node.right)) :
                return True
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (self.check(root) == False) :
            self.traversal(root)