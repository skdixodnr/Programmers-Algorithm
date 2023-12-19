def solution(a, b):
    strA = str(a)
    strB = str(b)
    if strA + strB < strB + strA:
        return int(strB + strA)
    elif strA + strB > strB + strA:
        return int(strA + strB)
    else :
        return int(strA + strB)