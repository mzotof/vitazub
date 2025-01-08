# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientInsuranceForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClientInsuranceForm(object):
    def setupUi(self, ClientInsuranceForm):
        if not ClientInsuranceForm.objectName():
            ClientInsuranceForm.setObjectName(u"ClientInsuranceForm")
        ClientInsuranceForm.resize(1375, 523)
        font = QFont()
        font.setPointSize(14)
        ClientInsuranceForm.setFont(font)
        self.gridLayout_6 = QGridLayout(ClientInsuranceForm)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(ClientInsuranceForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.upd_b = QPushButton(self.groupBox)
        self.upd_b.setObjectName(u"upd_b")

        self.gridLayout.addWidget(self.upd_b, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.del_b = QPushButton(self.groupBox)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout.addWidget(self.del_b, 1, 2, 1, 1)

        self.view = QTableView(self.groupBox)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(0, 200))

        self.gridLayout.addWidget(self.view, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.line = QFrame(ClientInsuranceForm)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(ClientInsuranceForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.start_dt_e = QDateEdit(self.groupBox_4)
        self.start_dt_e.setObjectName(u"start_dt_e")
        self.start_dt_e.setMinimumSize(QSize(0, 0))
        self.start_dt_e.setDateTime(QDateTime(QDate(1900, 1, 1), QTime(0, 0, 0)))
        self.start_dt_e.setCurrentSection(QDateTimeEdit.YearSection)
        self.start_dt_e.setCalendarPopup(True)
        self.start_dt_e.setDate(QDate(1900, 1, 1))

        self.gridLayout_3.addWidget(self.start_dt_e, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.end_dt_e = QDateEdit(self.groupBox_5)
        self.end_dt_e.setObjectName(u"end_dt_e")
        self.end_dt_e.setMinimumSize(QSize(0, 0))
        self.end_dt_e.setDateTime(QDateTime(QDate(1900, 1, 1), QTime(0, 0, 0)))
        self.end_dt_e.setCurrentSection(QDateTimeEdit.YearSection)
        self.end_dt_e.setCalendarPopup(True)
        self.end_dt_e.setDate(QDate(1900, 1, 1))

        self.gridLayout_4.addWidget(self.end_dt_e, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(895, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 3, 0, 1, 2)

        self.save_b = QPushButton(self.groupBox_2)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_5.addWidget(self.save_b, 3, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.comment_e = QLineEdit(self.groupBox_8)
        self.comment_e.setObjectName(u"comment_e")
        self.comment_e.setMinimumSize(QSize(0, 0))
        self.comment_e.setReadOnly(False)

        self.gridLayout_8.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_8, 2, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.insur_s = QComboBox(self.groupBox_3)
        self.insur_s.setObjectName(u"insur_s")

        self.gridLayout_2.addWidget(self.insur_s, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.groupBox_2, 2, 0, 1, 1)


        self.retranslateUi(ClientInsuranceForm)

        QMetaObject.connectSlotsByName(ClientInsuranceForm)
    # setupUi

    def retranslateUi(self, ClientInsuranceForm):
        ClientInsuranceForm.setWindowTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u043e \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.upd_b.setText(QCoreApplication.translate("ClientInsuranceForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.del_b.setText(QCoreApplication.translate("ClientInsuranceForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.start_dt_e.setDisplayFormat(QCoreApplication.translate("ClientInsuranceForm", u"yyyy-MM-dd", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u041a\u043e\u043d\u0435\u0446 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.end_dt_e.setDisplayFormat(QCoreApplication.translate("ClientInsuranceForm", u"yyyy-MM-dd", None))
        self.save_b.setText(QCoreApplication.translate("ClientInsuranceForm", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ClientInsuranceForm", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
    # retranslateUi

