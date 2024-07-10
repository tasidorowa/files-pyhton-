import os

def make_tuple(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_data = f.readlines()
    tuples_list = []
    # Текущий кортеж
    current_tuple = ()

    for item in file_data:
        if item != "\n":
            current_tuple += (item,)
        elif current_tuple:
            tuples_list.append(current_tuple)
            current_tuple = ()
    
    if current_tuple:
        tuples_list.append(current_tuple)
    
    return tuples_list

def data_search(phone_number):
    dir = '/Users/tasidorowa/Desktop/обучение разработчик/python'
    found_files = []
    for filename in os.listdir(dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = f.readlines()
                if phone_number+'\n' in data:
                    found_files.append(filename)
    if not found_files:
        return 0
    else:
        return found_files


