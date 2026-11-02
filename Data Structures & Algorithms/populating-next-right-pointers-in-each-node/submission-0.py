"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=deque()
        q.append(root)
        ans=[]
        while q:
            l=len(q)
            while l:
                n=q.popleft()
                if l>1:
                    n.next=q[0]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            
        return root