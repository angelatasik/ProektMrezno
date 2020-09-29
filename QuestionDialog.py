# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OkClose.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class QuestionDialog(QtWidgets.QDialog):
    def __init__(self, QA):
        super().__init__(parent = None)
        self.q = QA.get("q")
        self.a = QA.get("a")
        self.b = QA.get("b")
        self.c = QA.get("c")
        self.answer = ""
        self.setupUi(self)
    
    def getAnswer(self):
        print("Answered ", self.answer)
        return self.answer

    def accept(self):
        if self.Answer1RadioButton.isChecked():
            self.answer = self.Answer1RadioButton.text()
            self.answerLetter = "a" 
        elif self.Answer2RadioButton.isChecked():
            self.answer = self.Answer2RadioButton.text()
            self.answerLetter = "b" 
        else: 
            self.answer = self.Answer3RadioButton.text()
            self.answerLetter = "c" 

        print("Одговорено: {}) {}\n".format(self.answerLetter,self.answer))
        super().accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("QuestionDialog")
        Dialog.resize(300, 200)
        Dialog.setWindowTitle("Прашање")

        self.QuestionTitleLabel = QtWidgets.QLabel(Dialog)
        self.QuestionTitleLabel.setGeometry(QtCore.QRect(20, 40, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.QuestionTitleLabel.setFont(font)
        self.QuestionTitleLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.QuestionTitleLabel.setObjectName("QuestionTitleLabel")
        self.QuestionTitleLabel.setText(str(self.q))

        self.Answer1RadioButton = QtWidgets.QRadioButton(Dialog)
        self.Answer1RadioButton.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.Answer1RadioButton.setObjectName("Answer1RadioButton")
        self.Answer1RadioButton.setText(str(self.a))

        self.Answer2RadioButton = QtWidgets.QRadioButton(Dialog)
        self.Answer2RadioButton.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.Answer2RadioButton.setObjectName("Answer2RadioButton")
        self.Answer2RadioButton.setText(str(self.b))

        self.Answer3RadioButton = QtWidgets.QRadioButton(Dialog)
        self.Answer3RadioButton.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.Answer3RadioButton.setObjectName("Answer3RadioButton")
        self.Answer3RadioButton.setText(str(self.c))

        self.AcceptButton = QtWidgets.QDialogButtonBox(Dialog)
        self.AcceptButton.setGeometry(QtCore.QRect(30, 150, 200, 32))
        self.AcceptButton.setOrientation(QtCore.Qt.Horizontal)
        self.AcceptButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.AcceptButton.setObjectName("AcceptButton")

        self.AcceptButton.accepted.connect(Dialog.accept)