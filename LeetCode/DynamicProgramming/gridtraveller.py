def gridTravellerRecursive(m:int,n:int,mem = {}):
    key = str(m) + "," + str(n)    
    if(key in mem):
        return mem[key]
    if(m == 0 or n == 0):return 0
    if(m == 1 and n == 1):return 1
    mem[key] = gridTravellerRecursive(m-1,n,mem) + gridTravellerRecursive(n,m-1,mem)
    return mem[key]

def gridTravellerIterative(m:int,n:int):
    temptable = [ [0]*(n+1) for i in range(m+1)]
    temptable[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            current = temptable[i][j]
            if(i+1 <= m):
                temptable[i+1][j] = temptable[i+1][j] + current
            if(j+1 <= n):
                temptable[i][j+1] = temptable[i][j+1] + current
    return temptable[m][n]


print(gridTravellerRecursive(18,18))
print(gridTravellerIterative(18,18))