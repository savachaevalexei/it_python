from data_create import name_data, text_data, data_create
import os
import re

def input_data():
    name = name_data()
    text = text_data()
    data = data_create()
    if not os.path.isdir("notes"):
        os.mkdir("notes")
    with open(f'notes/{name}.csv', 'a', encoding='utf8') as f:
        f.write(f"{name}\n{text}\n{data}\n")


def print_data():
    print("Ваши заметки: \n")
    notes = os.listdir("notes") 
    # Проверяем что заметки есть
    if len(notes) < 1:
        print ("Заметок нет")
    else:
        n = 1
        # Выводим список заметок по именам
        for i in notes:
            print (f"{n}) {i}")
            n+=1

    nn = input("Введите номер заметки для отображения: \n")
   

    
    with open(f'notes/{(notes[int(nn)-1])}', 'r', encoding='utf8') as f:
        data_first = f.readlines()
      

        for line in data_first:
            print(line)
        

