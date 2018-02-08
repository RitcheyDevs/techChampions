import math

def hackPin(n):
    base_formular = (n + (math.sqrt(n))) **n
    formular_list = str(base_formular).split(".")
    pin = formular_list[0]
    pin_len = len(str(pin))
    if (pin_len < 4):
        for i in range(4-pin_len):
            pin = "0"+pin
    else:
        pin = pin[0:4]

    return pin

file = open("output.txt", "w+")

with open("Problem.txt") as task:
    T = int(task.readline())
    for i in range(1,T+1):
        n = int(task.readline())

        file.write("Case #{}: {}\n".format(i,hackPin(n)))

file.close
