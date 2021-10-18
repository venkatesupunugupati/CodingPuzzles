def RomanToInteger(x:str):
    mydict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    intval = 0
    prvval = 0
    temp = ""
    for ch in x:  
        if(prvval == 0):
            prvval = mydict[ch]
            intval = mydict[ch]
        else:
            if(prvval < mydict[ch]):
                intval = intval + mydict[ch] - 2*prvval
            else:
                prvval = mydict[ch]
                intval = intval + mydict[ch]                        
    return intval

r = "IX"
i = RomanToInteger(r)
print(i)