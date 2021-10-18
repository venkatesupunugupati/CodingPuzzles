def countAndSay(n: int) -> str:
    ans = '1'
    i = 1
    while(i < n):
        temp = ''
        num_to_say = ans[0]
        count = 0
        for index in range(len(ans)):
            if(ans[index] == num_to_say):
                count += 1
            elif(ans[index] != num_to_say):
                #We run into a number we're not counting so we add to 
                #the temp and continue iterating through the current string
                temp += str(count) + num_to_say
                num_to_say = ans[index]
                count = 1
        temp += str(count) + num_to_say
        ans = temp #replace so we can count and say again
        i += 1
    return ans

n = 6
res = countAndSay(n)
print(res)