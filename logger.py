from data_create import name_data, text_data, data_create
import os


def input_data():
    name = name_data()
    text = text_data()
    data = data_create()
    if not os.path.isdir("notes"):
        os.mkdir("notes")
    with open(f'notes/{name}.csv', 'a', encoding='utf8') as f:
        f.write(f"{name}\n{text}\n{data}\n")


def show_note_list():
    print("Ваши заметки: \n")
    notes = os.listdir("notes")
    # Проверяем что заметки есть
    if len(notes) < 1:
        print("Заметок нет")
    else:
        n = 1
        # Выводим список заметок по именам
        for i in notes:
            print(f"{n}) {i}")
            n += 1
        print("\n")


def print_data():
    show_note_list()
    notes = os.listdir("notes")
    nn = input("Введите номер заметки для отображения: \n")
    # Считываем и выводим заметку
    with open(f'notes/{(notes[int(nn)-1])}', 'r', encoding='utf8') as f:
        data_first = f.readlines()
        for line in data_first:
            print(line)


def edit_data():
    show_note_list()
    notes = os.listdir("notes")
    if len(notes) >= 1:
        nn = input("Введите номер заметки для редактирования: \n")

        with open(f'notes/{(notes[int(nn)-1])}', 'r', encoding='utf8') as f:
            data_first = f.readlines()
            print(f"Старый текст:\n{data_first}")
        os.remove(f'notes/{(notes[int(nn)-1])}')
        input_data()


def del_data():
    show_note_list()
    notes = os.listdir("notes")
    if len(notes) >= 1:
        nn = input("Введите номер заметки для удаления: \n")
        os.remove(f'notes/{(notes[int(nn)-1])}')
