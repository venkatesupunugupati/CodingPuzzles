def MedianOfTwoArrays(a1 : list, a2 : list):
    m = []
    i1 = 0
    i2 = 0
    while (i1 < len(a1)) and (i2 < len(a2)):
        if(a1[i1] < a2[i2]):
            m.append(a1[i1])
            i1 = i1 + 1
        else:
            m.append(a2[i2])
            i2 = i2 + 1
    while(i1 < len(a1)):
        m.append(a1[i1])
        i1 = i1 + 1
    while(i2 < len(a2)):
        m.append(a2[i2])
        i2 = i2 + 1
    print(m)
    if(len(m)%2 == 0):
        return (m[len(m)//2-1] + m[(len(m)//2)])/2
    else:
        return (m[len(m)//2])

a1 = [2]
a2 = []
m = MedianOfTwoArrays(a1,a2)
print(m)
