# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UserForm(object):
    def setupUi(self, UserForm):
        if not UserForm.objectName():
            UserForm.setObjectName(u"UserForm")
        UserForm.resize(392, 320)
        font = QFont()
        font.setPointSize(14)
        UserForm.setFont(font)
        self.gridLayout_2 = QGridLayout(UserForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.del_b = QPushButton(UserForm)
        self.del_b.setObjectName(u"del_b")
        self.del_b.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.del_b, 6, 2, 1, 1)

        self.save_b = QPushButton(UserForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_2.addWidget(self.save_b, 6, 4, 1, 1)

        self.cancel_b = QPushButton(UserForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_2.addWidget(self.cancel_b, 6, 0, 1, 1)

        self.groupBox_4 = QGroupBox(UserForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comment_e = QLineEdit(self.groupBox_4)
        self.comment_e.setObjectName(u"comment_e")
        self.comment_e.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.comment_e, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 5, 0, 1, 5)

        self.groupBox_3 = QGroupBox(UserForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pass2_e = QLineEdit(self.groupBox_3)
        self.pass2_e.setObjectName(u"pass2_e")
        self.pass2_e.setMinimumSize(QSize(200, 0))
        self.pass2_e.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.pass2_e, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 3, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 6, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 1, 1, 1)

        self.groupBox_2 = QGroupBox(UserForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pass_e = QLineEdit(self.groupBox_2)
        self.pass_e.setObjectName(u"pass_e")
        self.pass_e.setMinimumSize(QSize(200, 0))
        self.pass_e.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pass_e, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 5)

        self.groupBox = QGroupBox(UserForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.login_e = QLineEdit(self.groupBox)
        self.login_e.setObjectName(u"login_e")
        self.login_e.setMinimumSize(QSize(200, 0))

        self.gridLayout_3.addWidget(self.login_e, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 5)

        self.groupBox_5 = QGroupBox(UserForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.type_s = QComboBox(self.groupBox_5)
        self.type_s.addItem("")
        self.type_s.addItem("")
        self.type_s.setObjectName(u"type_s")

        self.gridLayout_6.addWidget(self.type_s, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 4, 0, 1, 5)

        QWidget.setTabOrder(self.login_e, self.pass_e)
        QWidget.setTabOrder(self.pass_e, self.pass2_e)
        QWidget.setTabOrder(self.pass2_e, self.save_b)
        QWidget.setTabOrder(self.save_b, self.del_b)
        QWidget.setTabOrder(self.del_b, self.cancel_b)

        self.retranslateUi(UserForm)

        QMetaObject.connectSlotsByName(UserForm)
    # setupUi

    def retranslateUi(self, UserForm):
        UserForm.setWindowTitle(QCoreApplication.translate("UserForm", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.del_b.setText(QCoreApplication.translate("UserForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.save_b.setText(QCoreApplication.translate("UserForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_b.setText(QCoreApplication.translate("UserForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("UserForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("UserForm", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("UserForm", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.groupBox.setTitle(QCoreApplication.translate("UserForm", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("UserForm", u"\u0422\u0438\u043f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.type_s.setItemText(0, QCoreApplication.translate("UserForm", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.type_s.setItemText(1, QCoreApplication.translate("UserForm", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))

    # retranslateUi

