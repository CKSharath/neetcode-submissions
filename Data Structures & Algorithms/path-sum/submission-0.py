# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n,s):
            if not n:
                return False
            s+=n.val
            if not n.left and not n.right:
                return s==targetSum
            return dfs(n.left,s) or dfs(n.right,s)
        return dfs(root,0)