from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtGui import QCursor

class Dialog(QtWidgets.QDialog):
    def __init__(self, main, parent=None):
        super(Dialog, self).__init__(parent)
        self.main = main
        self.btn_add = QtWidgets.QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_rows)
        layout = QtWidgets.QGridLayout(self)
        self.line_edits = []  # Список для хранения экземпляров QLineEdit
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('hum_res.db')
        if not db.open():
            print("Не удалось установить соединение с базой данных.")
            # Обработка ошибки
        else:
            # Получение названий столбцов из базы данных
            table = status.tableName()
            query = QSqlQuery(f"PRAGMA table_info({table})")  # Замените "employee" на имя вашей таблицы
            i = 1
            while query.next():
                if query.value(1) != "id":
                    label = QtWidgets.QLabel(f'Введите {query.value(1)}:')
                    line = QtWidgets.QLineEdit()
                    layout.addWidget(label, i, 1, 1, 1)
                    layout.addWidget(line, i, 2, 1, 1)
                    self.line_edits.append(line)  # Добавляем экземпляр QLineEdit в список
                    i += 1
            layout.addWidget(self.btn_add, i, 2, 1, 1)

    def add_rows(self):
        values = [line.text() for line in self.line_edits]  # Получаем значения из QLineEdit
        # Теперь у вас есть список значений из QLineEdit, который вы можете использовать по вашему усмотрению
        #print("Введенные значения:", values)
        self.main.add_r(values)
        self.close()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global status
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(600)
        MainWindow.setFixedWidth(900)
        MainWindow.setStyleSheet("background:rgb(47, 150, 171)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.frame.setStyleSheet("border: 4px solid \'#FFFFFF\';\n"
                                 "border-radius: 15px;\n"
                                 "margin: 10px;\n"
                                 "background: #FFFFFF")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 861, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 172, 235), stop:1 rgba(109, 20, 184));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;\n"
            "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 172, 235), stop:1 rgba(109, 20, 184));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget)

        #self.comboBox = QComboBox(self.centralwidget)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("hum_res.db")
        if not db.open():
            print("Unable to open database")
            sys.exit(1)

        tables = db.tables()
        self.pushButton_4.clear()
        self.pushButton_4.addItems(tables)


        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 172, 235), stop:1 rgba(109, 20, 184));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;\n"
            "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(  # "appearance: none;\n"
            "border: 0;\n"
            "border-radius: 15px;\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 172, 235), stop:1 rgba(109, 20, 184));\n"
            "color: #FFFFFF;\n"
            "padding: 8px 16px;\n"
            "font-size: 16px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableView(self.frame)  # QTableView  !!!
        status = QSqlTableModel()
        status.setTable(self.pushButton_4.currentText())
        status.select()
        self.tableWidget.setModel(status)

        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 830, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(830, 351))
        self.tableWidget.setMaximumSize(QtCore.QSize(811, 351))
        self.tableWidget.setStyleSheet("border: 4px solid \'#2DACEB\';\n"
                                       "border-radius: 15px;\n"
                                       "margin: 10px;\n"
                                       "background: #FFFFFF")
        self.tableWidget.setObjectName("tableWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отдел кадров"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить запись"))
        #self.pushButton_4.setText(_translate("MainWindow", "Обновить"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.add_row)
        self.pushButton_4.currentTextChanged.connect(self.updateTable)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('hum_res.db')  # !!! ваша db
        db.open()
        self.dialog = Dialog(self)

    def add_row(self):
        self.dialog.exec_()
    def add_r(self, lst):
        r = status.record()
        table = status.tableName()
        query = QSqlQuery(f"PRAGMA table_info({table})")
        name = []
        while query.next():
            name.append(query.value(1))
        for i in range(len(lst)):
            print(name[i+1], lst[i])
            r.setValue(name[i+1],lst[i])
        status.insertRecord(-1, r)
        status.select()
    def updateTable(self):
        global status
        print(status.tableName())
        print(self.pushButton_4.currentText())
        status.setTable(self.pushButton_4.currentText())
        print(status.tableName())
        status.select()
        self.tableWidget.setModel(status)
    def deleteTable(self):
        db.open()




# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())