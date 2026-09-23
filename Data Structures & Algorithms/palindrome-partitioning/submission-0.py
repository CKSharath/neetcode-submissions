class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkP(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        res=[]
        part=[]
        def dfs(j,i):
            if i>=len(s):
                if j==i:
                    res.append(part[:])
                return
            if checkP(j,i):
                part.append(s[j:i+1])
                dfs(i+1,i+1)
                part.pop()
            dfs(j,i+1)
        dfs(0,0)
        return res