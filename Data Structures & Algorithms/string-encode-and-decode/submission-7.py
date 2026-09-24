class Solution:

    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
            s.append(str(len(i)))
            s.append('#')
            s.append(i)
            
        return "".join(s)

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