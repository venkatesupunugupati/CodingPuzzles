def backspaceStringCompare(S:str,T:str) -> bool :
    # def build(S):
    #     res = []
    #     for c in S:
    #         if(c != '#'):
    #             res.append(c)
    #         elif res:
    #             res.pop()
    #     return "".join(res)
    # return build(S) == build(T)

    def get_string(st):
        s = ""
        for c in st:
            if c == "#":
                s = s[:-1]
            else:
                s += c
        return s
    return get_string(S) == get_string(T)


S = "a#b#c"
T = "s#e#c"
res = backspaceStringCompare(S,T)
print(res)

