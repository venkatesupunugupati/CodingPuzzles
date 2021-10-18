import math
def multiply(num1,num2):
    # if (num1 == "0" or num2 == "0" ):
    #         return "0"
    # M = len(num1)
    # N = len(num2)
    # arr = [0] * (M + N)
    # for i in range(M-1,-1,-1):
    #     for j in range(N-1,-1,-1):
    #         mul = (int(num1[i]) - int('0')) * (int(num2[j]) - int('0')) + arr[i+j+1]
    #         arr[i+j+1] = mul % 10
    #         arr[i+j] += mul//10

    # index = 0
    # res = ""
    # while(arr[index] == 0):
    #     index += 1    
    # for i in range(index,len(arr)):
    #     res += str(arr[i])
    # return res
    ans=0        
    for i,v1 in enumerate(reversed(num1)):
        for j,v2 in enumerate(reversed(num2)):
            ans+=(ord(v1)-ord('0'))*(ord(v2)-ord('0'))*(10**(i+j))
    return str(ans)
num1 = "123"
num2 = "456"
res = multiply(num1,num2)
print(res)