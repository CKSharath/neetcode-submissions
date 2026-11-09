# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans=[0]
        def dfs(n,m):
            if not n:
                return
            if n.val>=m:
                ans[0]+=1
            dfs(n.left,max(m,n.val))
            dfs(n.right,max(m,n.val))
        dfs(root,root.val)
        return ans[0]