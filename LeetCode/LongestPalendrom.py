resultLength = 0
resultStart = 0

def LongestPalendrom(s:str):
    for i in range(len(s)-1):
        ExpandRange(s,i,i)
        ExpandRange(s,i,i+1)
    return s[resultStart:resultStart + resultLength]

def ExpandRange(st:str,begin:int,end:int):
    global resultLength
    global resultStart
    while(begin >= 0 and end < len(st) and st[begin] == st[end]):
        begin = begin - 1
        end = end + 1
    if(resultLength < (end - begin -1)):
        resultStart = begin + 1
        resultLength = end - begin -1

s = "cbbd"
lps = LongestPalendrom(s)
print(lps)