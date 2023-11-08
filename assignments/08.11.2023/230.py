# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,lst) :
        if (node) :
            self.inorder(node.left,lst)
            lst.append(node.val)
            self.inorder(node.right,lst)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        self.inorder(root,lst)
        return lst[k-1]