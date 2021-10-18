def TrappingWater(arr:list):
     # initialize output
    result = 0
    n = len(arr)
    left_max = 0
    right_max = 0
    lo = 0
    hi = n-1
    while(lo <= hi):
        if(arr[lo] < arr[hi]):
            if(arr[lo] > left_max):
                # update max in left
                left_max = arr[lo]
            else:
                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1
        else:
            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1
    return result

h = [4,2,3]
tw = TrappingWater(h)
print(tw)