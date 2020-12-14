# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_room.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import database as dbd

class Ui_del_room(object):

    def fill_room_data(self,choose_dorm_number):
        self.RoomNumber.clear()
        room_mas = dbd.list_of_all_rooms()
        i = 0
        for room in room_mas:
            dorm_num = room[0]
            if str(dorm_num) == choose_dorm_number:
                room_number = room[1]
                self.RoomNumber.addItem("")
                self.RoomNumber.setItemText(i, f"{room_number}")
                i += 1

    def fill_dorm_data(self):
        dorm_mas = dbd.list_of_dormitories()
        i = 0
        for dorm in dorm_mas:
            self.HostelNumber.addItem("")
            self.HostelNumber.setItemText(i, f"{dorm[1]['number']}")
            i += 1

    def search_room(self):
        room_number = self.RoomNumber.currentText()
        dorm_number = self.HostelNumber.currentText()
        room_data = dbd.search_room(dorm_number,room_number)

        str_student_fio = ""
        if "members" in room_data:
            for student in room_data["members"]:
                str_student_fio += dbd.get_fio_by_student_id(student) + "\n"
        self.Room_list.addItem(f"Общежитие: {dorm_number}; Комната: {room_number}\nВместимость: {room_data['capacity']}; Свободно: {int(room_data['capacity'])-int(room_data['occupied'])}\nЖильцы:\n{str_student_fio}")

    def del_room(self):
        room_number = self.RoomNumber.currentText()
        dorm_number = self.HostelNumber.currentText()
        if self.Room_list.currentRow() != -1:
            room_data = dbd.search_room(dorm_number, room_number)
            if "members" not in room_data:
                dbd.remove_room(dorm_number,room_number)
            else:
                print("Вы не можете удалить пока комната не пуста!")
            self.Room_list.clear()
            self.RoomNumber.clear()


    def openRoom(self):
        from rooms import Ui_Rooms
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rooms()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, del_room):
        del_room.setObjectName("del_room")
        del_room.resize(630, 300)
        del_room.setMinimumSize(QtCore.QSize(630, 300))
        del_room.setMaximumSize(QtCore.QSize(630, 300))
        self.centralwidget = QtWidgets.QWidget(del_room)
        self.centralwidget.setObjectName("centralwidget")
        self.label_room = QtWidgets.QLabel(self.centralwidget)
        self.label_room.setGeometry(QtCore.QRect(60, 80, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_room.setFont(font)
        self.label_room.setAlignment(QtCore.Qt.AlignCenter)
        self.label_room.setObjectName("label_room")
        self.label_hostel = QtWidgets.QLabel(self.centralwidget)
        self.label_hostel.setGeometry(QtCore.QRect(60, 140, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_hostel.setFont(font)
        self.label_hostel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hostel.setObjectName("label_hostel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 20, 431, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.find_room_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.find_room_btn.setMinimumSize(QtCore.QSize(150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.find_room_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.find_room_btn.setFont(font)
        self.find_room_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.find_room_btn.setObjectName("find_room_btn")
        self.horizontalLayout.addWidget(self.find_room_btn)
        self.back_to_rooms_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_rooms_btn.setMinimumSize(QtCore.QSize(150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.back_to_rooms_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_rooms_btn.setFont(font)
        self.back_to_rooms_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_rooms_btn.setObjectName("back_to_rooms_btn")

        self.back_to_rooms_btn.clicked.connect(self.openRoom)
        self.find_room_btn.clicked.connect(self.search_room)


        self.back_to_rooms_btn.clicked.connect(del_room.close)

        self.horizontalLayout.addWidget(self.back_to_rooms_btn)
        self.label_FIO_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_FIO_2.setGeometry(QtCore.QRect(60, 110, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FIO_2.setFont(font)
        self.label_FIO_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FIO_2.setObjectName("label_FIO_2")
        self.del_room_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_room_btn.setGeometry(QtCore.QRect(370, 210, 195, 40))
        self.del_room_btn.setMinimumSize(QtCore.QSize(150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.del_room_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.del_room_btn.setFont(font)
        self.del_room_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.del_room_btn.setObjectName("del_room_btn")
        self.Room_list = QtWidgets.QListWidget(self.centralwidget)
        self.Room_list.setGeometry(QtCore.QRect(60, 200, 240, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.Room_list.sizePolicy().hasHeightForWidth())
        self.Room_list.setSizePolicy(sizePolicy)
        self.Room_list.setMinimumSize(QtCore.QSize(240, 30))
        self.Room_list.setMaximumSize(QtCore.QSize(240, 60))
        self.Room_list.setSizeIncrement(QtCore.QSize(0, 30))
        self.Room_list.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Room_list.setFont(font)
        self.Room_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Room_list.setObjectName("Room_list")
        self.RoomNumber = QtWidgets.QComboBox(self.centralwidget)
        self.RoomNumber.setGeometry(QtCore.QRect(270, 140, 300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.RoomNumber.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.RoomNumber.setFont(font)
        self.RoomNumber.setToolTip("")
        self.RoomNumber.setStatusTip("")
        self.RoomNumber.setStyleSheet("background-color: rgb(135, 206, 235);\n"
"")
        self.RoomNumber.setEditable(False)
        self.RoomNumber.setMaxCount(10)
        self.RoomNumber.setIconSize(QtCore.QSize(16, 16))
        self.RoomNumber.setModelColumn(0)
        self.RoomNumber.setObjectName("RoomNumber")
        self.HostelNumber = QtWidgets.QComboBox(self.centralwidget)
        self.HostelNumber.setGeometry(QtCore.QRect(270, 80, 300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.HostelNumber.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HostelNumber.setFont(font)
        self.HostelNumber.setToolTip("")
        self.HostelNumber.setStatusTip("")
        self.HostelNumber.setStyleSheet("background-color: rgb(135, 206, 235);\n"
"")
        self.HostelNumber.setEditable(False)
        self.HostelNumber.setMaxCount(10)
        self.HostelNumber.setIconSize(QtCore.QSize(16, 16))
        self.HostelNumber.setModelColumn(0)
        self.HostelNumber.setObjectName("HostelNumber")
        # self.HostelNumber.addItem("")
        # self.HostelNumber.addItem("")
        # self.HostelNumber.addItem("")
        # self.HostelNumber.addItem("")
        # self.HostelNumber.addItem("")
        del_room.setCentralWidget(self.centralwidget)

        self.del_room_btn.clicked.connect(self.del_room)

        self.retranslateUi(del_room)
        self.RoomNumber.setCurrentIndex(-1)
        self.HostelNumber.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(del_room)
        self.HostelNumber.activated[str].connect(self.fill_room_data)
        # self.fill_room_data()
        self.fill_dorm_data()

    def retranslateUi(self, del_room):
        _translate = QtCore.QCoreApplication.translate
        del_room.setWindowTitle(_translate("del_room", "Удаление комнаты"))
        self.label_room.setText(_translate("del_room", "Выберите общежитие"))
        self.label_hostel.setText(_translate("del_room", "Комнату"))
        self.find_room_btn.setText(_translate("del_room", "Найти"))
        self.back_to_rooms_btn.setText(_translate("del_room", "Вернуться в меню комнат"))
        self.label_FIO_2.setText(_translate("del_room", "и"))
        self.del_room_btn.setText(_translate("del_room", "Удалить"))
        # self.RoomNumber.setItemText(0, _translate("del_room", "1"))
        # self.RoomNumber.setItemText(1, _translate("del_room", "2"))
        # self.RoomNumber.setItemText(2, _translate("del_room", "3"))
        # self.RoomNumber.setItemText(3, _translate("del_room", "4"))
        # self.RoomNumber.setItemText(4, _translate("del_room", "5"))
        # self.HostelNumber.setItemText(0, _translate("del_room", "1"))
        # self.HostelNumber.setItemText(1, _translate("del_room", "2"))
        # self.HostelNumber.setItemText(2, _translate("del_room", "3"))
        # self.HostelNumber.setItemText(3, _translate("del_room", "4"))
        # self.HostelNumber.setItemText(4, _translate("del_room", "5"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    del_room = QtWidgets.QMainWindow()
    ui = Ui_del_room()
    ui.setupUi(del_room)
    del_room.show()
    sys.exit(app.exec_())
