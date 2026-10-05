class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        st=[]
        for i in s:
            if i in [')','(']:
                if i==')':
                    st.pop()
                else:
                    st.append(i)
            res=max(res,len(st))
        return res
