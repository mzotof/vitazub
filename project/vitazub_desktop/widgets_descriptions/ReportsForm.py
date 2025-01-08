# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReportsForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ReportsForm(object):
    def setupUi(self, ReportsForm):
        if not ReportsForm.objectName():
            ReportsForm.setObjectName(u"ReportsForm")
        ReportsForm.resize(966, 519)
        font = QFont()
        font.setPointSize(14)
        ReportsForm.setFont(font)
        self.gridLayout = QGridLayout(ReportsForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(ReportsForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rec_upd_b = QPushButton(self.tab)
        self.rec_upd_b.setObjectName(u"rec_upd_b")

        self.gridLayout_2.addWidget(self.rec_upd_b, 1, 3, 1, 1)

        self.rec_v = QVBoxLayout()
        self.rec_v.setObjectName(u"rec_v")

        self.gridLayout_2.addLayout(self.rec_v, 0, 0, 1, 4)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.rec_start_dt = QDateEdit(self.groupBox)
        self.rec_start_dt.setObjectName(u"rec_start_dt")
        self.rec_start_dt.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.rec_start_dt)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.rec_end_dt = QDateEdit(self.groupBox)
        self.rec_end_dt.setObjectName(u"rec_end_dt")
        self.rec_end_dt.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.rec_end_dt)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rec_days_r = QRadioButton(self.groupBox_2)
        self.rec_days_r.setObjectName(u"rec_days_r")
        self.rec_days_r.setChecked(True)

        self.horizontalLayout.addWidget(self.rec_days_r)

        self.rec_months_r = QRadioButton(self.groupBox_2)
        self.rec_months_r.setObjectName(u"rec_months_r")

        self.horizontalLayout.addWidget(self.rec_months_r)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.serv_v = QVBoxLayout()
        self.serv_v.setObjectName(u"serv_v")

        self.gridLayout_4.addLayout(self.serv_v, 0, 0, 1, 4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.serv_start_dt = QDateEdit(self.groupBox_5)
        self.serv_start_dt.setObjectName(u"serv_start_dt")
        self.serv_start_dt.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.serv_start_dt)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.serv_end_dt = QDateEdit(self.groupBox_5)
        self.serv_end_dt.setObjectName(u"serv_end_dt")
        self.serv_end_dt.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.serv_end_dt)


        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.serv_serv_r = QRadioButton(self.groupBox_6)
        self.serv_serv_r.setObjectName(u"serv_serv_r")
        self.serv_serv_r.setChecked(True)

        self.horizontalLayout_8.addWidget(self.serv_serv_r)

        self.serv_cat_r = QRadioButton(self.groupBox_6)
        self.serv_cat_r.setObjectName(u"serv_cat_r")

        self.horizontalLayout_8.addWidget(self.serv_cat_r)


        self.gridLayout_4.addWidget(self.groupBox_6, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(425, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.serv_upd_b = QPushButton(self.tab_2)
        self.serv_upd_b.setObjectName(u"serv_upd_b")

        self.gridLayout_4.addWidget(self.serv_upd_b, 1, 3, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fin_v = QVBoxLayout()
        self.fin_v.setObjectName(u"fin_v")

        self.gridLayout_5.addLayout(self.fin_v, 0, 0, 1, 5)

        self.groupBox_7 = QGroupBox(self.tab_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.fin_start_dt = QDateEdit(self.groupBox_7)
        self.fin_start_dt.setObjectName(u"fin_start_dt")
        self.fin_start_dt.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.fin_start_dt)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.fin_end_dt = QDateEdit(self.groupBox_7)
        self.fin_end_dt.setObjectName(u"fin_end_dt")
        self.fin_end_dt.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.fin_end_dt)


        self.gridLayout_5.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fin_days_r = QRadioButton(self.groupBox_8)
        self.fin_days_r.setObjectName(u"fin_days_r")
        self.fin_days_r.setChecked(True)

        self.horizontalLayout_10.addWidget(self.fin_days_r)

        self.fin_months_r = QRadioButton(self.groupBox_8)
        self.fin_months_r.setObjectName(u"fin_months_r")

        self.horizontalLayout_10.addWidget(self.fin_months_r)


        self.gridLayout_5.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fin_income_r = QRadioButton(self.groupBox_9)
        self.fin_income_r.setObjectName(u"fin_income_r")
        self.fin_income_r.setChecked(True)

        self.horizontalLayout_11.addWidget(self.fin_income_r)

        self.fin_outcome_r = QRadioButton(self.groupBox_9)
        self.fin_outcome_r.setObjectName(u"fin_outcome_r")

        self.horizontalLayout_11.addWidget(self.fin_outcome_r)

        self.fin_profit_r = QRadioButton(self.groupBox_9)
        self.fin_profit_r.setObjectName(u"fin_profit_r")

        self.horizontalLayout_11.addWidget(self.fin_profit_r)

        self.fin_payment_type_r = QRadioButton(self.groupBox_9)
        self.fin_payment_type_r.setObjectName(u"fin_payment_type_r")

        self.horizontalLayout_11.addWidget(self.fin_payment_type_r)


        self.gridLayout_5.addWidget(self.groupBox_9, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(71, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.fin_upd_b = QPushButton(self.tab_5)
        self.fin_upd_b.setObjectName(u"fin_upd_b")

        self.gridLayout_5.addWidget(self.fin_upd_b, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(ReportsForm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ReportsForm)
    # setupUi

    def retranslateUi(self, ReportsForm):
        ReportsForm.setWindowTitle(QCoreApplication.translate("ReportsForm", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.rec_upd_b.setText(QCoreApplication.translate("ReportsForm", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("ReportsForm", u"\u041f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label.setText(QCoreApplication.translate("ReportsForm", u"\u0421", None))
        self.label_2.setText(QCoreApplication.translate("ReportsForm", u"\u043f\u043e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ReportsForm", u"\u0413\u0440\u0430\u0434\u0443\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e:", None))
        self.rec_days_r.setText(QCoreApplication.translate("ReportsForm", u"\u0434\u043d\u044f\u043c", None))
        self.rec_months_r.setText(QCoreApplication.translate("ReportsForm", u"\u043c\u0435\u0441\u044f\u0446\u0430\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ReportsForm", u"\u041f\u0440\u0438\u0435\u043c\u044b", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ReportsForm", u"\u041f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_7.setText(QCoreApplication.translate("ReportsForm", u"\u0421", None))
        self.label_8.setText(QCoreApplication.translate("ReportsForm", u"\u043f\u043e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ReportsForm", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e:", None))
        self.serv_serv_r.setText(QCoreApplication.translate("ReportsForm", u"\u0443\u0441\u043b\u0443\u0433\u0430\u043c", None))
        self.serv_cat_r.setText(QCoreApplication.translate("ReportsForm", u"\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c", None))
        self.serv_upd_b.setText(QCoreApplication.translate("ReportsForm", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ReportsForm", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ReportsForm", u"\u041f\u0435\u0440\u0438\u043e\u0434:", None))
        self.label_9.setText(QCoreApplication.translate("ReportsForm", u"\u0421", None))
        self.label_10.setText(QCoreApplication.translate("ReportsForm", u"\u043f\u043e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ReportsForm", u"\u0413\u0440\u0430\u0434\u0443\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e:", None))
        self.fin_days_r.setText(QCoreApplication.translate("ReportsForm", u"\u0434\u043d\u044f\u043c", None))
        self.fin_months_r.setText(QCoreApplication.translate("ReportsForm", u"\u043c\u0435\u0441\u044f\u0446\u0430\u043c", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("ReportsForm", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e:", None))
        self.fin_income_r.setText(QCoreApplication.translate("ReportsForm", u"\u0434\u043e\u0445\u043e\u0434\u0430\u043c", None))
        self.fin_outcome_r.setText(QCoreApplication.translate("ReportsForm", u"\u0440\u0430\u0441\u0445\u043e\u0434\u0430\u043c", None))
        self.fin_profit_r.setText(QCoreApplication.translate("ReportsForm", u"\u043f\u0440\u0438\u0431\u044b\u043b\u044c", None))
        self.fin_payment_type_r.setText(QCoreApplication.translate("ReportsForm", u"\u0442\u0438\u043f\u0430\u043c \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
        self.fin_upd_b.setText(QCoreApplication.translate("ReportsForm", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("ReportsForm", u"\u0424\u0438\u043d\u0430\u043d\u0441\u044b", None))
    # retranslateUi

