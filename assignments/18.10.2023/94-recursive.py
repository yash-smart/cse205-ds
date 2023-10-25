# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,node,res) :
        if (node == None) :
            return None
        self.traversal(node.left,res)
        res.append(node.val)
        self.traversal(node.right,res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root,res)
        return res