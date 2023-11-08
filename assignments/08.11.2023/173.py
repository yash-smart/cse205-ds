# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class my_func :
    def preorder(self,node,lst) :
        if (node) :
            self.preorder(node.left,lst)
            lst.append(node.val)
            self.preorder(node.right,lst)
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.pos = 0
        self.lst = []
        func = my_func()
        func.preorder(root,self.lst)

    def next(self) -> int:
        self.pos += 1
        return self.lst[self.pos-1]

    def hasNext(self) -> bool:
        return self.pos < len(self.lst) 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()