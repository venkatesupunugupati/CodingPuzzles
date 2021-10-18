
def isPalindrome(x:int) -> bool:
    rn = 0
    temp = x
    dec = 10
    while(x > 0):
        rn = rn*dec + x%dec
        x = x//dec
    if(temp == rn):
        return True
    else:
        return False

i = 121
s = isPalindrome(i)
print(s)