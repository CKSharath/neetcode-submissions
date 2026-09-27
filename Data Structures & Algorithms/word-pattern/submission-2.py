class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(" ")
        if len(pattern)!=len(word):
            return False
        ctow={}
        wtoc={}

        for c,w in zip(pattern,word):
            if c in ctow and ctow[c]!=w:
                return False
            if w in wtoc and wtoc[w]!=c:
                return False
            ctow[c]=w
            wtoc[w]=c
        return True