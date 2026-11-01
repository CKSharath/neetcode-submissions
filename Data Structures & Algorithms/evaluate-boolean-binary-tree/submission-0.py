# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        s=[]
        def po(n):
            if not n:
                return
            s.append(n.val)
            po(n.left)
            po(n.right)
        po(root)
        while len(s)>1:
            v1=s.pop()
            v2=s.pop()
            o=s.pop()
            if o==2:
                v=v1+v2
                if v==2:
                    v=1
                s.append(v)
            elif o==3:
                s.append(v1*v2)
        return True if s[-1]==1 else False
            