import math
min_a = 1000000
n=int(input("Введите натуральное число n "))
for i in range (1,n+1):
    a= (i-1)/(i+1)+math.sin(((i-1)**3)/(i+1))
    print(a)
    if a<min_a and a>0:
        min_a=a
print("минимальный", min_a)