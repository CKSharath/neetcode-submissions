class Solution:
    def maxDepth(self, s: str) -> int:
        m=0
        st=[]
        v=['(',')']
        for i in s:
            if i not in v:
                continue
            elif st and i==')' and st[-1]=='(':
                st.pop()
            else:
                st.append(i)
            m=max(m,len(st))
        return m