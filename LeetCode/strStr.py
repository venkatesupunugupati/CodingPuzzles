def strStr(haystack: str, needle: str):
    if not needle:
        return 0
    return haystack.find(needle)

haystack = "aaaaa"
needle = "ll"
index = strStr(haystack,needle)
print(index)