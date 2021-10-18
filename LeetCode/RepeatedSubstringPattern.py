def RepeatedSubstringPattern(s):
    l = len(s)
    for i in range(l//2,0,-1):
        if(l%i == 0):
            m = l//i
            subs = s[0:i]
            r = ""
            for j in range(m):
                r += subs
            if(r == s):
                return True
    return False

import math

def RepeatedStringMatch(a:str,b:str) -> int:
    m = math.ceil(len(b) / len(a))       
    if b in a * m:
        return m
    elif b in a * (m + 1):
        return m + 1
    else:
        return -1

# s="ababc"
# res = RepeatedSubstringPattern(s)
# print(res)
# a = "abcd"
# b = "cdabcdab"
# res = RepeatedStringMatch(a,b)
# print(res)

def findLUSlength(a: str, b: str) -> int:
    maxss = -1
    for i in range(len(a),-1,-1):
        ss = a[0:i]
        if not(ss in b):
            maxss = i
            break
    if(maxss == len(a) and maxss < len(b)):
        maxss = len(b)
    return maxss

a = "a"
b = "aaa"
res = findLUSlength(a,b)
print(res)
