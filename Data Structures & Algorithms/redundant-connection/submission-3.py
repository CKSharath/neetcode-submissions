class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        p=[i for i in range(n+1)]
        r=[1]*(n+1)
        def find(n):
            if n!=p[n]:
                p[n]=find(p[n])
            return p[n]
        def union(u,v):
            p1,p2=find(u),find(v)

            if p1==p2:
                return False
            
            if r[p1]>r[p2]:
                p[v]=u
                r[p1]+=r[p2]
            else:
                p[u]=v
                r[p2]+=r[p1]
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []