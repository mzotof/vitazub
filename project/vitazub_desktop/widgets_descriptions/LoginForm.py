# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(392, 149)
        font = QFont()
        font.setPointSize(14)
        LoginForm.setFont(font)
        self.gridLayout_2 = QGridLayout(LoginForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(LoginForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.passEdit = QLineEdit(self.groupBox_2)
        self.passEdit.setObjectName(u"passEdit")
        self.passEdit.setMinimumSize(QSize(200, 0))
        self.passEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passEdit, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox = QGroupBox(LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.loginEdit = QLineEdit(self.groupBox)
        self.loginEdit.setObjectName(u"loginEdit")
        self.loginEdit.setMinimumSize(QSize(200, 0))

        self.gridLayout_3.addWidget(self.loginEdit, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)

        self.cancelButton = QPushButton(LoginForm)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout_2.addWidget(self.cancelButton, 2, 0, 1, 1)

        self.configButton = QPushButton(LoginForm)
        self.configButton.setObjectName(u"configButton")
        self.configButton.setMinimumSize(QSize(248, 0))

        self.gridLayout_2.addWidget(self.configButton, 2, 1, 1, 1)

        self.enterButton = QPushButton(LoginForm)
        self.enterButton.setObjectName(u"enterButton")

        self.gridLayout_2.addWidget(self.enterButton, 2, 2, 1, 1)

        QWidget.setTabOrder(self.loginEdit, self.passEdit)
        QWidget.setTabOrder(self.passEdit, self.enterButton)
        QWidget.setTabOrder(self.enterButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.configButton)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("LoginForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.groupBox.setTitle(QCoreApplication.translate("LoginForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d:", None))
        self.cancelButton.setText(QCoreApplication.translate("LoginForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.configButton.setText(QCoreApplication.translate("LoginForm", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.enterButton.setText(QCoreApplication.translate("LoginForm", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

