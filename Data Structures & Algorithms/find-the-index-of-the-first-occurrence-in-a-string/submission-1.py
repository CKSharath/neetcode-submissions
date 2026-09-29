class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans=-1
        l=0
        while l<len(haystack):
            if haystack[l]==needle[0]:
                res=True
                for i in range(len(needle)):
                    if haystack[l+i]!=needle[i]:
                        res=False
                if res:
                    return l
                else:
                    l+=1
            else:
                if haystack[l] in needle:
                    l+=1
                else:
                    l+=len(needle)
        return ans