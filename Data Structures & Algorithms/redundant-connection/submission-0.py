class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]*(n+1)

        def find(n):
            if n!=par[n]:
                par[n]=find(par[n])
            return par[n]
        def union(n1,n2):
            pn1,pn2=find(n1),find(n2)
            if pn1==pn2:
                return False
            if rank[pn1]>rank[pn2]:
                par[pn2]=pn1
                rank[pn1]+=rank[pn2]
            else:
                par[pn1]=pn2
                rank[pn2]+=rank[pn1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        return []