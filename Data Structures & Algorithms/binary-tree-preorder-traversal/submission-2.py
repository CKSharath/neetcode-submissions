# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def po(n):
            if not n:
                return
            a.append(n.val)
            po(n.left)
            po(n.right)
        po(root)
        return a