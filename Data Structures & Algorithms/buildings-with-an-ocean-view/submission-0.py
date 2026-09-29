class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        cmp = [0] * len(heights)
        mx = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            cmp[i] = mx
            mx = max(mx, heights[i])
        res = []
        for i in range(len(heights)):
            if heights[i] > cmp[i]:
                res.append(i)

        return res
