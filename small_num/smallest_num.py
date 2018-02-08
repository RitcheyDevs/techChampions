
def getSmallest(n):
    return min(n)

file = open("output.txt", "w+")

with open("Problem.txt") as task:
    T=int(task.readline())
    for i in range(1,T+1):
        x = [int(k) for k in map(int,task.readline().split(" "))]
        file.write("Case #{}: {}\n".format(i,getSmallest(x)))

file.close()