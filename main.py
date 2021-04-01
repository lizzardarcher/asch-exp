import csv
import datetime
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ash_exp.startWindow import startWindowClass
from ash_exp.experimentWindow import experimentWindowClass
from ash_exp.endWindow import endWindowClass
from ash_exp.formWindow import formWindowClass

data = {"firstName": "",
        "lastName": "",
        "age": "",
        "gender": "",
        "level": "",
        "answer": "",
        "date": datetime.datetime.now().date()}


def checkIfAccepted():
    uiMainWindow.pushButton.setDisabled(False)


def showForm():
    def verifyCollectedData():
        try:
            text = uiForm.lineEdit.text()
            text_2 = uiForm.lineEdit_2.text()
            age = uiForm.lineEdit_3.text()

            if not text:
                uiForm.label_8.setHidden(False)
                uiForm.pushButton.setEnabled(False)
                uiForm.label_7.setHidden(True)

            else:
                uiForm.label_7.setHidden(False)
                uiForm.label_8.setHidden(True)
                uiForm.pushButton.setEnabled(True)

            if not text_2:
                uiForm.label_9.setHidden(False)
                uiForm.pushButton.setEnabled(False)
                uiForm.label_7.setHidden(True)

            else:
                uiForm.label_7.setHidden(False)
                uiForm.label_9.setHidden(True)
                uiForm.pushButton.setEnabled(True)

            if not age:
                uiForm.label_6.setHidden(False)
                uiForm.pushButton.setEnabled(False)
                uiForm.label_7.setHidden(True)
            elif age >= 18:
                uiForm.label_7.setHidden(False)
                uiForm.label_6.setHidden(True)
                uiForm.pushButton.setEnabled(True)
        except:
            pass

        firstName = uiForm.lineEdit.text()
        data["firstName"] = firstName
        lastName = uiForm.lineEdit_2.text()
        data["lastName"] = lastName
        age = uiForm.lineEdit_3.text()
        data["age"] = age
        gender = uiForm.combobox.currentText()
        data["gender"] = gender
        level = uiForm.combobox_2.currentText()
        data["level"] = level

    global Form
    Form = QtWidgets.QWidget()
    uiForm = formWindowClass()
    uiForm.setupUi(Form)
    MainWindow.close()
    Form.show()
    uiForm.pushButton_2.clicked.connect(verifyCollectedData)
    uiForm.pushButton.clicked.connect(showExperiment)


def showExperiment():
    def checkIfRbtnToggled():
        uiExperiment.submitBtn.setEnabled(True)
        uiExperiment.submitBtn.clicked.connect(showEnd)

        if uiExperiment.radioButton_A.isChecked():
            if uiExperiment.selector == 3:
                print("correct")
                data["answer"] = "correct"
            else:
                print("incorrect")
                data["answer"] = "incorrect"
            uiExperiment.radioButton_B.setEnabled(False)
            uiExperiment.radioButton_C.setEnabled(False)

        if uiExperiment.radioButton_B.isChecked():
            if uiExperiment.selector == 1:
                print("correct")
                data["answer"] = "correct"
            else:
                print("incorrect")
                data["answer"] = "incorrect"
            uiExperiment.radioButton_A.setEnabled(False)
            uiExperiment.radioButton_C.setEnabled(False)

        if uiExperiment.radioButton_C.isChecked():
            if uiExperiment.selector == 2:
                print("correct")
                data["answer"] = "correct"
            else:
                print("incorrect")
                data["answer"] = "incorrect"
            uiExperiment.radioButton_B.setEnabled(False)
            uiExperiment.radioButton_A.setEnabled(False)

    global Experiment
    Experiment = QtWidgets.QWidget()
    uiExperiment = experimentWindowClass()
    uiExperiment.setupUi(Experiment)
    Form.close()
    Experiment.show()
    uiExperiment.radioButton_A.toggled.connect(checkIfRbtnToggled)
    uiExperiment.radioButton_B.toggled.connect(checkIfRbtnToggled)
    uiExperiment.radioButton_C.toggled.connect(checkIfRbtnToggled)


def showEnd():
    def link():
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://en.wikipedia.org/wiki/Solomon_Asch"))

    def showSpoiler():
        uiEnd.label_2.setHidden(False)
        uiEnd.label_3.setHidden(False)
        uiEnd.label_4.setHidden(False)
        uiEnd.label_4.setOpenExternalLinks(True)
        uiEnd.label_4.linkActivated.connect(link)
        uiEnd.pushButton_2.setHidden(True)

    global End
    End = QtWidgets.QWidget()
    uiEnd = endWindowClass()
    uiEnd.setupUi(End)
    Experiment.close()
    End.show()
    uiEnd.label_5.setText(data["answer"])
    if data["answer"] == "correct":
        uiEnd.label_5.setStyleSheet("color: blue; font: bold 18px;")
    else:
        uiEnd.label_5.setStyleSheet("color: red; font: bold 18px;")
    uiEnd.pushButton_2.clicked.connect(showSpoiler)
    uiEnd.pushButton.clicked.connect(End.close)
    uiEnd.pushButton_3.clicked.connect(showExperiment)
    if os.path.exists("results.csv"):
        with open("results.csv", "a") as file:
            fieldnames = ['firstName', 'lastName', 'age', 'gender', 'level', 'answer', "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
    else:
        with open("results.csv", "a") as file:
            fieldnames = ['firstName', 'lastName', 'age', 'gender', 'level', 'answer', "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uiMainWindow = startWindowClass()
    uiMainWindow.setupUi(MainWindow)
    MainWindow.show()
    uiMainWindow.checkBox.clicked.connect(checkIfAccepted)
    uiMainWindow.pushButton.clicked.connect(showForm)
    sys.exit(app.exec_())
