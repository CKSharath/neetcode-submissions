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
        def dfs(i,m):
            if not i:
                return
            if i.val>=m:
                ans[0]+=1
                m=i.val
            dfs(i.left,m)
            dfs(i.right,m)
        dfs(root,float('-inf'))
        return ans[0]
            