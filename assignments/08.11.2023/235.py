# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self,tree,val,lst1) :
        if (tree) :
            lst1.append(tree)
            if (tree.val > val) :
                self.search(tree.left,val,lst1)
            if (tree.val < val) :
                self.search(tree.right,val,lst1)
            if (tree.val == val) :
                return None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst1 = []
        self.search(root,p.val,lst1)
        lst2 = []
        self.search(root,q.val,lst2)
        lst3 = []
        for i in lst1 :
            if (i in lst2) :
                lst3.append(i)
        return lst3[-1]