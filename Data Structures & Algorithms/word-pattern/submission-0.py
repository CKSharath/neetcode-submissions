class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split(" ")
        if len(w)!=len(pattern):
            return False
        cTow={}
        wToc={}
        for c,wrd in zip(pattern,w):
            if c in cTow and cTow[c]!=wrd:
                return False
            if wrd in wToc and wToc[wrd]!=c:
                return False
            cTow[c]=wrd
            wToc[wrd]=c
        return True