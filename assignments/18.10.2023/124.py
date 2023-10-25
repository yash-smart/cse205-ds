# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    self.ans = max(self.ans, node.val)
                    return node.val if node.val > 0 else 0
                ls = dfs(node.left)
                rs = dfs(node.right)
                self.ans = max(self.ans, ls + node.val + rs, ls + node.val, rs + node.val, node.val)
                if ls > rs and ls > 0:
                    return ls + node.val
                elif ls <= rs and rs > 0:
                    return rs + node.val
                else:
                    return node.val if node.val > 0 else 0
            else:
                return 0
        dfs(root)

        return self.ans