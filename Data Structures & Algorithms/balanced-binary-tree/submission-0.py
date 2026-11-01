# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(n):
            if not n:
                return 0
            return 1+max(h(n.left),h(n.right))
        def dfs(node):
            if not node:
                return True
            if abs(h(node.left)-h(node.right))>1:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
        