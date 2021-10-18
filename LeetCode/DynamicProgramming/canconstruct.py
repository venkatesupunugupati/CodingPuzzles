def canConstructRecursive(target, wordBank, mem):
    
    if(target in mem): return mem[target]
    if(target == ''): return True

    for word in wordBank:
        if(target.find(word) == 0):
            suffix = target[len(word):]
            if(canConstructRecursive(suffix,wordBank, mem) == True):
                mem[target] = True
                return mem[target]    
    
    mem[target] = False
    return mem[target]


def canConstructIterative(target, wordBank):

    tempTable = [False] * (len(target) + 1)
    tempTable[0] = True

    for i in range(len(tempTable)):
        if(tempTable[i] == True):
            for word in wordBank:
                if(target[i:i+len(word)] == word):
                    tempTable[i+len(word)] = True

    return tempTable[len(target)]

print(canConstructRecursive('abcdef',['ab','abc','cd','def','abcd'],{}))
print(canConstructRecursive('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeeee'],{}))

print(canConstructIterative('abcdef',['ab','abc','cd','def','abcd']))
print(canConstructIterative('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeeee']))