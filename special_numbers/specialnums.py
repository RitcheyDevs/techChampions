def dstr(i):
  i = int(i) - 1
  return str(i) if i else ""

def special_num(nums):
  chng_num = 1
  for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
      chng_num = i + 1
    if nums[i-1] > nums[i]:
      return dstr(nums[:chng_num]) + "9" * (len(nums) - chng_num)
  return nums

#t = int(input())
#for i in range(1, t+1):
#  print("Case #{}: {}".format(i, special_num(input())))



file = open("output.txt","w+")

with open("Problem.txt") as task:
    T=int(task.readline())
    for i in range(1,T+1):
        x = [int(k) for k in map(int,task.readline().split())]
        a = x[0]
        file.write("Case #{}: {}\n".format(i,special_num(str(a))))

file.close()