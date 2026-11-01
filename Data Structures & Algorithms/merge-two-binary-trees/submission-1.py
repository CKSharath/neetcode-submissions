# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(p,q):
            if not p and not q:
                return None
            np=p.val if p else 0
            nq=q.val if q else 0
            sm=np+nq

            if p:
                p.val=sm
            else:
                p=TreeNode(sm)
            p.left=dfs(p.left,q.left if q else None)
            p.right=dfs(p.right,q.right if q else None)
            return p
        return dfs(root1,root2)

