class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l,h):
            if l>h:
                return None
            m=(l+h)//2
            return TreeNode(nums[m],build(l,m-1),build(m+1,h))
        return build(0,len(nums)-1)
