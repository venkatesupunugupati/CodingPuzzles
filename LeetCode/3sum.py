def Sum3(nums):
    result = []
    length = len(nums)-1
    nums.sort()                             # sort the array to save time complexity

    for i in range(length-1):
        if i > 0 and nums[i] == nums[i-1]:  # when i's index is greater than 0 and their values are equal, jump it to avoid repetition
            continue
        j = i+1
        k = length
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if not temp:
                result.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif temp < 0:
                j += 1
            else:
                k -= 1
    return result

nums = [1,-1,-1,0]
result = Sum3(nums)
print(result)