from logger import input_data, print_data, change_data

def interface():
    print('Добрый день! Это бот-справочник Таня\n1: Записать данные\n2: Вывести данные')
    command = int(input('Введите номер команды: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print('Неправильный ввод')
        command = int(input('Введите номер команды: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data()
    # elif command == 4:
    #     delete_data()

