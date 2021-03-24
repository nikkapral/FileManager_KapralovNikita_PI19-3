import os,shutil




# 1. Создание папки (с указанием имени);
# 2. Удаление папки по имени;
# 3. Перемещение между папками (в пределах рабочей папки) - заход в папку
# по имени, выход на уровень вверх;
# 4. Создание пустых файлов с указанием имени;
# 5. Запись текста в файл;
# 6. Просмотр содержимого текстового файла;
# 7. Удаление файлов по имени;
# 8. Копирование файлов из одной папки в другую;
# 9. Перемещение файлов;
# 10. Переименование файлов.


# 1. Создание папки (с указанием имени)
def create_folder(path,name):
    try:
        os.mkdir(path + "\\" + name)
    except OSError:
        print("This directory already exists")

# 2. Удаление папки по имени
def remove_folder(path):
    shutil.rmtree(path)

# 3. Перемещение между папками (в пределах рабочей папки) - заход в папку
def move_in_folder(path):
    return path
    
# 4. Создание пустых файлов с указанием имени
def create_file(path):
    with open(path, "w+") as file:
        file.write("")
    
# 5. Запись текста в файл
def write_file(path,text):
    with open(path,"w") as file:
        file.write(text)

# 6. Просмотр содержимого текстового файла
def watch(path):
    with open(path,"r") as file:
        print(path)
        print(file.read())

# 7. Удаление файлов по имени
def remove_file(path):
    shutil.rmtree(path)

# 8. Копирование файлов из одной папки в другую
def copy_file(path,new_path):
    if os.path.isfile(path):
        try:
            shutil.copyfile(path, new_path)
        except FileExistsError:
            print("This file already exists")
    
# 9. Перемещение файлов
def move_file(path, new_path):
    if os.path.isdir(path):
        try:
            shutil.move(path, new_path)
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.remove(path)
        except FileExistsError:
            print("This file already exists")
    else:
        shutil.move(path, new_path)
        
# 10. Переименование файлов
def rename_file(path,name,new_name):
    os.rename(path + name, path + new_name)

