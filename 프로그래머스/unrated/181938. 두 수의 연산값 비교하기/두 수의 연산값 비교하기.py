def solution(a, b):
    strA = str(a)
    strB = str(b)
    if int(strA + strB) >= 2*a*b :
        return int(strA + strB)
    else:
        return 2*a*b