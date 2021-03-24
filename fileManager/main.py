# 1. Расположение рабочей папки должно указываться в настройках файлового
# менеджера. Настройки должны располагаться в отдельном от основного
# исходного кода файле.

# 2. Файловый менеджер должен блокировать пользователя от выхода за
# пределы рабочей папки. Пользователь должен воспринимать рабочую
# папку как корневую и все действия файлового менеджера должны
# локализоваться только в пределах этой папки.

# 3. Программный проект должен быть оформлен как код на языке
# программирования Python и располагаться в определенной папке. Проект
# должен состоять из нескольких файлов. Расположение рабочей папки не
# должно быть связано с физическим расположением файлов исходного
# кода.

# 4. Файловый менеджер по умолчанию должен иметь текстовый интерфейс по
# аналогии с интерфейсом командной строки. Действия пользователя
# осуществляются вводом с клавиатуры соответствующей команды (по
# необходимости с параметрами).

# 5. Код должен быть организован в виде набора функций или классов, каждая
# операция файлового менеджера должна быть реализована в отдельной
# функции или методе класса.

# 6. Файловый менеджер должен быть кроссплатформенным и работать как в
# среде Windows, так и в UNIX системах. Необходимо протестировать
# работоспособность программы в разных ОС. Для кроссплатформенности
# рекомендуется использовать стандартную библиотеку Python для
# осуществления файловых операций.

# 7. Разработка программы должна вестись с использованием СКВ Git. Код
# должен публиковаться в репозитории на GitHub.

# 8. Перед разработкой программист должен продумать названия и структуру
# команд для пользователя. Команды не должны повторять команды
# существующих программных оболочек.

import os
from commands import create_folder, remove_folder, move_in_folder, create_file, write_file, watch, remove_file, copy_file, move_file, rename_file 

with open ('settings.txt') as file:
    path = file.read()


def main(path):

    command = str(input('Command:: \n  '))

    if command == "create_folder":
        name = str(input("Name of the folder: \n  "))
        create_folder(path,name)

    elif command == "remove_folder":
        try:
            for i in os.scandir(path):
                if i.is_dir:
                    folder_name = i.path.rpartition('\\')[2]
                    print("Folder:", folder_name)
            name = str(input("Name of the folder:"))
            remove_folder(path + "\\" + name)
        except Exception:
            print("ERROR")

    elif command == "move_in_folder":
        try:
            for i in os.scandir(path):
                if i.is_dir:
                    folder_name = i.path.rpartition('\\')[2]
                    print("Folder:", folder_name)
            name = str(input("Name of the folder we move in:"))
            main(move_in_folder(path + "\\" + name))
        except Exception:
            print("ERROR")
    
    elif command == "create_file":
        name = str(input("Name of the file:"))
        create_file(path + "\\" + name)

    elif command == "write_file":
        try:
            for i in os.scandir(path):
                if i.is_file:
                    file_name = i.path.rpartition('\\')[2]
                    print("File:", file_name)
            name = str(input("Name of the file to write in:"))
            text = str(input("What to write:"))
            write_file(path + "\\" + name, text)
        except Exception:
            print("ERROR")
    
    elif command == "watch":
        try:
            for i in os.scandir(path):
                if i.is_file:
                    file_name = i.path.rpartition('\\')[2]
                    print("File:", file_name)
            name = str(input("Name of the file to read:"))
            watch(path + "\\" + name)
        except Exception:
            print("Error")
    elif command == "remove_file":
        try:
            for i in os.scandir(path):
                if i.is_file:
                    file_name = i.path.rpartition('\\')[2]
                    print("File:", file_name)
            name = str(input("Name of the file to remove:"))
            remove_file(path + "\\" + name)
        except Exception:
            print("ERROR")
    elif command == "copy_file":
        for i in os.scandir(path):
            if i.is_file:
                file_name = i.path.rpartition('\\')[2]
                print("File:", file_name)
        name = str(input("Name of the file to copy:"))
        new_path = str(input("Name of the path where to copy:"))
        if check_path(path,new_path) == True:
            copy_file(path + "\\" + name,new_path)
        else:
            print("Error path")

    elif command == "move_file":
        try:
            for i in os.scandir(path):
                if i.is_file:
                    file_name = i.path.rpartition('\\')[2]
                    print("File:", file_name)
            name = str(input("Name of the file to move:"))
            new_path = str(input("Name of the path where to move:"))
            if check_path(path,new_path) == True:
                move_file(path + "\\" + name,new_path)
            else:
                print("Error path")
        except Exception:
            print("Error. Try again.")
    elif command == "rename_file":
        try:
            for i in os.scandir(path):
                if i.is_file:
                    file_name = i.path.rpartition('\\')[2]
                    print("File:", file_name)
            name = str(input("Name of the file to rename:"))
            new_name = str(input("New name of the file:"))
            rename_file(path,name,new_name)
        except FileNotFoundError:
            print("No files founded")
    else:
        print("Uknown command. Try again")
        main(path)

    
def check_path(path,new_path):
    if new_path in path:
        return True
    else:
        return False


main(path)