from PyQt5 import QtCore, QtGui, QtWidgets


'''This .py file contains the widgets. '''

class Ui_Essay_Generator(object):

    def setupUi(self, Essay_Generator):
        #This creates Main Window
        Essay_Generator.setObjectName("Essay_Generator")
        Essay_Generator.resize(1281, 655)
        Essay_Generator.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(Essay_Generator)
        self.centralwidget.setObjectName("centralwidget")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(380, 300, 251, 41))

        #This creates pushButton
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setUnderline(True)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 231, 41))
        #This creates label
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 151, 31))

        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.getText = QtWidgets.QLineEdit(self.centralwidget)
        self.getText.setGeometry(QtCore.QRect(710, 40, 311, 31))

        #This creates the comboBox
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.getText.setFont(font)
        self.getText.setObjectName("getText")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(710, 140, 321, 31))

        #This adds the items to the comboBox 
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        #This creates label for displaying the result of process
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(10, 360, 1261, 261))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.Result.setFont(font)
        self.Result.setText("")
        self.Result.setObjectName("Result")
        Essay_Generator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Essay_Generator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 20))

        self.menubar.setObjectName("menubar")
        Essay_Generator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Essay_Generator)
        self.statusbar.setObjectName("statusbar")
        Essay_Generator.setStatusBar(self.statusbar)

        self.retranslateUi(Essay_Generator)
        QtCore.QMetaObject.connectSlotsByName(Essay_Generator)

    def retranslateUi(self, Essay_Generator):
        _translate = QtCore.QCoreApplication.translate
        Essay_Generator.setWindowTitle(_translate("Essay_Generator", "Essay_Generator"))
        self.generate.setText(_translate("Essay_Generator", "GENERATE"))
        self.label.setText(_translate("Essay_Generator", "Enter The Topic"))
        self.label_2.setText(_translate("Essay_Generator", "Browser"))
        self.comboBox.setItemText(0, _translate("Essay_Generator", "None"))
        self.comboBox.setItemText(1, _translate("Essay_Generator", "Chrome"))
        self.comboBox.setItemText(2, _translate("Essay_Generator", "Firefox"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Essay_Generator = QtWidgets.QMainWindow()
    ui = Ui_Essay_Generator()
    ui.setupUi(Essay_Generator)
    Essay_Generator.show()
    sys.exit(app.exec_())
