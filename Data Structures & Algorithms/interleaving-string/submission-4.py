class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        def bt(i,j,k):
            if k==len(s3):
                return i==len(s1) and j==len(s2)
            if s1[i]==s3[k]:
                if bt(i+1,j,k+1):
                    return True
            if s2[j]==s3[k]:
                if bt(i,j+1,k+1):
                    return True
            return False
        return bt(0,0,0)