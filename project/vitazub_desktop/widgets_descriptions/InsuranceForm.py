# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InsuranceForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InsuranceForm(object):
    def setupUi(self, InsuranceForm):
        if not InsuranceForm.objectName():
            InsuranceForm.setObjectName(u"InsuranceForm")
        InsuranceForm.resize(295, 218)
        font = QFont()
        font.setPointSize(14)
        InsuranceForm.setFont(font)
        self.gridLayout_3 = QGridLayout(InsuranceForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(InsuranceForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_e = QLineEdit(self.groupBox)
        self.name_e.setObjectName(u"name_e")

        self.gridLayout.addWidget(self.name_e, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(InsuranceForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comment_e = QLineEdit(self.groupBox_2)
        self.comment_e.setObjectName(u"comment_e")

        self.gridLayout_2.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.cancel_b = QPushButton(InsuranceForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_3.addWidget(self.cancel_b, 2, 0, 1, 1)

        self.del_b = QPushButton(InsuranceForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_3.addWidget(self.del_b, 2, 1, 1, 1)

        self.save_b = QPushButton(InsuranceForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_3.addWidget(self.save_b, 2, 2, 1, 1)


        self.retranslateUi(InsuranceForm)

        QMetaObject.connectSlotsByName(InsuranceForm)
    # setupUi

    def retranslateUi(self, InsuranceForm):
        InsuranceForm.setWindowTitle(QCoreApplication.translate("InsuranceForm", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("InsuranceForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("InsuranceForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.cancel_b.setText(QCoreApplication.translate("InsuranceForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.del_b.setText(QCoreApplication.translate("InsuranceForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.save_b.setText(QCoreApplication.translate("InsuranceForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

