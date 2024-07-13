import os

def make_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_data = f.readlines()
    big_list = []
    # Текущий кортеж
    current_list = []

    if file_path == 'data_first_variant.csv':
        for item in file_data:
            if item != "\n":
                current_list.append(item.strip())
            elif current_list:
                big_list.append(current_list)
                current_list = []
        
        if current_list:
            big_list.append(current_list)


    elif file_path == 'data_second_variant.csv':
        for item in file_data:
            if item != "\n":
                big_list.append(item.strip().split(';'))
            elif current_list:
                big_list.append(current_list)
                current_tuple = []

        if current_list:
            big_list.append(current_list)
    
    #print(tuples_list)
    
    return big_list

def data_search(phone_number):
    dir = '/Users/tasidorowa/Desktop/обучение разработчик/python'
    found_files = []
    for file_name in os.listdir(dir):
        if file_name.endswith('.csv'):
            data = make_list(file_name)
            for lst in data:
                if phone_number in lst:
                    found_files.append(file_name)
    if not found_files:
        return 0
    else:
        return found_files


#print(make_tuple('data_first_variant.csv'))

# with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
#         data_second = f.readlines()

print(data_search('7000'))