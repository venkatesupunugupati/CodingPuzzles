def sortarr(a):
    lo = 0
    hi = len(arr) - 1
    mid = 0
    while mid <= hi: 
        if a[mid] == 0: 
            a[lo], a[mid] = a[mid], a[lo] 
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[hi] = a[hi], a[mid]  
            hi = hi - 1
    return a
    

if __name__ == "__main__":
    arr = [0,1,2,0,0,2,1,0,2]    
    arr = sortarr(arr)
    print(arr)