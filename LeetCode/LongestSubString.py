def LongestSubString(s):
    print(s)
    ar = []
    maxlength = 0
    for ch in s:
        if (ch in ar):
            ar = ar[ar.index(ch)+1:]
        ar.append(ch)
        if(len(ar) > maxlength):
            maxlength = len(ar)
    return maxlength if maxlength > len(ar) else len(ar)


if __name__ == "__main__":
    s = "ckilbkd"
    l = LongestSubString(s)
    print(l)