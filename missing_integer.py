def solution(A):
    #better not use max(), instead use check at the first cycle of the this function A[i] > 0
    #but solution was committed with the next line and got 100%
    maxA = max(A)
    if maxA <= 0:
        return 1

    ln = len(A)
    if ln == 1:
        if A[0] == 1:
            return 2
        else:
            return 1

    lst = [False for x in range(maxA+1)] 
    
    i = 0
    while(i < ln):
        if A[i] > 0:
            lst[A[i]] = True
        i += 1

    i = 1
    while(i < maxA):
        if lst[i] == False:
           return i
        i += 1
    
    return i + 1