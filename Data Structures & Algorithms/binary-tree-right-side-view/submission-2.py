# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(n,i):
            if not n:
                return
            if len(res)==i:
                res.append(n.val)
            dfs(n.right,i+1)
            dfs(n.left,i+1)
        dfs(root,0)
        return res
