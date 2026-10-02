class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res=[]
        def bt(s,i):
            if i==len(digits):
                v="".join(s)
                res.append(v)
                return
            for j in (n[digits[i]]):
                s.append(j)
                bt(s,i+1)
                s.pop()
        bt([],0)
        return res