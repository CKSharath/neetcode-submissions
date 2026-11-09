# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            l=len(q)
            a=[]
            for i in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                a.append(n.val)
            res.append(a)
        return res
