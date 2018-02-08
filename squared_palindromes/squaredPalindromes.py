import math

def isPalindrome(n):
    x = [int(i) for i in str(n)]
    reversed_x = (x[::-1])

    if (len(x) != 1 and x[0] == 0):
        return False

    if (x == reversed_x):
        return True 
    else:
        return False 


def isSquared(x):
    square_root = math.sqrt(x) 
    d_square = float(square_root**2) 

    if (int(square_root + 0.5) ** 2 == x):
        return True 
    else:
        return False 

def isSquaredPalindrome(n):
    sqrt_int = int(math.sqrt(n)+ 0.5) 
    if (isSquared(n) == True and isPalindrome(n) == True and isPalindrome(sqrt_int) == True):
        return True 
    else:
        return False 

def countPalindrome(a,b):
    total_palindromes = 0 
    for i in range(a,b+1):
        if (isSquaredPalindrome(i)):
            total_palindromes +=1 
    return total_palindromes 


#Write Output

file = open("output.txt","w+") 
with open("Problem.txt") as task:
    T=int(task.readline()) 
    for k in range(1,T+1):
        x = [int(i) for i in map(int,task.readline().split())] 
        a = x[0] 
        b = x[1] 
        file.write("Case #{}: {}\n".format(k,countPalindrome(a,b))) 

file.close() 