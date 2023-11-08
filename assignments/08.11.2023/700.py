# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,val) :
        if (node) :
            if (node.val == val) :
                return node
            elif (node.val > val) :
                return self.traversal(node.left,val)
            else :
                return self.traversal(node.right,val)
                
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traversal(root,val)