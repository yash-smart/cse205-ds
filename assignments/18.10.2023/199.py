# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class queue :
    def __init__(self) :
        self.lst = []
    def enqueue(self,element) :
        self.lst.append(element)
    def dequeue(self) :
        return self.lst.pop(0)
    def isempty(self) :
        return self.lst == [] 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (root) :
            q = queue()
            q.enqueue(root)
            lst = []
            while not q.isempty() :
                n = len(q.lst)
                temp = []
                for i in range(n) :
                    e = q.dequeue()
                    temp.append(e.val)
                    if (e.left) :
                        q.enqueue(e.left)
                    if (e.right) :
                        q.enqueue(e.right)
                lst.append(temp)
            return [i[-1] for i in lst]
        else :
            return []