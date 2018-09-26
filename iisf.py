# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IISF.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import smtplib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 400)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(220, 159, 65, 193), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 20, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.symbol = QtWidgets.QLabel(self.centralwidget)
        self.symbol.setGeometry(QtCore.QRect(0, 70, 221, 221))
        self.symbol.setText("")
        self.symbol.setPixmap(QtGui.QPixmap("../Downloads/download.jpg"))
        self.symbol.setObjectName("symbol")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 250, 111, 41))
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "          E-CHALAN GENERATOR"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "    VEHICLE NUMBER"))
        self.pushButton.setText(_translate("MainWindow", "GENERATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))
    #################
    def send(self):
        iisf=sqlite3.connect("chalan.db")
        cur=iisf.cursor()
        data=self.lineEdit.text()
        sql="select * from vehicle where vehicle_number='"+data+"';"
        x=cur.execute(sql)

        if x!=None:
            y=cur.fetchone()
            try:
                mail="shreshthar.speed17@gmail.com"
                password="tommymyfriend"
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login(mail,password)
                sub="E-CHALAN VEHICLE POLLUTION"
                person=y[2]
                message = "Subject: {}\n Hello {} vehicle number {} model {} producing excesive amount of harmfull gases. \n please submit fine of Rs 1000 to the nearest RTO office or police station. \n Thank You \n RTO office".format(sub,y[1],y[0],y[3])
                server.sendmail(mail,person,message)
                server.quit()
                print("CHALAN SEND")
            except:
                print("VEHICLE NOT REGISTERED")
#########################3

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

