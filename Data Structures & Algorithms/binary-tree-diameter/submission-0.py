# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def d(n):
            if not n:
                return 0
            lh=h(n.left)
            rh=h(n.right)
            dm=lh+rh
            sub=max(d(n.left),d(n.right))
            return max(dm,sub)
        def h(n):
            if not n:
                return 0
            return 1+max(h(n.left),h(n.right))
        return d(root)