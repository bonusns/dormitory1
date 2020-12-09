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
    """отдает массив формата [(dormitory$, {все данные}),(dormitory$, {все данные})]"""
    dormitory_mas = []
    db = init_firebase()
    dormitories_data = db.child("dormitories").get()
    for dormitory in dormitories_data.each():
        dormitory_mas.append((dormitory.key(), dormitory.val()))
    return dormitory_mas


def update_number_of_rooms(dormitory = "all"):
    """обновляет поле количество комнат в общежитии"""
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
    update_number_of_rooms(str(dormitory))


def list_of_all_rooms(dormitory = "all"):
    """
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def list_of_empty_rooms(dormitory = "all"):
    """отдает список свободных комнат
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            if room.val()["status"] == "свободна":
                room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                if room.val()["status"] == "свободна":
                    room_mas.append((dormitory, room.key(), room.val()))
    return room_mas

def list_of_empty_rooms_by_sex(sex,dormitory = "all"):
    """отдает список свободных комнат
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            if room.val()["status"] == "свободна" and room.val()["gender"] == sex:
                room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                if room.val()["status"] == "свободна" and room.val()["gender"] == sex:
                    room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def update_rooms_status(dormitory = "all", room_number = 0):
    """обновляет статус комнаты"""
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        pass

def update_room_gender(dormitory,room,sex):
    db = init_firebase()
    db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child(room).update({"gender":sex})


# функции студента
def add_student(fio, phone, passport, address, educ_form, gender, dormitory = 0):
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': 'queue', 'Общежитие': dormitory}

    # добавление в бд клиентов
    key = db.generate_key()
    db.child('clients').child(key).set(student_data)

    if dormitory == 0:
        db.child("dormitories").child("queue").child(key).set({"ФИО":fio})
    else:
        db.child("dormitories").child("dormitory"+str(dormitory)).child("queue").child(key).set({"ФИО":fio})


def edit_student(student_id):
    pass


def delete_student(student_id):
    '''удаление студента'''
    db = init_firebase()
    db.child("clients").child(student_id).remove()
    # добавить удаление из комнаты


def search_student_by_fio(fio):
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    db = init_firebase()
    searched_student_mas = []

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()

    for student in searched_names.each():
        searched_student_mas.append((student.key(), student.val()))
    return searched_student_mas

def search_student_by_id(student_id):
    """отдает массив формата (id,{все данные})"""
    db = init_firebase()
    student_data = db.child("clients").order_by_key().equal_to(student_id).get()
    for student in student_data.each():
        student_mas = (student.key(),student.val())
    return student_mas


def list_off_all_students():
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    students_mas = []
    db = init_firebase()
    students_data = db.child("clients").get()
    for student in students_data.each():
        students_mas.append((student.key(), student.val()))
    return students_mas

def remove_student_from_queue(student_id):
    db = init_firebase()
    student = search_student_by_id(student_id)
    dormitory = student[1]["Общежитие"]
    print(dormitory)
    if dormitory == 0:
        db.child("dormitories").child("queue").child(student_id).remove()
    else:
        db.child("dormitories").child("dormitory"+str(dormitory)).child("queue").child(student_id).remove()


"""Функции договора"""

def add_contract(student_id,date_start,date_end,room,cost,sex):
    db = init_firebase()
    last_num = get_last_contract_num()
    code = "ОБ - " + str(last_num + 1 )
    contract_data = {"Шифр":code,"Дата начала":date_start,"Дата_конца":date_end,"Стоимость":cost}
    db.child("clients").child(student_id).child(code).set(contract_data)

    dormitory = search_student_by_id(student_id)[1]["Общежитие"]

    #удаляем человека из очереди
    remove_student_from_queue(student_id)

    #Обновляем комнаты
    db.child("clients").child(student_id).update({"Комната":room})
    db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child(room).update({"members":{student_id:True}})

    update_room_gender(dormitory,room,sex)
    update_last_contract_num(last_num+1)

def get_last_contract_num():
    """отдает номер последнего договора"""
    db = init_firebase()
    last_num = db.child("last_contract_num").get()
    return last_num.val()

def update_last_contract_num(num):
    db = init_firebase()
    db.update({"last_contract_num":num})


# проверка на дурака

def check_fio(fio):
    pass

def check_phone_number(phone_number):
    pass

#и т.д. уточнить у моситовцев, как пиздато сделать проверку на дурака


if __name__ == '__main__':
    db = init_firebase()
    # add_student("Романенко Владимир Юрьевич","94239423","423423","fdgfdgdf","mgkfdg","male","1")
    print(list_off_all_students())
    # st = db.child("clients").order_by_key().equal_to("-MO2ZXoFYxIRHsaST1G6").get()
    # print(st.val())
    # add_contract("-MO2ZXoFYxIRHsaST1G6","11.12.2018","11.12.2020",301,500,"муж")
    # print(search_student_by_id("-MO2ZXoFYxIRHsaST1G6"))
    # delete_student("-MNV8YOZ6F6Rqrwj5JRa")
    # update_number_of_rooms()
    # print(list_of_all_rooms())
    # print(list_of_empty_rooms())ц