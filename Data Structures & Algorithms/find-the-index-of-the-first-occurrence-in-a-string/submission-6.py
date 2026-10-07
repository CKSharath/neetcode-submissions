class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        while j<len(haystack)-len(needle):
            i=0
            while needle[i]==haystack[j+i]:
                i+=1
                if i==len(needle):
                    return j
            j+=1
        return -1