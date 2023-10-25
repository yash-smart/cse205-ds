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
    def isempty(self) :
        return self.lst == []
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = stack()
        curr = root
        post = []
        while (curr != None) or (not st.isempty()) :
            if (curr != None) :
                st.push(curr)
                curr = curr.left
            else :
                temp = st.top().right
                if (temp == None) :
                    temp = st.top()
                    st.pop()
                    post.append(temp.val)
                    while (not st.isempty()) and (temp == st.top().right) :
                        temp = st.top()
                        st.pop()
                        post.append(temp.val)
                else :
                    curr = temp
        return post