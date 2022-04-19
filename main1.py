import math

a = float(input("Введите коэффициент при Х^2 "))
b = float(input("Введите коэффициент при X "))
c = float(input('Введите свободный коэффициент '))
d = (pow(b, 2))-(4*a*c)
if (d < 0):
    print('Корни комплексные, посчитать не могу')
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
