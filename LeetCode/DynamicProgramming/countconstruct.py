def countConstructRecursive(target, wordBank, mem):

    if(target in mem): return mem[target]
    if(target == ''): return 1

    totalCount = 0

    for word in wordBank:
        if(target.find(word) == 0):
            numways = countConstructRecursive(target[len(word):],wordBank,mem)
            totalCount += numways
    
    mem[target] = totalCount
    return totalCount

def countConstructIterative(target, wordBank):

    temptable = [0] * (len(target) + 1)
    temptable[0] = 1

    for i in range(len(temptable)):
            for word in wordBank:
                if(target[i:i+len(word)] == word):
                    temptable[i+len(word)] += temptable[i]

    return temptable[len(target)]



print(countConstructRecursive('purple',['purp','p','ur','le','purpl'],{}))
print(countConstructRecursive('abcdef',['ab','abc','cd','def','abcd'],{}))
print(countConstructRecursive('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeeee'],{}))

print(countConstructIterative('purple',['purp','p','ur','le','purpl']))
print(countConstructIterative('abcdef',['ab','abc','cd','def','abcd']))
print(countConstructIterative('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeeee']))