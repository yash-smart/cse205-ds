# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,node,res) :
        if (node) :
            res.append(node.val)
            self.traverse(node.left,res)
            self.traverse(node.right,res)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root,res)
        return res