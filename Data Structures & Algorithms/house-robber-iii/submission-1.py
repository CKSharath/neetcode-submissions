# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def bt(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            res=node.val
            if node.left:
                res+=bt(node.left.left)+bt(node.left.right)
            if node.right:
                res+=bt(node.right.left)+bt(node.right.right)
            res=max(res,bt(node.left)+bt(node.right))
            dp[node]=res
            return dp[node]
        return bt(root)
