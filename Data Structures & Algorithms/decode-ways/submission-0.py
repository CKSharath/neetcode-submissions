class Solution:
    def numDecodings(self, s: str) -> int:
        def bt(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            res=bt(i+1)
            if i<len(s)-1:
                if (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    res+=bt(i+2)
            return res
        return bt(0)