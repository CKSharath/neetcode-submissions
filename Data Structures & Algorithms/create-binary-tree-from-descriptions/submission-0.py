class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node={}
        child=set()
        for p,c,l in descriptions:
            child.add(c)
            if p not in node:
                node[p]=TreeNode(p)
            if c not in node:
                node[c]=TreeNode(c)
            if l:
                node[p].left=node[c]
            else:
                node[p].right=node[c]
        for p,c,l in descriptions:
            if p not in child:
                return node[p]
