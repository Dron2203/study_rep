from math import sqrt

bad_data = True
while bad_data == True:
    try:
        a = int(input('введите а:'))
        b = int(input('введите b:'))
        c = int(input('введите c:'))
        bad_data = False
    except:
        print('Ведены неверные данные')
D = b * b - (4 * a * c)
print(f'Дискриминант равен {D}')
if D < 0:
    print('уравнение не имеет корней')
elif D == 0:
    x1 = (-b) / 2 * a
    print(f'Уравнение имеет один корень, X1={x1}')
else:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - sqrt(D)) / (2 * a)
    print(f'Корни уравнения X1={x1},X2={x2}')
