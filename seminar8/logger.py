from data_create import name_data, surname_data, phone_data, adress_data
from data_processing import make_list, data_search

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные?\n\nВариант 1:\n{name}\n{surname}\n{phone}\n{adress}\n\n"
                    f"Вариант 2:\n{name};{surname};{phone};{adress}\n\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input(f"В каком формате записать данные?\n\nВариант 1:\n{name}\n{surname}\n{phone}\n{adress}\n\n"
                    f"Вариант 2:\n{name};{surname};{phone};{adress}\n\n"
                    f"Выберите вариант: "))
        
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{adress}\n\n")
    #pass # Обозначает пустую функцию

def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
        #print(data_first)
    
    print('Вывожу данные из второго файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(data_second)

def change_data():
    phone_number = input('Введите номер телефона для поиска записи: ')
    files = data_search(phone_number)
    while files == 0:
       print ('Запись не найдена, возможно вы ввели неверный номер телефона или не телефон')
       phone_number = input('Введите номер телефона для поиска записи: ')
       files = data_search(phone_number)

    if files != 0:
        command = int(input('Какие данные нужно изменить?\n1: Имя\n2: Фамилию\n3: Номер телефона\n4: Адрес\n'))

        while command != 1 and command != 2 and command != 3 and command != 4:
            print('Неправильный ввод')
            command = int(input('Какие данные нужно изменить?\n1: Имя\n2: Фамилию\n3: Номер телефона\n4: Адрес\n'))

        if command == 1:
            name = input('Введите новое имя: ')
        elif command == 2:
            surname = input('Введите новую фамилию: ')
        elif command == 3:
            number = input('Введите новый телефон: ')
        elif command == 4:
            adress = input('Введите новую фамилию: ')
        
        # data = make_tuple(files[0])
        # for i in range(len(data)):
        #     print(i, data[i][2])


        for file in files:
            data = make_list(file)
            for i in range(len(data)):
                if data[i][2] == phone_number:
                    if command == 1:
                        data[i][command-1] = name
                    elif command == 2:
                        data[i][command-1] = surname
                    elif command == 3:
                        data[i][command-1] = number
                    elif command == 4:
                        data[i][command-1] = adress
                    
            with open(file, 'w', encoding='utf-8') as f:
                if  file == 'data_first_variant.csv':
                    for i in range(len(data)):
                        f.write(f"{data[i][0]}\n{data[i][1]}\n{data[i][2]}\n{data[i][3]}\n\n")   
                elif file == 'data_second_variant.csv':
                    for i in range(len(data)):
                        f.write(f"{data[i][0]};{data[i][1]};{data[i][2]};{data[i][3]}\n\n")
           
