from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import time

LoginSucces = False

def login():
    LoginSucces = False

    email = ""

    class LoginWin(QWidget):
        def __init__(self):
            super().__init__()

            self.LoginLabel = QtWidgets.QLabel(self)
            self.LoginLabel.setGeometry(QtCore.QRect(160, 0, 101, 41))
            self.setWindowTitle("Login")
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.LoginLabel.setFont(font)
            self.LoginLabel.setObjectName("LoginLabel")
            self.LoginLabel.setText("Login")

            self.EmailLabel = QtWidgets.QLabel(self)
            self.EmailLabel.setGeometry(QtCore.QRect(10, 50, 81, 18))
            self.EmailLabel.setText("E-Mail:")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.EmailLabel.setFont(font)
            self.EmailLabel.setObjectName("EmailLabel")

            self.PassLabel = QtWidgets.QLabel(self)
            self.PassLabel.setGeometry(QtCore.QRect(10, 80, 81, 18))
            self.PassLabel.setText("Passwort:")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.PassLabel.setFont(font)
            self.PassLabel.setObjectName("PassLabel")

            self.EmailEntry = QtWidgets.QLineEdit(self)
            self.EmailEntry.setGeometry(QtCore.QRect(120, 50, 271, 21))
            self.EmailEntry.setObjectName("EmailEntry")

            self.PassEntry = QtWidgets.QLineEdit(self)
            self.PassEntry.setGeometry(QtCore.QRect(120, 80, 271, 21))
            self.PassEntry.setObjectName("PassEntry")
            
            self.LoginButton = QtWidgets.QPushButton(self)
            self.LoginButton.setGeometry(QtCore.QRect(130, 110, 251, 34))
            self.LoginButton.setText("Login")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.LoginButton.setFont(font)
            self.LoginButton.setObjectName("LoginButton")
            self.LoginButton.clicked.connect(lambda: self.checkLogin())

            self.RegButton = QtWidgets.QPushButton(self)
            self.RegButton.setGeometry(QtCore.QRect(0, 110, 101, 34))
            self.RegButton.setText("Register")
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.RegButton.setFont(font)
            self.RegButton.setObjectName("RegButton")
            self.RegButton.clicked.connect(lambda: self.signup())
            
            
            self.show()

            LoginSucces = False
        
        def checkLogin(self):
            file = open("emails.txt", "r")
            self.EmailList = []
            self.PassList = []
            email = self.EmailEntry.text()
            password = self.PassEntry.text()
            
            for line in file.readlines():
                self.komma = line.find(",")
                self.komma1 = self.komma + 1
                if line[-1] == "\n":
                    self.EmailList.append(line[:self.komma])
                    self.PassList.append(line[self.komma1:-1])
                else:
                    self.EmailList.append(line[:self.komma])
                    self.PassList.append(line[self.komma1:])
            
            
            try:
                self.index = self.EmailList.index(self.email)
                if self.password == self.PassList[self.index]:
                    LoginSucces = True 
                    main.show()
                    print("Succes")           
                    self.close()
                else:
                    self.WrongData = QtWidgets.QLabel(self)
                    self.WrongData.setGeometry(QtCore.QRect(280, 10, 111, 21))
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    font.setBold(True)
                    font.setWeight(75)
                    self.WrongData.setFont(font)
                    self.WrongData.setObjectName("WrongData")


            except:
                self.WrongData = QtWidgets.QLabel(self)
                self.WrongData.setGeometry(QtCore.QRect(280, 10, 111, 21))
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setBold(True)
                font.setWeight(75)
                self.WrongData.setFont(font)
                self.WrongData.setObjectName("WrongData")
        
        def signup(self):
            SignUpSucces = False
            signwin = SignUpWin()
            self.close()             


    class SignUpWin(QWidget):
        def __init__(self):
            super().__init__()

            self.newEmailLabel = QtWidgets.QLabel(self)
            self.newEmailLabel.setGeometry(QtCore.QRect(30, 40, 58, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.newEmailLabel.setFont(font)
            self.newEmailLabel.setObjectName("newEmailLabel")
            self.newEmailLabel.setText("E-Mail")

            self.newPassLabel = QtWidgets.QLabel(self)
            self.newPassLabel.setGeometry(QtCore.QRect(10, 70, 81, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.newPassLabel.setFont(font)
            self.newPassLabel.setObjectName("newPassLabel")
            self.newPassLabel.setText("Passwort")

            self.newEmailEntry = QtWidgets.QLineEdit(self)
            self.newEmailEntry.setGeometry(QtCore.QRect(100, 40, 271, 21))
            self.newEmailEntry.setObjectName("newEmailEntry")

            self.newPassEntry = QtWidgets.QLineEdit(self)
            self.newPassEntry.setGeometry(QtCore.QRect(100, 70, 271, 21))
            self.newPassEntry.setObjectName("newPassEntry")

            self.newPassEntry_2 = QtWidgets.QLineEdit(self)
            self.newPassEntry_2.setGeometry(QtCore.QRect(100, 100, 271, 21))
            self.newPassEntry_2.setObjectName("newPassEntry_2")

            self.newPassLabel_2 = QtWidgets.QLabel(self)
            self.newPassLabel_2.setGeometry(QtCore.QRect(10, 100, 81, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.newPassLabel_2.setFont(font)
            self.newPassLabel_2.setObjectName("newPassLabel_2")
            self.newPassLabel_2.setText("Confirm")
            
            self.titleLabel = QtWidgets.QLabel(self)
            self.titleLabel.setGeometry(QtCore.QRect(160, 10, 81, 18))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.titleLabel.setFont(font)
            self.titleLabel.setObjectName("titleLabel")
            self.titleLabel.setText("Sign Up")

            self.regButton = QtWidgets.QPushButton(self)
            self.regButton.setGeometry(QtCore.QRect(130, 140, 201, 34))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.regButton.setFont(font)
            self.regButton.setObjectName("regButton")
            self.regButton.setText("Register")
            self.regButton.clicked.connect(lambda: self.confirm())

            self.regButton_2 = QtWidgets.QPushButton(self)
            self.regButton_2.setGeometry(QtCore.QRect(0, 140, 88, 34))
            self.regButton_2.setObjectName("regButton_2")
            self.regButton_2.setText("Login")

            self.show()

        def confirm(self):
            file = open("emails.txt", "a")
            if self.newPassEntry.text() == self.newPassEntry_2.text():
                self.newEmail = self.newEmailEntry.text()
                self.newPass = self.newPassEntry.text()
                file.write(f"\n{self.newEmail},{self.newPass}")
                SignUpSucces = True
                loginwin = LoginWin()
                self.close()
            else:
                print("Unsuccesfull")
                


    class mainWin(QWidget):
        def __init__(self):
            super().__init__()
            self.window = QtWidgets.QMainWindow()
            loginwin = LoginWin()
            self.setWindowTitle("ToDo App")

            self.TitleLabel = QtWidgets.QLabel(self)
            self.TitleLabel.setGeometry(QtCore.QRect(290, 20, 161, 18))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.TitleLabel.setFont(font)
            self.TitleLabel.setObjectName("TitleLabel")
            self.TitleLabel.setText("Deine Todos:")

            self.Todo1 = QtWidgets.QLabel(self)
            self.Todo1.setGeometry(QtCore.QRect(40, 60, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo1.setFont(font)
            self.Todo1.setObjectName("Todo1")

            self.Todo8 = QtWidgets.QLabel(self)
            self.Todo8.setGeometry(QtCore.QRect(40, 270, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo8.setFont(font)
            self.Todo8.setObjectName("Todo8")

            self.Todo7 = QtWidgets.QLabel(self)
            self.Todo7.setGeometry(QtCore.QRect(40, 240, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo7.setFont(font)
            self.Todo7.setObjectName("Todo7")

            self.Todo6 = QtWidgets.QLabel(self)
            self.Todo6.setGeometry(QtCore.QRect(40, 210, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo6.setFont(font)
            self.Todo6.setObjectName("Todo6")

            self.Todo5 = QtWidgets.QLabel(self)
            self.Todo5.setGeometry(QtCore.QRect(40, 180, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo5.setFont(font)
            self.Todo5.setObjectName("Todo5")

            self.Todo4 = QtWidgets.QLabel(self)
            self.Todo4.setGeometry(QtCore.QRect(40, 150, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo4.setFont(font)
            self.Todo4.setObjectName("Todo4")

            self.Todo3 = QtWidgets.QLabel(self)
            self.Todo3.setGeometry(QtCore.QRect(40, 120, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo3.setFont(font)
            self.Todo3.setObjectName("Todo3")

            self.Todo2 = QtWidgets.QLabel(self)
            self.Todo2.setGeometry(QtCore.QRect(40, 90, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo2.setFont(font)
            self.Todo2.setObjectName("Todo2")

            self.Todo9 = QtWidgets.QLabel(self)
            self.Todo9.setGeometry(QtCore.QRect(40, 300, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo9.setFont(font)
            self.Todo9.setObjectName("Todo9")

            self.Todo11 = QtWidgets.QLabel(self)
            self.Todo11.setGeometry(QtCore.QRect(40, 360, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo11.setFont(font)
            self.Todo11.setObjectName("Todo11")

            self.Todo12 = QtWidgets.QLabel(self)
            self.Todo12.setGeometry(QtCore.QRect(40, 390, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo12.setFont(font)
            self.Todo12.setObjectName("Todo12")

            self.Todo13 = QtWidgets.QLabel(self)
            self.Todo13.setGeometry(QtCore.QRect(40, 420, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo13.setFont(font)
            self.Todo13.setObjectName("Todo13")

            self.Todo15 = QtWidgets.QLabel(self)
            self.Todo15.setGeometry(QtCore.QRect(40, 480, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo15.setFont(font)
            self.Todo15.setObjectName("Todo15")

            self.Todo14 = QtWidgets.QLabel(self)
            self.Todo14.setGeometry(QtCore.QRect(40, 450, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo14.setFont(font)
            self.Todo14.setObjectName("Todo14")

            self.Todo10 = QtWidgets.QLabel(self)
            self.Todo10.setGeometry(QtCore.QRect(40, 330, 401, 18))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.Todo10.setFont(font)
            self.Todo10.setObjectName("Todo10")
        
        def checkTodos(self):
            userfile = open(f"userfiles/{email}.txt", "r")

            self.todolist = []

            for line in range(userfile.readlines()):
                self.todolist.append(userfile[line])
            
            for x in range(self.todolist):
                if x == 1:
                    self.Todo1.setText(self.todolist[0])
                elif x == 2:
                    self.Todo2.setText(self.todolist[1])
                elif x == 3:
                    self.Todo2.setText(self.todolist[2])
                elif x == 4:
                    self.Todo2.setText(self.todolist[3])
                elif x == 5:
                    self.Todo2.setText(self.todolist[4])
                elif x == 6:
                    self.Todo2.setText(self.todolist[5])
                elif x == 7:
                    self.Todo2.setText(self.todolist[6])
                elif x == 8:
                    self.Todo2.setText(self.todolist[7])
                elif x == 9:
                    self.Todo2.setText(self.todolist[8])
                elif x == 10:
                    self.Todo2.setText(self.todolist[9])
                elif x == 11:
                    self.Todo2.setText(self.todolist[10])
                elif x == 12:
                    self.Todo2.setText(self.todolist[11])
                elif x == 13:
                    self.Todo2.setText(self.todolist[12])
                elif x == 14:
                    self.Todo2.setText(self.todolist[13])
                elif x == 15:
                    self.Todo2.setText(self.todolist[14])
                

        

    app = QApplication(sys.argv)
    main = mainWin()
    sys.exit(app.exec_())


login()
