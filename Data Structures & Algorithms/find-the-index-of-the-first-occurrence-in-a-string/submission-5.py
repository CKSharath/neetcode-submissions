class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        ans=-1
        l=0
        while l<=(len(haystack)-len(needle)):
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

                    l+=1

        return ans