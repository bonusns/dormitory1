# coding=utf-8
import pyrebase
import random
from PyQt5 import QtCore, QtGui, QtWidgets


def noquote(s):
    """Обновляет модуль pyrebase для работы с нашими данными"""
    return s


pyrebase.pyrebase.quote = noquote


def init_firebase():
    """Подключается к БД"""
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


"""Функции общежития"""


def add_dormitory(number, address):
    """Создает общежитие с 30 комнатами по умолчанию"""
    db = init_firebase()
    dormitoryData = {'number': number, 'rooms': {}, 'name': 'Общежитие ' + str(number), 'Адрес': address}

    check_num = db.child("dormitories").order_by_key().equal_to("dormitory" + str(number)).get().each()
    if check_num == [] and check_num != '' and check_num != '0':
        db.child("dormitories").child('dormitory' + str(number)).set(dormitoryData)
        dorm_num = number
        for number in range(100, 106):
            capacity = random.randint(2, 3)
            room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                         'residents': {}}
            db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

        for number in range(200, 206):
            capacity = random.randint(2, 3)
            room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                         'residents': {}}
            db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

        for number in range(300, 306):
            capacity = random.randint(2, 3)
            room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                         'residents': {}}
            db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

        for number in range(400, 406):
            capacity = random.randint(2, 3)
            room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                         'residents': {}}
            db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

        for number in range(500, 506):
            capacity = random.randint(2, 3)
            room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                         'residents': {}}
            db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)
    else:
        c = 0
        return c


def list_of_dormitories():
    """отдает массив формата [(dormitory$, {все данные}),(dormitory$, {все данные})]"""
    dormitory_mas = []
    db = init_firebase()
    dormitories_data = db.child("dormitories").get()
    for dormitory in dormitories_data.each():
        if "buffer" not in dormitory.key() and "contract_buffer" not in dormitory.key() and "queue" not in dormitory.key():
            dormitory_mas.append((dormitory.key(), dormitory.val()))
    return dormitory_mas


def update_number_of_rooms(dormitory="all"):
    """обновляет поле количество комнат в общежитии"""
    db = init_firebase()
    if dormitory != "all":
        pass
    else:
        for dormitory in range(1, 4):
            n_room = 0
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                n_room += 1
            db.child("dormitories").child("dormitory" + str(dormitory)).update({"number_of_rooms": n_room - 1})


"""Функции комнаты"""


def add_room(dormitory, number, capacity):
    """Добавляет комнату"""
    db = init_firebase()
    room_list = list_of_room_num(dormitory)
    if str(number) not in room_list:
        roomData = {'number': int(number), 'capacity': capacity, 'occupied': 0, 'status': 'свободна', 'gender': ''}
        db.child("dormitories").child('dormitory' + str(dormitory)).child('rooms').child(int(number)).set(roomData)


def remove_room(dormitory, room):
    """Удаляет комнату"""
    db = init_firebase()
    # чуваков в очередь
    room_data = search_room(dormitory, room)
    if "members" not in room_data:
        db.child("dormitories").child('dormitory' + str(dormitory)).child('rooms').child(room).remove()


def list_of_all_rooms(dormitory="all"):
    """
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    dorm_data = list_of_dormitories()
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, len(dorm_data) + 1):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def list_of_empty_rooms(dormitory="all"):
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


def list_of_empty_rooms_by_sex(sex, dormitory="all"):
    """отдает список свободных комнат
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            if room.key() != "queue":
                if room.val()["status"] == "свободна" and (room.val()["gender"] == sex or room.val()["gender"] == ""):
                    room_mas.append((dormitory, room.key(), room.val()))

    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                if room.key() != "queue":
                    if room.val()["status"] == "свободна" and (
                            room.val()["gender"] == sex or room.val()["gender"] == ""):
                        room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def update_rooms_status(dormitory, room):
    """обновляет статус комнаты"""
    room_mas = []
    db = init_firebase()
    room_data = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).get()
    if room_data.val()["occupied"] == room_data.val()["capacity"]:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"status": "занята"})
    else:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"status": "свободна"})


def update_room_occupied(dormitory, room):
    """обновляет поле занятость в комнате"""
    db = init_firebase()
    room_mas = []
    room_data = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(int(room)).get()
    if "members" in room_data.val():
        current_occupied = len(room_data.val()["members"])
    else:
        current_occupied = 0
    db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(int(room)).update(
        {"occupied": current_occupied})
    update_rooms_status(dormitory, room)


def update_room_gender(dormitory, room, sex=None):
    """обновляет поле пола в комнате"""
    db = init_firebase()
    if sex:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update({"gender": sex})
    else:
        room_data = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).get()
        if "members" not in room_data.val():
            sex = ''
            db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
                {"gender": sex})


def edit_room(dormitory, room, capacity=None, gender=None, occupied=0):
    """изменяет комнату"""
    db = init_firebase()
    if capacity:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"capacity": capacity})
    if gender:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"gender": gender})
    if occupied:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"occupied": occupied})


def search_room(dormitory, room):
    """Отдает OrderedDict([('capacity', 3), ('gender', 'Мужской'), ('members', {'-MOSEAzqRcR2X04yWBSB': True}), ('number', 100), ('occupied', 1), ('status', 'свободна')])"""
    db = init_firebase()
    room_data = db.child("dormitories").child('dormitory' + str(dormitory)).child('rooms').child(room).get()
    return room_data.val()


def list_of_room_num(dormitory):
    """Возвращет список номеров комнат"""
    db = init_firebase()
    room_mas = []
    rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
    for room in rooms.each():
        room_mas.append(room.key())
    return room_mas


"""Функции студента"""


def add_student(fio, phone, passport, address, educ_form, gender, dormitory=0):  # dormitory = 0
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': 'queue', 'Общежитие': dormitory}

    # добавление в бд клиентов
    key = db.generate_key()
    db.child('clients').child(key).set(student_data)

    if dormitory == '':
        db.child("dormitories").child("queue").child(key).set({"ФИО": fio})
    elif dormitory == -1:
        db.child("dormitories").child("buffer").child(key).set(student_data)
    else:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child("queue").child(key).set(
            {"ФИО": fio})
    return key


def add_student_buffer(student_id, fio, phone, passport, address, educ_form, gender, room, dormitory):
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': room, 'Общежитие': dormitory, }

    # добавление в бд клиентов
    db.child("dormitories").child("buffer").child(student_id).set(student_data)


def edit_student(student_id, room, fio, phone, passport, address, educ_form, gender, hostel):
    """Ecли какой-то параметр меняется его передаешь в формате fio = изменения, если нет то не указываешь"""
    db = init_firebase()
    hostel_old = db.child("clients").child(student_id).child('Общежитие').get().val()
    #  if fio:
    db.child("clients").child(student_id).update({"ФИО": fio})

    #  if phone:
    db.child("clients").child(student_id).update({"Телефон": phone})
    #   if passport:
    db.child("clients").child(student_id).update({"Паспорт": passport})
    #   if address:
    db.child("clients").child(student_id).update({"Адрес регистрации": address})

    # if educ_form:
    db.child("clients").child(student_id).update({"Форма обучения": educ_form})
    #  if gender:
    db.child("clients").child(student_id).update({"Пол": gender})
    # if hostel:
    # if room !='' and room !="dormitory" + str(hostel) + "/" + "rooms" + "/" + "queue":
    #     db.child("dormitories").child(room).child(student_id).remove()
    if hostel_old != '' and hostel != 'queue':
        db.child("dormitories").child("dormitory" + str(hostel_old)).child("rooms").child("queue").child(
            student_id).remove()
    else:
        db.child("dormitories").child("queue").child(student_id).remove()
    if hostel != '' and hostel != 'queue':
        db.child("dormitories").child("dormitory" + str(hostel)).child("rooms").child("queue").child(student_id).set(
            {"ФИО": fio})
    else:
        db.child("dormitories").child("queue").child(student_id).set({"ФИО": fio})
    db.child("clients").child(student_id).update({"Общежитие": hostel})


def delete_student(student_id, room):
    """удаление студента"""
    db = init_firebase()
    room_old = search_student_by_id(student_id)[1]["Комната"]
    dormitory = search_student_by_id(student_id)[1]["Общежитие"]
    sex = search_student_by_id(student_id)[1]["Пол"]

    db.child("clients").child(student_id).remove()
    db.child("dormitories").child(room).remove()
    # добавить удаление из комнаты
    if room_old != 'queue' and room_old != '':
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room_old).child(
            "members").child(
            student_id).remove()
        update_room_occupied(dormitory, room_old)
        update_room_gender(dormitory, room_old)


def search_student_by_fio(fio):
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    db = init_firebase()
    searched_student_mas = []

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()

    for student in searched_names.each():
        searched_student_mas.append((student.key(), student.val()))
    return searched_student_mas


def search_student_by_code(code):
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    student_mas = []
    db = init_firebase()
    students = db.child("clients").get()

    for student in students.each():
        if "Договор" in student.val():
            if code == student.val()["Договор"]["Шифр"]:
                student_mas.append((student.key(), student.val(), student.val()["Договор"]["Шифр"]))
    return student_mas


def search_student_by_id(student_id):
    """отдает массив формата (id,{все данные})"""
    db = init_firebase()
    student_data = db.child("clients").order_by_key().equal_to(student_id).get()
    for student in student_data.each():
        student_mas = (student.key(), student.val())
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
    """Удаляет студента из очереди"""
    db = init_firebase()
    student = search_student_by_id(student_id)
    dormitory = student[1]["Общежитие"]
    if dormitory == 0 or '':
        db.child("dormitories").child("queue").child(student_id).remove()
    else:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child("queue").child(
            student_id).remove()


def delete_buffer():
    """Удаляет буффер клиента"""
    db = init_firebase()
    db.child("dormitories").child("buffer").remove()


def buffer():
    """буфер, от сюда собственно и происходит закачка в red_client_2"""
    buffer_mas = []
    db = init_firebase()
    students_data = db.child("dormitories").child("buffer").get()
    for student in students_data.each():
        buffer_mas.append((student.key(), student.val()))
    return buffer_mas


def get_students_contract_num(student_id):
    """Отдает номер договора по id_студента"""
    code = []
    db = init_firebase()
    code = ""
    student = search_student_by_id(student_id)
    if student != [] and student != "":
        if "Договор" in student[1]:
            code = student[1]["Договор"]["Шифр"]
        else:
            code = "ОБ - " + str(get_last_contract_num() + 1)
    return code


def get_fio_by_student_id(student_id):
    """Возвращает ФИО студента по его id"""
    db = init_firebase()
    student = search_student_by_id(student_id)
    fio = student[1]["ФИО"]
    return fio


def try_get_fio(fio):
    """Если ФИО состоит из 2х 3х слов возвращает 1"""
    try:
        c = 0
        mas = fio.split()
        if 2 <= len(mas) <= 3:
            for elem in mas:

                for let in elem:
                    if let in "1234567890":
                        c = 1

        else:
            c = 1

    except:
        c = 1
    return c


def try_get_hostel(hostel):
    "Если хостел не пустая строка возвращает 1"

    if hostel != '':
        d = 0
    else:
        d = 1

    return d


"""Функции договора"""


def add_empty_contract(student_id):
    """создает пустой договор, тогда когда мы редактируем договор клиента у которого его нет """
    db = init_firebase()
    last_num = get_last_contract_num()
    code = "ОБ - " + str(last_num + 1)
    contract_data = {"Шифр": code}
    db.child("clients").child(student_id).child("Договор").set(contract_data)
    return code


def add_contract(student_id, date_start, date_end, room, cost, facility, sex, code=None):
    """Вносит изменения в договор если такие имеются"""
    db = init_firebase()
    last_num = get_last_contract_num()

    contract_data = {"Шифр": code, "Дата начала": date_start, "Дата конца": date_end, "Стоимость": cost,
                     "Льгота": facility}
    db.child("clients").child(student_id).child("Договор").set(contract_data)

    dormitory = search_student_by_id(student_id)[1]["Общежитие"]

    # удаляем человека из очереди или старой комнаты
    student = search_student_by_id(student_id)
    room_old = student[1]["Комната"]
    if room_old == "queue" or room_old == "":
        # удаляем человека из очереди
        remove_student_from_queue(student_id)
    else:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room_old).child(
            "members").child(student_id).remove()
        remove_student_from_queue(student_id)
    # Обновляем комнаты
    db.child("clients").child(student_id).update({"Комната": room})
    db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).child("members").child(
        student_id).set(True)
    if room_old != "queue" and room_old != "":
        update_room_occupied(dormitory, room_old)
        update_room_gender(dormitory, room_old)
    update_room_occupied(dormitory, room)
    update_room_gender(dormitory, room, sex)
    if code[5:] == str(last_num + 1):
        update_last_contract_num(last_num + 1)


def add_contract_buffer(student_id, fio, date_start, date_end, room, cost, facility, code=None):
    """Добавляет договор в буффер"""
    db = init_firebase()
    last_num = get_last_contract_num()

    if code != '':

        contract_data = {"ФИО": fio, "Шифр": code, "Дата начала": date_start, "Дата конца": date_end, "Стоимость": cost,
                         "Льгота": facility, "Комната": room}
        db.child("dormitories").child("contract_buffer").child(student_id).set(contract_data)
    else:
        code = add_empty_contract(student_id)
        contract_data = {"ФИО": fio, "Шифр": code, "Дата начала": date_start, "Дата конца": date_end, "Стоимость": cost,
                         "Льгота": facility, "Комната": room}
        db.child("dormitories").child("contract_buffer").child(student_id).set(contract_data)


def get_last_contract_num():
    """отдает номер последнего договора"""
    db = init_firebase()
    last_num = db.child("last_contract_num").get()
    return last_num.val()


def update_last_contract_num(num):
    """обновляет последний номер договора"""
    db = init_firebase()
    db.update({"last_contract_num": num})


def contract_buffer():
    """буфер, от сюда собственно и происходит закачка в red_client_2"""
    buffer_mas = []
    db = init_firebase()
    contract_data = db.child("dormitories").child("contract_buffer").get()
    for contract in contract_data.each():
        buffer_mas.append((contract.key(), contract.val()))
    return buffer_mas


def delete_contract_buffer():
    """Удаляет буффер договора"""
    db = init_firebase()
    db.child("dormitories").child("contract_buffer").remove()


def delite_contract(student_id):
    '''удаление контракта'''
    db = init_firebase()
    db.child("clients").child(student_id).child("Договор").remove()
    dormitory = search_student_by_id(student_id)[1]["Общежитие"]
    room = search_student_by_id(student_id)[1]["Комната"]
    sex = search_student_by_id(student_id)[1]["Пол"]
    db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).child("members").child(
        student_id).remove()
    db.child("dormitories").child("queue").child(student_id).set({"ФИО": search_student_by_id(student_id)[1]["ФИО"]})
    db.child("clients").child(student_id).update({"Комната": ""})
    db.child("clients").child(student_id).update({"Общежитие": ""})
    update_room_occupied(dormitory, room)
    update_room_gender(dormitory, room)

    # db.child("dormitories").child(room).remove()


def edit_contract(code, date_start=None, date_end=None, room=None, cost=None, facility=None):
    """Вносит изменения в договор если такие имеются"""
    db = init_firebase()
    last_num = get_last_contract_num()
    contract = search_contract_by_code(code)
    student_id = contract[0]
    dormitory = contract[1]
    student = search_student_by_id(student_id)
    room_old = student[1]["Комната"]
    sex = student[1]["Пол"]

    if date_start:
        db.child("clients").child(student_id).child("Договор").update({"Дата начала": date_start})
    if date_end:
        db.child("clients").child(student_id).child("Договор").update({"Дата конца": date_end})
    if room:
        db.child("clients").child(student_id).update({"Комната": room})
        if room_old == "queue":
            # удаляем человека из очереди
            remove_student_from_queue(student_id)
        else:
            db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room_old).child(
                "members").child(student_id).remove()
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).child("members").child(
            student_id).set(True)

        if room_old != "queue" and room_old != "":
            update_room_gender(dormitory, room_old)
            update_room_occupied(dormitory, room_old)
        update_room_occupied(dormitory, room)
        update_room_gender(dormitory, room, sex)
    if cost:
        db.child("clients").child(student_id).child("Договор").update({"Стоимость": str(cost)})
    if facility:
        db.child("clients").child(student_id).child("Договор").update({"Льгота": str(facility)})
    if code[5:] == str(last_num + 1):
        update_last_contract_num(last_num + 1)


def search_contract_by_code(code):
    """возвращает данные формата (id_студента, номер общаги, {данные договора}"""
    student_mas = []
    db = init_firebase()
    students = db.child("clients").get()

    for student in students.each():
        if "Договор" in student.val():
            if code == student.val()["Договор"]["Шифр"]:
                student_mas = (student.key(), student.val()["Общежитие"], student.val()["Договор"])
    return student_mas


def list_of_contracts():
    """возвращает данные формата [(id_студента, номер общаги, {данные договора}),(id_студента, номер общаги, {данные договора})] """
    last_num = get_last_contract_num()
    contract_mas = []
    for contract_num in range(1, last_num + 1):
        contract = search_contract_by_code("ОБ - " + str(contract_num))
        if contract != []:
            contract_mas.append(contract)

    return contract_mas


def get_students_contract_num2(student_id):
    """Отдает номер договора студента или пустую строку, если его нет"""
    code = []
    db = init_firebase()
    code = ""
    student = search_student_by_id(student_id)
    if student != [] and student != "":
        if "Договор" in student[1]:
            code = student[1]["Договор"]["Шифр"]
        else:
            code = ""
    return code


"""функции льгот/стоимостей"""


def add_facility(name, cost):
    """Добавляет новую льготу"""
    db = init_firebase()
    db.child("facilities").child(name).set({"Название": name, "Стоимость": cost})


def remove_facility(name):
    """Удаляет общежитие по номеру"""
    db = init_firebase()
    db.child("facilities").child(name).remove()


def edit_facility(name, cost=None):
    """Изменяет поля льгот если такие указаны"""
    db = init_firebase()
    old_name = db.child("facilities").child("buffer").get()
    for names in old_name.each():
        old = names.key()
        db.child("facilities").child(old).remove()
        db.child("facilities").child(name).update({"Название": name})
        db.child("facilities").child(name).update({"Стоимость": cost})
    return old_name


def list_of_facilities():
    """возвращает список формата [('Без льгот', 550), ('Инвалид', 0), ('Сирота', 1), ('ЧАЭС', 0)]"""
    db = init_firebase()
    facilities = db.child("facilities").get()
    fac_mas = []
    i = 0
    for facility in facilities.each():
        fac_mas.append((facility.val()["Название"], facility.val()["Стоимость"]))
        i = i + 1
    return fac_mas, i


def update_facility_data(old_name, new_name=None, new_cost=None):
    """Обновляет значения и названия льгот у всех договоров при изменении"""
    db = init_firebase()
    contract_data = list_of_contracts()
    for contract in contract_data:
        if "Льгота" in contract[2]:
            if contract[2]["Льгота"] == old_name:
                if new_name != "" and new_name:
                    db.child("clients").child(contract[0]).child("Договор").update({"Льгота": new_name})
                if new_cost != "" and new_cost:
                    db.child("clients").child(contract[0]).child("Договор").update({"Стоимость": new_cost})


def check_facility(fac_name):
    """Возвращает True если можно удалить"""
    db = init_firebase()
    contract_mas = list_of_contracts()
    can_delete = True
    if contract_mas != []:
        for contract in contract_mas:
            contract_data = contract[2]
            if contract_data["Льгота"] == fac_name:
                can_delete = False
                break
    return can_delete


"""Функции архива"""


def list_of_archive():
    """[('ФИО', 'Дата начала', 'Дата конца', 'Код'), ('ФИО', 'Дата начала', 'Дата конца', 'Код')]"""
    db = init_firebase()
    archive_mas = []
    archive_data = db.child("archive").get()
    if archive_data.val():
        for code in archive_data.each():
            archive_mas.append(
                (code.val()["ФИО"], code.val()["Дата начала"], code.val()["Дата конца"], code.val()["Шифр"]))
    return archive_mas


def add_to_archive(fio, code, date_start, date_end):
    """Добавляет студента в архив"""
    db = init_firebase()
    archive_data = {"ФИО": fio, "Дата начала": date_start, "Дата конца": date_end, "Шифр": code}
    db.child("archive").child(code).set(archive_data)


if __name__ == '__main__':
    db = init_firebase()
