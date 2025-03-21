import math
Xn = float(input("Введите Xn="))
Xk = float(input("Введите Xk=")) #ввод с клавиатуры
S=0
a=5.27

K = 0
x=Xn
DX = 1
print(" X"," ","Z")
while x<=Xk:
    Z= (x ** (1/3)) + math.sin(a*x) / math.log((a**4) + 2.65)

    print(round(x,3)," ",round(Z,3))

    if Z>0:
        K+=1; S=S+Z#количество и сумма положительных значений у

    x+=DX

print(f"СРеднее арифметическое y = {S/K}",)

