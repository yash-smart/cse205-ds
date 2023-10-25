# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class stack :
    def __init__(self) :
        self.lst = []
    def push(self,element) :
        self.lst.append(element)
    def pop(self) :
        return self.lst.pop()
    def top(self) :
        return self.lst[-1]
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        if (root == None) :
            return preorder
        stk = stack()
        stk.push(root)
        while stk.lst != [] :
            root = stk.pop()
            preorder.append(root.val)
            if (root.right != None) :
                stk.push(root.right)
            if (root.left != None) :
                stk.push(root.left)
        return preorder