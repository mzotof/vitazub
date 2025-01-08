# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .classes import DoctorSelector


class Ui_TaskForm(object):
    def setupUi(self, TaskForm):
        if not TaskForm.objectName():
            TaskForm.setObjectName(u"TaskForm")
        TaskForm.resize(362, 358)
        font = QFont()
        font.setPointSize(14)
        TaskForm.setFont(font)
        self.gridLayout_3 = QGridLayout(TaskForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cancel_b = QPushButton(TaskForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_3.addWidget(self.cancel_b, 6, 0, 1, 1)

        self.del_b = QPushButton(TaskForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_3.addWidget(self.del_b, 6, 1, 1, 1)

        self.save_b = QPushButton(TaskForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_3.addWidget(self.save_b, 6, 2, 1, 1)

        self.groupBox = QGroupBox(TaskForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_e = QLineEdit(self.groupBox)
        self.name_e.setObjectName(u"name_e")

        self.gridLayout.addWidget(self.name_e, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 3)

        self.groupBox_2 = QGroupBox(TaskForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comment_e = QLineEdit(self.groupBox_2)
        self.comment_e.setObjectName(u"comment_e")

        self.gridLayout_2.addWidget(self.comment_e, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 4, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(TaskForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dt_e = QDateEdit(self.groupBox_3)
        self.dt_e.setObjectName(u"dt_e")
        self.dt_e.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.dt_e, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(TaskForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.status_s = QComboBox(self.groupBox_4)
        self.status_s.addItem("")
        self.status_s.addItem("")
        self.status_s.addItem("")
        self.status_s.setObjectName(u"status_s")

        self.gridLayout_5.addWidget(self.status_s, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 3)

        self.groupBox_5 = QGroupBox(TaskForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.doctor_s = DoctorSelector(self.groupBox_5)
        self.doctor_s.setObjectName(u"doctor_s")

        self.gridLayout_6.addWidget(self.doctor_s, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_5, 3, 0, 1, 3)


        self.retranslateUi(TaskForm)

        QMetaObject.connectSlotsByName(TaskForm)
    # setupUi

    def retranslateUi(self, TaskForm):
        TaskForm.setWindowTitle(QCoreApplication.translate("TaskForm", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.cancel_b.setText(QCoreApplication.translate("TaskForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.del_b.setText(QCoreApplication.translate("TaskForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.save_b.setText(QCoreApplication.translate("TaskForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("TaskForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TaskForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TaskForm", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d:", None))
        self.dt_e.setDisplayFormat(QCoreApplication.translate("TaskForm", u"dd.MM.yyyy", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TaskForm", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.status_s.setItemText(0, QCoreApplication.translate("TaskForm", u"\u041d\u0435 \u043d\u0430\u0447\u0430\u0442\u043e", None))
        self.status_s.setItemText(1, QCoreApplication.translate("TaskForm", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.status_s.setItemText(2, QCoreApplication.translate("TaskForm", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("TaskForm", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439:", None))
    # retranslateUi

