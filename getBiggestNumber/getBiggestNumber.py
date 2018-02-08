
def getBiggest(x):
    return max(x);

file=open("output.txt","w+");

with open("Problem-1.txt") as task:
    T=int(task.readline());
    for j in range(1,T+1):
        k=[int(i) for i in map(int,task.readline().split())];
        file.write("Case #{}: {}\n".format(j,getBiggest(k)));

file.close();
