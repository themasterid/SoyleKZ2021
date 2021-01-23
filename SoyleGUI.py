# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SoyleGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 627)
        MainWindow.setMinimumSize(QtCore.QSize(800, 627))
        MainWindow.setMaximumSize(QtCore.QSize(800, 627))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("soyle.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 390, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.comboBox_0 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_0.setGeometry(QtCore.QRect(10, 10, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_0.setFont(font)
        self.comboBox_0.setObjectName("comboBox_0")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(410, 10, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setObjectName("comboBox_1")
        self.textEdit_0 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_0.setGeometry(QtCore.QRect(410, 390, 381, 31))
        self.textEdit_0.setObjectName("textEdit_0")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 430, 781, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(10, 250, 781, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_0.setFont(font)
        self.label_0.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 350, 781, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 40, 781, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setAutoFillBackground(True)
        self.label_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("KDV.jpg"))
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.replay_word = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.replay_word.setGeometry(QtCore.QRect(10, 250, 781, 91))
        self.replay_word.setText("")
        self.replay_word.setCheckable(False)
        self.replay_word.setObjectName("replay_word")
        self.progressBar_0 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_0.setGeometry(QtCore.QRect(10, 550, 781, 23))
        self.progressBar_0.setProperty("value", 24)
        self.progressBar_0.setObjectName("progressBar_0")
        self.label_status_bar = QtWidgets.QLabel(self.centralwidget)
        self.label_status_bar.setGeometry(QtCore.QRect(10, 520, 781, 31))
        self.label_status_bar.setObjectName("label_status_bar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_about = QtWidgets.QMenu(self.menu_2)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_close_window = QtWidgets.QAction(MainWindow)
        self.action_close_window.setObjectName("action_close_window")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_close_window)
        self.menu_2.addAction(self.action_help)
        self.menu_2.addAction(self.menu_about.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Қазақша сөйлейміз"))
        self.pushButton_1.setText(_translate("MainWindow", "Проверка текста"))
        self.label_0.setText(_translate("MainWindow", "Вывод слов, нажмите кнопку \"Следующее слово\""))
        self.pushButton_0.setText(_translate("MainWindow", "Следующее слово"))
        self.label_status_bar.setText(_translate("MainWindow", "Прогресс выученных слов"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.menu_about.setTitle(_translate("MainWindow", "О программе"))
        self.action_help.setText(_translate("MainWindow", "Справка"))
        self.action_open.setText(_translate("MainWindow", "Открыть"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_close_window.setText(_translate("MainWindow", "Закрыть"))
        self.action.setText(_translate("MainWindow", "изучаем"))
