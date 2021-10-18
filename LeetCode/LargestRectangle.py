from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans

heights = [2,1,5,6,2,3]
area = largestRectangleArea(heights)
print(area)