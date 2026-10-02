class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        p=[i for i in range(n+1)]
        r=[1]*(n+1)
        def find(u):
            if u!=p[u]:
                p[u]=find(p[u])
            return p[u]
        def union(u,v):
            b,q=find(u),find(v)
            if b==q:
                return False
            if r[b]>r[q]:
                p[q]=b
                r[b]+=r[q]
            else:
                p[b]=q
                r[q]+=1
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []