csvfile = open('user.csv','r')

for line in csvfile:
    split_line = line.split(';')

    print(f'Имя - {split_line[0]}, фамилия - {split_line[1]}, телефон {split_line[2]}')
