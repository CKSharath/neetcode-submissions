class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def bt(i,j):
            if i==len(s):
                return True
            if j==len(t):
                return False
            if s[i]==t[j]:
                return bt(i+1,j+1)
            return bt(i,j+1)
        return bt(0,0)