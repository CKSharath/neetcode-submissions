# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        c={None:0}
        def dfs(n):
            if not n:
                return c[n]
            if n in c:
                return c[n]
            c[n]=n.val
            if n.left:
                c[n]+=dfs(n.left.left)+dfs(n.left.right)
            if n.right:
                c[n]+=dfs(n.right.left)+dfs(n.right.right)
            c[n]=max(c[n],dfs(n.left)+dfs(n.right))
            return c[n]
        return dfs(root)