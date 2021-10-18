def ValidParentheses(s):
    d = {'(','[','{'}
    stack = []
    n = len(s)

    if (n < 2 or (n > 2 and n%2 != 0)):
        return False

    for i in range(n):
        if(s[i] in d):
            stack.append(s[i])
        else:
            if not((len(stack) != 0) and ((s[i] == ')' and stack.pop() == '(') or (s[i] == ']' and stack.pop() == '[') or (s[i] == '}' and stack.pop() == '{'))):
                return False
    return (len(stack) == 0)

s = "["
r = ValidParentheses(s)
print(r)