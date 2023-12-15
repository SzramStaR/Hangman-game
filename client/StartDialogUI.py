# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog - untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(969, 614)
        Dialog.setMinimumSize(QtCore.QSize(969, 614))
        Dialog.setStyleSheet("QDialog{\n"
"background-color:rgb(250, 250, 250)\n"
"}")
        self.nickNameEdit = QtWidgets.QLineEdit(Dialog)
        self.nickNameEdit.setGeometry(QtCore.QRect(320, 180, 311, 51))
        self.nickNameEdit.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(247, 178, 183);\n"
"border-radius: 20px;\n"
"background-color:rgb(250, 250, 250);\n"
"padding-left:20px;\n"
"padding-reght:20px;\n"
"text-color:rgb(78, 78, 78)\n"
"\n"
"}")
        self.nickNameEdit.setText("")
        self.nickNameEdit.setObjectName("nickNameEdit")
        self.gameIdEdit = QtWidgets.QLineEdit(Dialog)
        self.gameIdEdit.setGeometry(QtCore.QRect(300, 360, 191, 51))
        self.gameIdEdit.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(247, 178, 183);\n"
"border-radius: 20px;\n"
"background-color:rgb(250, 250, 250);\n"
"padding-left:20px;\n"
"padding-reght:20px;\n"
"text-color:rgb(78, 78, 78)\n"
"\n"
"}")
        self.gameIdEdit.setText("")
        self.gameIdEdit.setObjectName("gameIdEdit")
        self.joinGameButton = QtWidgets.QPushButton(Dialog)
        self.joinGameButton.setGeometry(QtCore.QRect(540, 360, 91, 51))
        self.joinGameButton.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(247, 178, 183);\n"
"border-radius: 20px;\n"
"background-color:rgb(250, 250, 250);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"\n"
"\n"
"}")
        self.joinGameButton.setObjectName("joinGameButton")
        self.createGameButton = QtWidgets.QPushButton(Dialog)
        self.createGameButton.setGeometry(QtCore.QRect(420, 530, 131, 51))
        self.createGameButton.setStyleSheet("QPushButton{\n"
"border: 2px solid rgb(247, 178, 183);\n"
"border-radius: 20px;\n"
"background-color:rgb(250, 250, 250);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"\n"
"\n"
"}")
        self.createGameButton.setObjectName("createGameButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(230, 10, 481, 151))
        self.widget.setObjectName("widget")
        self.gameTittleImg = QtWidgets.QLabel(self.widget)
        self.gameTittleImg.setGeometry(QtCore.QRect(80, 30, 341, 151))
        self.gameTittleImg.setAutoFillBackground(True)
        self.gameTittleImg.setStyleSheet("background-image: url(:/nowyPrzedrostek/a0e46391894ff0de4550420292842c95.png);")
        self.gameTittleImg.setText("")
        self.gameTittleImg.setTextFormat(QtCore.Qt.PlainText)
        self.gameTittleImg.setScaledContents(True)
        self.gameTittleImg.setObjectName("gameTittleImg")
        self.selectGameIdImg = QtWidgets.QLabel(Dialog)
        self.selectGameIdImg.setGeometry(QtCore.QRect(250, 290, 461, 71))
        self.selectGameIdImg.setAutoFillBackground(True)
        self.selectGameIdImg.setStyleSheet("background-image: url(:/nowyPrzedrostek/select_existing_game.png);")
        self.selectGameIdImg.setText("")
        self.selectGameIdImg.setObjectName("selectGameIdImg")
        self.orCreateNewImg = QtWidgets.QLabel(Dialog)
        self.orCreateNewImg.setGeometry(QtCore.QRect(260, 430, 421, 91))
        self.orCreateNewImg.setAutoFillBackground(True)
        self.orCreateNewImg.setStyleSheet("\n"
"background-image: url(:/nowyPrzedrostek/or_create_new_game.png);")
        self.orCreateNewImg.setText("")
        self.orCreateNewImg.setObjectName("orCreateNewImg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.nickNameEdit.setPlaceholderText(_translate("Dialog", "Type your nickname here"))
        self.gameIdEdit.setPlaceholderText(_translate("Dialog", "Type game ID here"))
        self.joinGameButton.setText(_translate("Dialog", "JOIN"))
        self.createGameButton.setText(_translate("Dialog", "CREATE NEW"))
import images_rc