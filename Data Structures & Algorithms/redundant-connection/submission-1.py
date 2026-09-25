class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        r=[1]*(n+1)
        p=[i for i in range(n+1)]

        def find(n):
            if n!=p[n]:
                p[n]=find(p[n])
            return p[n]
        def union(u,v):
            pu,pv=find(u),find(v)
            if pu==pv:
                return False

            if r[pu]>r[pv]:
                p[pv]=pu
                r[pu]+=r[pv]
            else:
                p[pu]=pv
                r[pv]+=r[pu]
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []