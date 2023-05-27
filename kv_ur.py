bad_data = True
while bad_data == True:
    try:
        a = int(input('введите а:'))
        b = int(input('введите b:'))
        c = int(input('введите c:'))
        bad_data = False
    except:
        print('Ведены неверные данные')