from dormitory.database import *


def init_room():
    for dorm_num in range(1, 4):
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

if __name__ == '__main__':
    db = init_firebase(firebaseConfig)
    number = 'queue'
    room_data = {number: {'capacity': 0, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                          'residents':{}}}

    for number in range(1, 4):

        name = 'dormitory' + str(number)
        dormitory_data = {'number': number, 'rooms': room_data, 'name': 'Общежитие ' + str(number), 'number_of_rooms': 0}
        db.child('dormitories').child(name).set(dormitory_data)

    fio = 'Романенко Владимир Юрьевич'
    contract_data = {'code': ' ', 'start_date': 0, 'ending date': 0}
    client_data = {'fio':fio,'dormitory': 0, 'room_number': 0, 'contract': contract_data, 'address': '', 'phone_number': ' ',
               'gender': ' ', 'passport': ' ', 'education_form': ' '}
    mas = fio.split()
    fio = mas[0]+mas[1][0]+mas[2][0]
    db.child('clients').child(fio).set(client_data)



    init_room()