import datetime

def name_data():
    name = input("Введите название заметки: ")
    return name

def text_data():
    text = input("Введите текст заметки: ")
    return text

def data_create():
    data = datetime.date.today().isoformat()
    return data