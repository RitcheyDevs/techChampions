def isSpecialNum(n):
    x = [int(i) for i in str(n)]
    y = x[::-1]
    checkResult = False
    for i in range(len(x)):
        if (y[i] <= y [i-1]):
            checkResult = True
        else:
            checkResult = False
    return checkResult

def getLastSN(n):
    lastSpecialNum = 0
    for i in range(799999999999999999,n):
        if (isSpecialNum(i)):
            lastSpecialNum = i
    return lastSpecialNum

file = open("output.txt","w+")

with open("Problem.txt") as task:
    T=int(task.readline())
    for i in range(1,T+1):
        x = [int(k) for k in map(int,task.readline().split())]
        a = x[0]
        file.write("Case #{}: {}\n".format(i,getLastSN(a)))

file.close()