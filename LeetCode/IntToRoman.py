def IntToRoman(num:int):
    mydict = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
    rvalue =""
    for k in mydict.keys():
        rvalue = rvalue + mydict[k] * (num//k)
        num=num%k
    rvalue = rvalue.replace('DCCCC','CM')
    rvalue = rvalue.replace('CCCC','CD')
    rvalue = rvalue.replace('LXXXX','XC')
    rvalue = rvalue.replace('XXXX','XL')
    rvalue = rvalue.replace('VIIII','IX')
    rvalue = rvalue.replace('IIII','IV')
    return rvalue

num = 1994
r = IntToRoman(num)
print(r)
