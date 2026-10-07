class Solution:
    def reverse(self, x: int) -> int:
        v=2**31
        
        sign=1
        if x<0:
            x*=-1
            sign=-1
        rev=0
        n=x
        while n>0:
            r=n%10
            rev=rev*10+r
            n=n//10
        rev=sign*rev  
        if rev<=-v or rev>=v-1:
            return 0      
        return rev
        