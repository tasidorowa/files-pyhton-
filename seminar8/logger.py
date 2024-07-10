from data_create import name_data, surname_data, phone_data, adress_data
from data_processing import make_tuple, data_search

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

def change_data(phone_number):
    data_search(phone_number)
    




#print_data()
