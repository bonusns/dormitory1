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
def add_dormitory(number, address):
    db = init_firebase()
    dormitoryData = {'number': number, 'Rooms': {0: ''}, 'name': 'Общежитие ' + str(number), 'Адрес': address}
    db.child('dormitory' + str(number)).set(dormitoryData)


def list_of_dormitories():
    '''отдает массив с общагами формат – '''
    dormitory_mas = []
    db = init_firebase()
    dormitories_data = db.child("dormitories").get()
    for dormitory in dormitories_data.each():
        dormitory_mas.append((dormitory.key(), dormitory.val()))
    return dormitory_mas


def update_number_of_rooms(dormitory = "all"):
    db = init_firebase()
    if dormitory != "all":
        pass
    else:
        for dormitory in range(1,4):
            n_room = 0
            rooms = db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").get()
            for room in rooms.each():
                n_room += 1
            db.child("dormitories").child("dormitory"+str(dormitory)).update({"number_of_rooms":n_room-1})


# функции комнаты
def add_room(dormitory, number, capacity):
    db = init_firebase()
    roomData = {'number': number, 'capacity': capacity, 'occupied': 0, 'status': 'Свободна'}
    db.child('dormitory' + str(dormitory)).child('Rooms').child(roomData['number']).set(roomData)
    update_number_of_rooms()


def list_of_all_rooms(dormirory):
    """список комнат формата"""
    db = init_firebase()
    if dormirory != "all":
        pass
    else:
        pass

def list_of_empty_rooms(dormirory):
    db = init_firebase()
    if dormirory != "all":
        pass
    else:
        pass


def update_rooms_status(dormirory = "all", room_number = 0):
    pass


# функции студента
def add_student(fio, phone, passport, address, educ_form, gender, dormitory):
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': 'queue', 'Общежитие': dormitory}

    # fio_mas = student_data['ФИО'].split()

    # добавление в бд клиентов
    db.child('clients').push(student_data)
    # добавление заметки в комнату
    """подумать как селить в комнаты"""
    # db.child("dormitories").child("dormitory"+dormitory).child("queue").update({'members':})

    # добавить в бомжатник


def edit_student(student_id):
    pass


def delete_student(student_id):
    '''удаление студента'''
    db = init_firebase()
    db.child("clients").child(student_id).remove()


def search_student_by_fio(fio):
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    db = init_firebase()
    searched_student_mas = []

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()

    for student in searched_names.each():
        searched_student_mas.append((student.key(), student.val()))
    return searched_student_mas


def list_off_all_students():
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    students_mas = []
    db = init_firebase()
    students_data = db.child("clients").get()
    for student in students_data.each():
        students_mas.append((student.key(), student.val()))
    return students_mas


# функции договора

# проверка на дурака

def check_fio(fio):
    pass

def check_phone_number(phone_number):
    pass

#и т.д. уточнить у моситовцев, как пиздато сделать проверку на дурака


if __name__ == '__main__':
    db = init_firebase()
    # add_student("Романенко Владимир Юрьевич","94239423","423423","fdgfdgdf","mgkfdg","male","1")
    # delete_student("-MNV8YOZ6F6Rqrwj5JRa")
    # update_number_of_rooms()