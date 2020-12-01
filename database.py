# coding=utf-8
import pyrebase
import random

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote




def init_firebase():
    firebaseConfig = {'apiKey': "AIzaSyCcFUTbszDhbcZxCuXqM85MWr80FPhvY58",
                      'authDomain': "dormitory-c5829.firebaseapp.com",
                      'databaseURL': "https://dormitory-c5829.firebaseio.com",
                      'projectId': "dormitory-c5829",
                      'storageBucket': "dormitory-c5829.appspot.com",
                      'messagingSenderId': "282371830331",
                      'appId': "1:282371830331:web:c8c5c754d20184a045221e",
                      'measurementId': "G-QZSM07QZ73"}
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase.database()

# функции общежития
def add_dormitory(number,address):
    db = init_firebase()
    dormitoryData = {'number': number, 'Rooms': {0:''}, 'name': 'Общежитие ' + str(number), 'Адрес':address}
    db.child('dormitory' + str(number)).set(dormitoryData)


def list_of_dormitories():
    '''отдает массив с общагами формат – '''
    pass


def update_number_of_rooms():
    pass


# функции комнаты
def add_room(dormitory, number, capacity):
    db = init_firebase()
    roomData = {'number': number, 'capacity': capacity, 'occupied': 0, 'status': 'Свободна'}
    db.child('dormitory' + str(dormitory)).child('Rooms').child(roomData['number']).set(roomData)


def list_off_all_rooms():
    '''список комнат формата'''
    pass


def update_rooms_status():
    pass


# функции студента
def add_student(fio, phone, passport, address, educ_form, gender, dormitory):
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната':'queue', 'Общежитие':dormitory}

    fio_mas = student_data['ФИО'].split()
    name_tag = fio_mas[0] + fio_mas[1][0] + fio_mas[2][0]
    # добавление в бд
    db.child('clients').child(name_tag).set(student_data)

# добавить в бомжатник

def edit_student():
    # = найти, удалить добавить
    pass


def delete_student_by_fio(fio):
    '''удаление студента'''
    db = init_firebase()


def search_student_by_fio(fio):
    """отдает массив формата [(РоманенкоВЮ, {все данные}),(РоманенкоВЮ, {все данные})]"""
    db = init_firebase()
    searched_student_mas = []

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()

    for student in searched_names.each():
        searched_student_mas.append((student.key(), student.val()))
    return searched_student_mas


def list_off_all_students():
    """отдает массив формата [(РоманенкоВЮ, {все данные}),(Заусайлов, {все данные})]"""
    students_mas = []
    db = init_firebase()
    students_data = db.child("clients").get()
    for student in students_data.each():
        students_mas.append((student.key(),student.val()))
    return students_mas




# функции договора



if __name__ == '__main__':
    db = init_firebase()
    print(list_off_all_students())