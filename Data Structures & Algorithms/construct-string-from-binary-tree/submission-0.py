# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def sol(n):
            if not n:
                return ''
            s=str(n.val)
            if n.left or n.right:
                s+= '('+sol(n.left)+')'
            if n.right:
                s+='('+sol(n.right)+')'
            return s
        return sol(root)