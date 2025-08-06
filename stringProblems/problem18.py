def getPermutations(s):
    if len(s) == 0:
        return [""] 

    perm = []
    for i in range(0, len(s)):
        remStr = s[:i] + s[i+1:]
        
        subPerm = getPermutations(remStr)
        for j in subPerm:
            perm.append(s[i] + j)
            
    return perm

print(getPermutations("abc"))
