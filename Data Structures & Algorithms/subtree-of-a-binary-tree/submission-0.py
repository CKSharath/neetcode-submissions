# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def c(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return c(p.left,q.left) and c(p.right,q.right)
        m=[False]
        def dfs(n):
            if not n:
                return
            if c(n,subRoot):
                m[0]=True
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return m[0]
            
            