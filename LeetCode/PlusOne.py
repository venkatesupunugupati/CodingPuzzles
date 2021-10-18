def PlusOne(digits):
    l = len(digits)
    c = 0
    for d in digits[::-1]:
        if(l == len(digits)):
            d = d + 1
        digits[l-1] = (c + d)%10
        c = (c + d) // 10
        l = l - 1
    if(c > 0):
        digits.insert(0,c)
    return digits

nums = [9,9,9,9]
res = PlusOne(nums)
print(res)