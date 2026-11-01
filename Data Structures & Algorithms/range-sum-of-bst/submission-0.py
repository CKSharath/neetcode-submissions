# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s=[0]
        def dfs(n):
            if not n:
                return 0
            if low<=n.val<=high:
                s[0]+=n.val
            if n.val<low:
                dfs(n.right)
            if n.val>high:
                dfs(n.left)
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return s[0]