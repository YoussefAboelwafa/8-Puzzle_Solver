from utils import *
from bfs import bfs_solver
from dfs import dfs_solver

from PyQt5 import QtCore, QtGui, QtWidgets
from steps import Steps_window


# start_state = "123456780"
# goal_state = "012345678"

# if is_solvable(start_state):
#     bfs_solver(start_state, goal_state)
# else:
#     print("Unsolvable")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 599)
        MainWindow.setMinimumSize(QtCore.QSize(837, 599))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 160))
        self.frame_4.setMaximumSize(QtCore.QSize(30000, 347))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 20, 81, 20))
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(270, 50, 5, 210))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 60, 50, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(60, 120, 210, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(60, 260, 210, 5))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(60, 190, 210, 5))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(200, 50, 5, 210))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(130, 50, 5, 210))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(60, 50, 5, 210))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 60, 50, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 60, 50, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 130, 50, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 130, 50, 50))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 130, 50, 50))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 200, 50, 50))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 200, 50, 50))

        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 200, 50, 50))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(60, 50, 210, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 81, 20))
        self.label_2.setObjectName("label_2")
        self.line_10 = QtWidgets.QFrame(self.frame_2)
        self.line_10.setGeometry(QtCore.QRect(270, 50, 5, 210))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 60, 50, 50))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.line_11 = QtWidgets.QFrame(self.frame_2)
        self.line_11.setGeometry(QtCore.QRect(60, 50, 210, 5))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame_2)
        self.line_12.setGeometry(QtCore.QRect(60, 120, 210, 5))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame_2)
        self.line_13.setGeometry(QtCore.QRect(60, 260, 210, 5))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.frame_2)
        self.line_14.setGeometry(QtCore.QRect(60, 190, 210, 5))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.frame_2)
        self.line_15.setGeometry(QtCore.QRect(200, 50, 5, 210))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.frame_2)
        self.line_16.setGeometry(QtCore.QRect(130, 50, 5, 210))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.frame_2)
        self.line_17.setGeometry(QtCore.QRect(60, 50, 5, 210))
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 60, 50, 50))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(210, 60, 50, 50))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(70, 130, 50, 50))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 130, 50, 50))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 130, 50, 50))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(70, 200, 50, 50))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(140, 200, 50, 50))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(210, 200, 50, 50))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_4)

        ## put all line edit boxes in a list
        self.lineEdit_list = [
            self.lineEdit,
            self.lineEdit_2,
            self.lineEdit_3,
            self.lineEdit_4,
            self.lineEdit_5,
            self.lineEdit_6,
            self.lineEdit_7,
            self.lineEdit_8,
            self.lineEdit_9,
            self.lineEdit_10,
            self.lineEdit_11,
            self.lineEdit_12,
            self.lineEdit_13,
            self.lineEdit_14,
            self.lineEdit_15,
            self.lineEdit_16,
            self.lineEdit_17,
            self.lineEdit_18
        ]

        ## set the font size and style for all lineedit boxes 
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)
        self.lineEdit_4.setFont(font)
        self.lineEdit_5.setFont(font)
        self.lineEdit_6.setFont(font)
        self.lineEdit_7.setFont(font)
        self.lineEdit_8.setFont(font)
        self.lineEdit_9.setFont(font)
        self.lineEdit_10.setFont(font)
        self.lineEdit_11.setFont(font)
        self.lineEdit_12.setFont(font)
        self.lineEdit_13.setFont(font)
        self.lineEdit_14.setFont(font)
        self.lineEdit_15.setFont(font)
        self.lineEdit_16.setFont(font)
        self.lineEdit_17.setFont(font)
        self.lineEdit_18.setFont(font)

        ## set the alignment for all lineedit boxes
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)

        # attach function to detect text change
        self.lineEdit.textChanged.connect(self.checkValues)
        self.lineEdit_2.textChanged.connect(self.checkValues)
        self.lineEdit_3.textChanged.connect(self.checkValues)
        self.lineEdit_4.textChanged.connect(self.checkValues)
        self.lineEdit_5.textChanged.connect(self.checkValues)
        self.lineEdit_6.textChanged.connect(self.checkValues)
        self.lineEdit_7.textChanged.connect(self.checkValues)
        self.lineEdit_8.textChanged.connect(self.checkValues)
        self.lineEdit_9.textChanged.connect(self.checkValues)
        self.lineEdit_10.textChanged.connect(self.checkValues)
        self.lineEdit_11.textChanged.connect(self.checkValues)
        self.lineEdit_12.textChanged.connect(self.checkValues)
        self.lineEdit_13.textChanged.connect(self.checkValues)
        self.lineEdit_14.textChanged.connect(self.checkValues)
        self.lineEdit_15.textChanged.connect(self.checkValues)
        self.lineEdit_16.textChanged.connect(self.checkValues)
        self.lineEdit_17.textChanged.connect(self.checkValues)
        self.lineEdit_18.textChanged.connect(self.checkValues)
        
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(819, 183))
        self.frame_3.setMaximumSize(QtCore.QSize(39999, 183))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 91, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:3px;\n"
"    background:rgb(183, 234, 255);\n"
"    color:rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:rgb(239, 255, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.solve)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(299, 10, 191, 21))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8-Puzzle Solver"))
        self.label.setText(_translate("MainWindow", "Enter start state"))
        self.label_2.setText(_translate("MainWindow", "Enter goal state"))
        self.pushButton.setText(_translate("MainWindow", "Solve"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose algorithm"))
        self.comboBox.setItemText(1, _translate("MainWindow", "BFS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "DFS"))
        self.comboBox.setItemText(3, _translate("MainWindow", "A*"))        
    def solve(self):
        if self.comboBox.currentText() == "Choose algorithm":
            self.show_error("Please choose an algorithm")
        else:
            start_state=str()
            end_state=str()
            # start_state = "123456780"
            # end_state = "012345678"  
            zero_count=0
            for i in range(9):
                ## check if the text is not emphty
                if self.lineEdit_list[i].text() == "":
                    start_state+='0'
                    zero_count+=1
                    if zero_count>1:
                        self.show_error("Please fill all the boxes")
                        return
                else:
                    start_state+=self.lineEdit_list[i].text()
            ## check that the string is distict 
            if len(set(start_state)) != 9:
                self.show_error("Please enter a correct values")
                return
            
            zero_count=0
            for i in range(9,18):
                ## check if the text is not emphty
                if self.lineEdit_list[i].text() == "":
                    end_state+='0'
                    zero_count+=1
                    if zero_count>1:
                        self.show_error("Please fill all the boxes")
                        return
                else:
                    end_state+=self.lineEdit_list[i].text()
                
            if len(set(end_state)) != 9:
                self.show_error("Please enter a correct values")
            if self.comboBox.currentText() =='BFS':
                self.res =bfs_solver(start_state, end_state)
            elif self.comboBox.currentText() == 'DFS':
                self.res = dfs_solver(start_state, end_state)
            else:
                pass

            if self.res[0]==False:
                self.show_info('No solution')
            else:
                self.form = QtWidgets.QWidget()
                self.step_window = Steps_window()
                self.step_window.setupUi(self.form)
                self.step_window.init_solution(self.res[1])
                self.form.show()

            

    def checkValues(self):
        values = [
            self.lineEdit.text(),
            self.lineEdit_2.text(),
            self.lineEdit_3.text(),
            self.lineEdit_4.text(),
            self.lineEdit_5.text(),
            self.lineEdit_6.text(),
            self.lineEdit_7.text(),
            self.lineEdit_8.text(),
            self.lineEdit_9.text(),
            self.lineEdit_10.text(),
            self.lineEdit_11.text(),
            self.lineEdit_12.text(),
            self.lineEdit_13.text(),
            self.lineEdit_14.text(),
            self.lineEdit_15.text(),
            self.lineEdit_16.text(),
            self.lineEdit_17.text(),
            self.lineEdit_18.text()
        ]

        for value in range(len(values)):
            if values[value] == "":
                continue
            else:
                try:
                    int(values[value])
                    ## check if this value is single digit
                    if len(values[value]) > 1:
                        self.show_error("Please enter a single digit")
                        # erese this value 
                        self.lineEdit_list[value].setText("")
                        return
                    elif values[value] == '9':
                        self.show_error("Please enter a digit in range of (0 , 8)")
                        self.lineEdit_list[value].setText("")
                        return
                        
                    
                except:
                    self.show_error("Please enter a valid digit")
                    # erese this value 
                    self.lineEdit_list[value].setText("")
                    return
    def show_error(self,message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
