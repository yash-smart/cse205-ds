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
    def isempty(self) :
        return self.lst == []
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = stack()
        node = root
        inorder = []
        while True :
            if (node) :
                st.push(node)
                node = node.left
            else :
                if (st.isempty() == True) :
                    break
                node = st.pop()
                inorder.append(node.val)
                node = node.right
        return inorder