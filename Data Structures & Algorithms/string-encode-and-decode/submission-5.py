class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            lenn=int(s[i:j])
            i=j+1
            j=lenn+i
            ans.append(s[i:j])
            i=j
        return ans

