# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'experimentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import random

from PyQt5 import QtCore, QtGui, QtWidgets


class experimentWindowClass(object):

    def __init__(self):
        self.selector = random.randint(1, 3)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        Form.setFont(font)

        # correct - 2
        if self.selector == 1:
            self.line_1 = QtWidgets.QLabel(Form)
            pixmap1 = QtGui.QPixmap("line_1.jpg.")
            self.line_1.setPixmap(pixmap1)
            self.line_1.setObjectName("line_1")
            self.line_1.setGeometry(QtCore.QRect(40, 170, 30, 190))

            self.line_2 = QtWidgets.QLabel(Form)
            pixmap2 = QtGui.QPixmap("line_2.jpg")
            self.line_2.setPixmap(pixmap2)
            self.line_2.setObjectName("line_2")
            self.line_2.setGeometry(QtCore.QRect(140, 170, 30, 190))

            self.line_3 = QtWidgets.QLabel(Form)
            pixmap3 = QtGui.QPixmap("line_3.jpg")
            self.line_3.setPixmap(pixmap3)
            self.line_3.setObjectName("line_3")
            self.line_3.setGeometry(QtCore.QRect(230, 170, 30, 190))
        # correct - 3
        elif self.selector == 2:
            self.line_1 = QtWidgets.QLabel(Form)
            pixmap1 = QtGui.QPixmap("line_3.jpg.")
            self.line_1.setPixmap(pixmap1)
            self.line_1.setObjectName("line_1")
            self.line_1.setGeometry(QtCore.QRect(40, 170, 30, 190))

            self.line_2 = QtWidgets.QLabel(Form)
            pixmap2 = QtGui.QPixmap("line_1.jpg")
            self.line_2.setPixmap(pixmap2)
            self.line_2.setObjectName("line_2")
            self.line_2.setGeometry(QtCore.QRect(140, 170, 30, 190))

            self.line_3 = QtWidgets.QLabel(Form)
            pixmap3 = QtGui.QPixmap("line_2.jpg")
            self.line_3.setPixmap(pixmap3)
            self.line_3.setObjectName("line_3")
            self.line_3.setGeometry(QtCore.QRect(230, 170, 30, 190))
        # correct - 1
        elif self.selector == 3:
            self.line_1 = QtWidgets.QLabel(Form)
            pixmap1 = QtGui.QPixmap("line_2.jpg.")
            self.line_1.setPixmap(pixmap1)
            self.line_1.setObjectName("line_1")
            self.line_1.setGeometry(QtCore.QRect(40, 170, 30, 190))

            self.line_2 = QtWidgets.QLabel(Form)
            pixmap2 = QtGui.QPixmap("line_3.jpg")
            self.line_2.setPixmap(pixmap2)
            self.line_2.setObjectName("line_2")
            self.line_2.setGeometry(QtCore.QRect(140, 170, 30, 190))

            self.line_3 = QtWidgets.QLabel(Form)
            pixmap3 = QtGui.QPixmap("line_1.jpg")
            self.line_3.setPixmap(pixmap3)
            self.line_3.setObjectName("line_3")
            self.line_3.setGeometry(QtCore.QRect(230, 170, 30, 190))

        self.radioButton_A = QtWidgets.QRadioButton(Form)
        self.radioButton_A.setGeometry(QtCore.QRect(40, 380, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        self.radioButton_A.setFont(font)
        self.radioButton_A.setObjectName("radioButton_C")
        self.radioButton_B = QtWidgets.QRadioButton(Form)
        self.radioButton_B.setGeometry(QtCore.QRect(140, 380, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        self.radioButton_B.setFont(font)
        self.radioButton_B.setObjectName("radioButton_B")
        self.radioButton_C = QtWidgets.QRadioButton(Form)
        self.radioButton_C.setGeometry(QtCore.QRect(230, 380, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        self.radioButton_C.setFont(font)
        self.radioButton_C.setObjectName("radioButton_3")
        self.line_compare = QtWidgets.QFrame(Form)
        self.line_compare.setGeometry(QtCore.QRect(500, 180, 40, 130))
        self.line_compare.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        self.line_compare.setFont(font)
        self.line_compare.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_compare.setLineWidth(10)
        self.line_compare.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_compare.setObjectName("line_compare")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(510, 350, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.number_1 = QtWidgets.QLabel(Form)
        self.number_1.setGeometry(QtCore.QRect(40, 90, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(16)
        self.number_1.setFont(font)
        self.number_1.setObjectName("number_1")
        self.number_2 = QtWidgets.QLabel(Form)
        self.number_2.setGeometry(QtCore.QRect(140, 90, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(16)
        self.number_2.setFont(font)
        self.number_2.setObjectName("nubmer_2")
        self.number_3 = QtWidgets.QLabel(Form)
        self.number_3.setGeometry(QtCore.QRect(240, 100, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(16)
        self.number_3.setFont(font)
        self.number_3.setObjectName("number_3")

        if self.selector == 1:
            self.number_1.setText("5")
            self.number_2.setText("0")
            self.number_3.setText("0")

        if self.selector == 2:
            self.number_1.setText("0")
            self.number_2.setText("5")
            self.number_3.setText("0")

        if self.selector == 3:
            self.number_1.setText("0")
            self.number_2.setText("0")
            self.number_3.setText("5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.submitBtn = QtWidgets.QPushButton(Form)
        self.submitBtn.setGeometry(QtCore.QRect(40, 420, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.submitBtn.setFont(font)
        self.submitBtn.setAutoRepeatInterval(102)
        self.submitBtn.setAutoDefault(False)
        self.submitBtn.setDefault(False)
        self.submitBtn.setFlat(False)
        self.submitBtn.setEnabled(False)
        self.submitBtn.setObjectName("submitBtn")
        self.line_horizontal = QtWidgets.QFrame(Form)
        self.line_horizontal.setGeometry(QtCore.QRect(10, 150, 611, 20))
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line_horizontal")
        self.line_vertical_1 = QtWidgets.QFrame(Form)
        self.line_vertical_1.setGeometry(QtCore.QRect(70,90,50,50))
        self.line_vertical_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical_1.setObjectName("line_vertical_1")
        self.line_vertical_2 = QtWidgets.QFrame(Form)
        self.line_vertical_2.setGeometry(QtCore.QRect(180,90, 50, 50))
        self.line_vertical_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical_2.setObjectName("line_vertical_2")
        self.line_vertical_3 = QtWidgets.QFrame(Form)
        self.line_vertical_3.setGeometry(QtCore.QRect(70, 190, 50, 150))
        self.line_vertical_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical_3.setObjectName("line_vertical_1")
        self.line_vertical_4 = QtWidgets.QFrame(Form)
        self.line_vertical_4.setGeometry(QtCore.QRect(180, 190, 50, 150))
        self.line_vertical_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical_4.setObjectName("line_vertical_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton_A.setText(_translate("Form", "A"))
        self.radioButton_B.setText(_translate("Form", "B"))
        self.radioButton_C.setText(_translate("Form", "C"))
        self.label.setText(_translate("Form", "X"))
        self.label_2.setText(_translate("Form", "COMPARE"))
        self.label_6.setText(_translate("Form", "Real time answers:"))
        self.submitBtn.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = experimentWindowClass()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())