class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        ans=-1
        while l<len(haystack)-len(needle):
            if haystack[l]==needle[0]:
                res=True
                for i in range(len(needle)):
                    if needle[i]!=haystack[i+l]:
                        res=False
                if res:
                    return l
                else:
                    l+=1
            else:
                l+=1
        return -1