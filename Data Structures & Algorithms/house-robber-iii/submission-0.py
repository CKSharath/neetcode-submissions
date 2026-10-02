# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def bt(root):
            if not root:
                return 0
            if root in dp:
                return dp[root]
            res=root.val
            if root.left:
                res+=(bt(root.left.left)+bt(root.left.right))
            if root.right:
                res+=(bt(root.right.left)+bt(root.right.right))
            res=max(res,bt(root.left)+bt(root.right))
            dp[root]=res
            return dp[root]
        return bt(root)