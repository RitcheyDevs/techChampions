def getSmallest(v1,v2, len_v):
    v1.sort()
    v2.sort()
    v2.reverse()

    result = 0
    for i in range(len_v):
        result += v1[i] * v2[i]

    return result

file = open("output.txt","w+")

with open("Problem.txt") as task:
    T=int(task.readline())

    for i in range(1,T+1):
        len_v = int(task.readline())

        v1 = [int(k) for k in map(int,task.readline().split(" "))]
        v2 = [int(j) for j in map(int,task.readline().split(" "))]

        file.write("Case #{}: {}\n".format(i,getSmallest(v1,v2,len_v)))

file.close()