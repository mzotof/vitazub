# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SalaryForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SalaryReportForm(object):
    def setupUi(self, SalaryReportForm):
        if not SalaryReportForm.objectName():
            SalaryReportForm.setObjectName(u"SalaryReportForm")
        SalaryReportForm.resize(272, 178)
        font = QFont()
        font.setPointSize(14)
        SalaryReportForm.setFont(font)
        self.gridLayout_3 = QGridLayout(SalaryReportForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(SalaryReportForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cur_month_b = QPushButton(self.groupBox)
        self.cur_month_b.setObjectName(u"cur_month_b")

        self.gridLayout.addWidget(self.cur_month_b, 0, 0, 1, 2)

        self.pre_month_b = QPushButton(self.groupBox)
        self.pre_month_b.setObjectName(u"pre_month_b")

        self.gridLayout.addWidget(self.pre_month_b, 0, 2, 1, 3)

        self.start_dt_e = QDateEdit(self.groupBox)
        self.start_dt_e.setObjectName(u"start_dt_e")
        self.start_dt_e.setCalendarPopup(True)

        self.gridLayout.addWidget(self.start_dt_e, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.end_dt_e = QDateEdit(self.groupBox)
        self.end_dt_e.setObjectName(u"end_dt_e")
        self.end_dt_e.setCalendarPopup(True)

        self.gridLayout.addWidget(self.end_dt_e, 2, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(SalaryReportForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.directory_e = QLineEdit(self.groupBox_2)
        self.directory_e.setObjectName(u"directory_e")

        self.gridLayout_2.addWidget(self.directory_e, 0, 0, 1, 1)

        self.find_dir_b = QPushButton(self.groupBox_2)
        self.find_dir_b.setObjectName(u"find_dir_b")

        self.gridLayout_2.addWidget(self.find_dir_b, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.cancel_b = QPushButton(SalaryReportForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_3.addWidget(self.cancel_b, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(92, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.create_b = QPushButton(SalaryReportForm)
        self.create_b.setObjectName(u"create_b")

        self.gridLayout_3.addWidget(self.create_b, 2, 2, 1, 1)


        self.retranslateUi(SalaryReportForm)

        QMetaObject.connectSlotsByName(SalaryReportForm)
    # setupUi

    def retranslateUi(self, SalaryReportForm):
        SalaryReportForm.setWindowTitle(QCoreApplication.translate("SalaryReportForm", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430 \u043f\u043e \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u0430\u043c \u0432\u0440\u0430\u0447\u0435\u0439", None))
        self.groupBox.setTitle(QCoreApplication.translate("SalaryReportForm", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.cur_month_b.setText(QCoreApplication.translate("SalaryReportForm", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.pre_month_b.setText(QCoreApplication.translate("SalaryReportForm", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.label_2.setText(QCoreApplication.translate("SalaryReportForm", u"\u043f\u043e", None))
        self.label.setText(QCoreApplication.translate("SalaryReportForm", u"\u0421", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SalaryReportForm", u"\u041c\u0435\u0441\u0442\u043e \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.find_dir_b.setText(QCoreApplication.translate("SalaryReportForm", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.cancel_b.setText(QCoreApplication.translate("SalaryReportForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.create_b.setText(QCoreApplication.translate("SalaryReportForm", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

