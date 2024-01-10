# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createNewGame.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateNewGameUI(object):
    def setupUi(self, CreateNewGameUI):
        CreateNewGameUI.setObjectName("CreateNewGameUI")
        CreateNewGameUI.resize(400, 300)
        CreateNewGameUI.setStyleSheet("QDialog{\n"
"background-color:rgb(250, 250, 250)\n"
"}")
        self.createGameButton = QtWidgets.QPushButton(CreateNewGameUI)
        self.createGameButton.setGeometry(QtCore.QRect(150, 230, 91, 51))
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
        self.maxPlayersCountBox = QtWidgets.QSpinBox(CreateNewGameUI)
        self.maxPlayersCountBox.setGeometry(QtCore.QRect(280, 80, 41, 41))
        self.maxPlayersCountBox.setMinimum(2)
        self.maxPlayersCountBox.setMaximum(5)
        self.maxPlayersCountBox.setObjectName("maxPlayersCountBox")
        self.maxRoundsCountBox = QtWidgets.QSpinBox(CreateNewGameUI)
        self.maxRoundsCountBox.setGeometry(QtCore.QRect(280, 150, 41, 41))
        self.maxRoundsCountBox.setMinimum(2)
        self.maxRoundsCountBox.setMaximum(5)
        self.maxRoundsCountBox.setObjectName("maxRoundsCountBox")

        self.retranslateUi(CreateNewGameUI)
        QtCore.QMetaObject.connectSlotsByName(CreateNewGameUI)

    def retranslateUi(self, CreateNewGameUI):
        _translate = QtCore.QCoreApplication.translate
        CreateNewGameUI.setWindowTitle(_translate("CreateNewGameUI", "CreateGame"))
        self.createGameButton.setText(_translate("CreateNewGameUI", "CREATE"))