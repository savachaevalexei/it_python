from logger import input_data, print_data, edit_data, del_data


def interface():
    print ("Добрый день!\n 1 -Создать заметку\n 2 - Показать заметку\n 3 - Изменить заметку\n 4 - Удалить заметку")
    
    command = int(input("Введите число: "))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print ("Неправильный ввод!")
        command = int(input())

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        del_data()