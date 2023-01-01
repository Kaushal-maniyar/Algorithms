import math

n = int(input("Give any number :"))
div_list = []
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        div_list.append(n//i)
        div_list.append(i)
div_list.sort()

print(div_list)
