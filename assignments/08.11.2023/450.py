# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def constructTreeFromList(self, nodeList) -> TreeNode:
        if not nodeList:
            return None
        rootNode = TreeNode(nodeList[0])
        listTree = [ rootNode ]
        for val in nodeList[1:]:
            newNode = TreeNode(val)
            for node in listTree:
                if not node.left:
                    node.left = newNode
                    # print(node)
                    break
                if not node.right:
                    node.right = newNode
                    # print(node)
                    break
            listTree.append(newNode)
        # print(f'root={rootNode}')
        return rootNode

    def findParent(self, rootNode, value) -> Optional[TreeNode]:
        if rootNode == None:
            return None
        if rootNode.val == value:
            return None
        if rootNode.left == None and rootNode.right == None:
            return None
        if rootNode.left != None and rootNode.left.val == value:
            return rootNode
        if rootNode.right != None and rootNode.right.val == value:
            return rootNode
        if value < rootNode.val and rootNode.left != None:
            return self.findParent(rootNode.left, value)
        if value > rootNode.val and rootNode.right != None:
            return self.findParent(rootNode.right, value)
        return None

    def findNode(self, root, value) -> TreeNode:
        if root == None:
            return None
        if root.val == value:
            return root
        elif value < root.val:
            return self.findNode(root.left, value)
        else:
            return self.findNode(root.right, value)

    def successorNode(self, succParent) -> Optional[TreeNode]:
        if succParent == None:
            return None
        succ = succParent.right
        while succ.left != None:
            succParent = succ
            succ = succ.left
        return succ

    def shiftNodes(self, root, u, v) -> TreeNode:
        u_p = self.findParent(root, u.val)
        if u_p == None:
            root = v
        elif u == u_p.left:
            u_p.left = v
        else:
            u_p.right = v
        if v != None:
            v_p = self.findParent(root, v.val)
            v_p = u_p
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        d = self.findNode(root, key)
        if d == None:
            return root
        if d.left == None:
            root = self.shiftNodes(root, d, d.right)
        elif d.right == None:
            root = self.shiftNodes(root, d, d.left)
        else:
            e = self.successorNode(d)
            e_p = self.findParent(root, e.val)
            if e_p != d:
                root = self.shiftNodes(root, e, e.right)
                e.right = d.right
                e_r_p = self.findParent(root, e.right.val)
                e_r_p = e
            root = self.shiftNodes(root, d, e)
            e.left = d.left
            e_l_p = self.findParent(root, e.left.val)
            e_l_p = e
        return root


