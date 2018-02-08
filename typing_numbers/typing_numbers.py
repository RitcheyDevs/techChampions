keyMapping = {'a':2, 'b':22, 'c':222, 'd':3, 'e':33, 'f':333, 'g':4, 'h':44, 'i':444, 'j':5, 'k':55, 'l':555, 'm':6, 'n':66, 'o':666, 'p':7, 'q':77, 'r':777, 's':7777, 't':8, 'u':88, 'v':888, 'w':9, 'x':99, 'y':999, 'z':9999, ' ':0, '\n':''}

def getNum(letter):
    result = ""
    x = list(letter)
    for i in range(len(letter)):
        currentKey = str(keyMapping.get(x[i]))
        nextKey = str(keyMapping.get(x[i-1]))
        
        if (nextKey.find(currentKey) != -1 or currentKey.find(nextKey) != -1):
            result += " "+currentKey
        else:
            result += currentKey

    return str.rstrip(str.lstrip(result))


file = open("output.txt","w+")

with open("Problem.txt") as task:
    N = int(task.readline())
    for i in range(1,N+1):
        words = str(task.readline())
        file.write("Case #{}: {}\n".format(i,getNum(words)))

file.close()