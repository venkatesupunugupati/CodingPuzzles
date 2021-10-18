def ContainerWithMostWater(height):
    maxArea = 0
    left = 0
    right = len(height) - 1
    while(left < right):
        maxArea = max(maxArea, min(height[left],height[right])*(right-left))
        if(height[left] < height[right]):
            left = left + 1
        else:
            right = right - 1
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
area = ContainerWithMostWater(height)
print(area)
