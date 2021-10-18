def maxSubArray(nums):
    n = len(nums)
    dp = [nums[0]]
    maxval = dp[0]

    for i in range(1,n):
        dp.append(nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0))
        maxval = max(maxval,dp[i])
    return maxval

nums = [-2,1,-3,4,-1,2,1,-5,4]
res = maxSubArray(nums)
print(res)