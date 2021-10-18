def CharBurst(s,l):
    temp = ""
    lastchar = ""
    count = 0
    for ch in s:
        if(lastchar != ch):
            if(count >= l):
                temp = temp.replace(lastchar,"",count)
            count = 1
            lastchar = ch
        else:
            count = count + 1
        temp = temp + ch
    if(count >= l):
        temp = temp.replace(lastchar,"",count)
    return temp

s = "abbccccdd"
bl = 3
out = CharBurst(s,bl)
print(out)