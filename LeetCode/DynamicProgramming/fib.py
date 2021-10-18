def fibRecursive(n:int,mem={}):
    if(n in mem):
        return mem[n]
    if(n <= 2):
        return 1
    mem[n] = fibRecursive(n-1,mem) + fibRecursive(n-2,mem)
    return mem[n]

def fibIteratative(n:int):
    res = [0]*(n+1)
    res[1] = 1
    for i in range(n+2):
        if (i+1 <= n):
            res[i+1] = res[i+1] + res[i]
        if (i+2 <= n):
            res[i+2] = res[i+2] + res[i]
    return res[n]

print(fibRecursive(50))
print(fibIteratative(50))
