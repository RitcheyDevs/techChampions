def invertWord(word):
    new_word = word[::-1]
    inverted = ' '.join(new_word)
    return inverted

#print(invertWord("bimbo loves techchampions"))

file = open("output.txt","w+")

with open("Problem.txt") as task:
    T=int(task.readline())

    for i in range(1,T+1):
        x = [str(k) for k in map(str,task.readline().split())]
        file.write("Case #{}: {}\n".format(i,invertWord(x)))
file.close()