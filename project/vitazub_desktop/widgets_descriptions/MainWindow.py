# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .classes import Scheduler
from .classes import DoctorSelector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 650)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.add_client = QAction(MainWindow)
        self.add_client.setObjectName(u"add_client")
        self.view_clients = QAction(MainWindow)
        self.view_clients.setObjectName(u"view_clients")
        self.view_doctors = QAction(MainWindow)
        self.view_doctors.setObjectName(u"view_doctors")
        self.add_doctor = QAction(MainWindow)
        self.add_doctor.setObjectName(u"add_doctor")
        self.edit_users = QAction(MainWindow)
        self.edit_users.setObjectName(u"edit_users")
        self.change_user = QAction(MainWindow)
        self.change_user.setObjectName(u"change_user")
        self.show_reminder_m = QAction(MainWindow)
        self.show_reminder_m.setObjectName(u"show_reminder_m")
        self.save_db = QAction(MainWindow)
        self.save_db.setObjectName(u"save_db")
        self.change_db = QAction(MainWindow)
        self.change_db.setObjectName(u"change_db")
        self.edit_technical = QAction(MainWindow)
        self.edit_technical.setObjectName(u"edit_technical")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionFFF = QAction(MainWindow)
        self.actionFFF.setObjectName(u"actionFFF")
        self.salary_report = QAction(MainWindow)
        self.salary_report.setObjectName(u"salary_report")
        self.reports = QAction(MainWindow)
        self.reports.setObjectName(u"reports")
        self.make_trans = QAction(MainWindow)
        self.make_trans.setObjectName(u"make_trans")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.calendar = QWidget()
        self.calendar.setObjectName(u"calendar")
        self.gridLayout = QGridLayout(self.calendar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rec_del_b = QPushButton(self.calendar)
        self.rec_del_b.setObjectName(u"rec_del_b")
        self.rec_del_b.setFont(font)

        self.gridLayout.addWidget(self.rec_del_b, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.rec_upd_b = QPushButton(self.calendar)
        self.rec_upd_b.setObjectName(u"rec_upd_b")
        self.rec_upd_b.setFont(font)

        self.gridLayout.addWidget(self.rec_upd_b, 0, 3, 1, 1)

        self.rec_ins_b = QPushButton(self.calendar)
        self.rec_ins_b.setObjectName(u"rec_ins_b")
        self.rec_ins_b.setFont(font)

        self.gridLayout.addWidget(self.rec_ins_b, 0, 5, 1, 1)

        self.doctor_s = DoctorSelector(self.calendar)
        self.doctor_s.setObjectName(u"doctor_s")
        self.doctor_s.setMinimumSize(QSize(400, 0))
        self.doctor_s.setFont(font)

        self.gridLayout.addWidget(self.doctor_s, 0, 1, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.date_s = Scheduler(self.calendar)
        self.date_s.setObjectName(u"date_s")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.date_s.sizePolicy().hasHeightForWidth())
        self.date_s.setSizePolicy(sizePolicy)
        self.date_s.setMinimumSize(QSize(0, 0))
        self.date_s.setSizeIncrement(QSize(0, 0))
        self.date_s.setFont(font)
        self.date_s.setMinimumDate(QDate(1752, 9, 23))
        self.date_s.setGridVisible(True)

        self.gridLayout_27.addWidget(self.date_s, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.rec_v = QTableView(self.calendar)
        self.rec_v.setObjectName(u"rec_v")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.rec_v.sizePolicy().hasHeightForWidth())
        self.rec_v.setSizePolicy(sizePolicy1)
        self.rec_v.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        self.rec_v.setFont(font1)
        self.rec_v.setFrameShape(QFrame.Shape.Box)
        self.rec_v.setFrameShadow(QFrame.Shadow.Sunken)
        self.rec_v.setLineWidth(2)
        self.rec_v.setMidLineWidth(0)
        self.rec_v.horizontalHeader().setCascadingSectionResizes(True)
        self.rec_v.verticalHeader().setVisible(False)

        self.gridLayout_27.addWidget(self.rec_v, 1, 1, 2, 1)


        self.gridLayout.addLayout(self.gridLayout_27, 1, 0, 1, 6)

        self.tabWidget.addTab(self.calendar, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_26 = QGridLayout(self.tab)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupBox_16 = QGroupBox(self.tab)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_24 = QGridLayout(self.groupBox_16)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.loan_ln_e = QLineEdit(self.groupBox_16)
        self.loan_ln_e.setObjectName(u"loan_ln_e")

        self.gridLayout_24.addWidget(self.loan_ln_e, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_16, 0, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_25 = QGridLayout(self.groupBox_17)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.loan_fn_e = QLineEdit(self.groupBox_17)
        self.loan_fn_e.setObjectName(u"loan_fn_e")

        self.gridLayout_25.addWidget(self.loan_fn_e, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_17, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_22 = QGridLayout(self.groupBox_14)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.loan_mn_e = QLineEdit(self.groupBox_14)
        self.loan_mn_e.setObjectName(u"loan_mn_e")

        self.gridLayout_22.addWidget(self.loan_mn_e, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_14, 0, 2, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_23 = QGridLayout(self.groupBox_15)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label = QLabel(self.groupBox_15)
        self.label.setObjectName(u"label")

        self.gridLayout_23.addWidget(self.label, 0, 0, 1, 1)

        self.loan_start_dt_e = QDateEdit(self.groupBox_15)
        self.loan_start_dt_e.setObjectName(u"loan_start_dt_e")
        self.loan_start_dt_e.setCalendarPopup(True)

        self.gridLayout_23.addWidget(self.loan_start_dt_e, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_15)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_23.addWidget(self.label_2, 0, 2, 1, 1)

        self.loan_end_dt_e = QDateEdit(self.groupBox_15)
        self.loan_end_dt_e.setObjectName(u"loan_end_dt_e")
        self.loan_end_dt_e.setCalendarPopup(True)

        self.gridLayout_23.addWidget(self.loan_end_dt_e, 0, 3, 1, 1)


        self.gridLayout_26.addWidget(self.groupBox_15, 0, 3, 1, 1)

        self.loan_search_b = QPushButton(self.tab)
        self.loan_search_b.setObjectName(u"loan_search_b")

        self.gridLayout_26.addWidget(self.loan_search_b, 0, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(292, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.loan_v = QTableView(self.tab)
        self.loan_v.setObjectName(u"loan_v")
        self.loan_v.setSortingEnabled(True)

        self.gridLayout_26.addWidget(self.loan_v, 1, 0, 1, 6)

        self.tabWidget.addTab(self.tab, "")
        self.clients = QWidget()
        self.clients.setObjectName(u"clients")
        self.gridLayout_7 = QGridLayout(self.clients)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_2 = QGroupBox(self.clients)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.client_fn_e = QLineEdit(self.groupBox_2)
        self.client_fn_e.setObjectName(u"client_fn_e")

        self.gridLayout_5.addWidget(self.client_fn_e, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.clients)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.client_ln_e = QLineEdit(self.groupBox)
        self.client_ln_e.setObjectName(u"client_ln_e")

        self.gridLayout_4.addWidget(self.client_ln_e, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.client_del_b = QPushButton(self.clients)
        self.client_del_b.setObjectName(u"client_del_b")

        self.gridLayout_7.addWidget(self.client_del_b, 0, 7, 1, 1)

        self.client_add_b = QPushButton(self.clients)
        self.client_add_b.setObjectName(u"client_add_b")

        self.gridLayout_7.addWidget(self.client_add_b, 0, 8, 1, 1)

        self.client_search_b = QPushButton(self.clients)
        self.client_search_b.setObjectName(u"client_search_b")

        self.gridLayout_7.addWidget(self.client_search_b, 0, 4, 1, 1)

        self.client_edit_b = QPushButton(self.clients)
        self.client_edit_b.setObjectName(u"client_edit_b")
        icon = QIcon(QIcon.fromTheme(u"enter"))
        self.client_edit_b.setIcon(icon)

        self.gridLayout_7.addWidget(self.client_edit_b, 0, 6, 1, 1)

        self.clients_v = QTableView(self.clients)
        self.clients_v.setObjectName(u"clients_v")
        self.clients_v.setSortingEnabled(True)

        self.gridLayout_7.addWidget(self.clients_v, 1, 0, 1, 9)

        self.groupBox_3 = QGroupBox(self.clients)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.client_mn_e = QLineEdit(self.groupBox_3)
        self.client_mn_e.setObjectName(u"client_mn_e")

        self.gridLayout_6.addWidget(self.client_mn_e, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.clients)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_15 = QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.next_visit_dt_s = QComboBox(self.groupBox_9)
        self.next_visit_dt_s.addItem("")
        self.next_visit_dt_s.addItem("")
        self.next_visit_dt_s.addItem("")
        self.next_visit_dt_s.addItem("")
        self.next_visit_dt_s.setObjectName(u"next_visit_dt_s")

        self.gridLayout_15.addWidget(self.next_visit_dt_s, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_9, 0, 3, 1, 1)

        self.tabWidget.addTab(self.clients, "")
        self.insurances = QWidget()
        self.insurances.setObjectName(u"insurances")
        self.gridLayout_3 = QGridLayout(self.insurances)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_6 = QGroupBox(self.insurances)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.insur_name_e = QLineEdit(self.groupBox_6)
        self.insur_name_e.setObjectName(u"insur_name_e")

        self.gridLayout_10.addWidget(self.insur_name_e, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.insur_sel_b = QPushButton(self.insurances)
        self.insur_sel_b.setObjectName(u"insur_sel_b")

        self.gridLayout_3.addWidget(self.insur_sel_b, 0, 1, 1, 1)

        self.insur_sel_all_b = QPushButton(self.insurances)
        self.insur_sel_all_b.setObjectName(u"insur_sel_all_b")

        self.gridLayout_3.addWidget(self.insur_sel_all_b, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(407, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.insur_upd_b = QPushButton(self.insurances)
        self.insur_upd_b.setObjectName(u"insur_upd_b")

        self.gridLayout_3.addWidget(self.insur_upd_b, 0, 4, 1, 1)

        self.insur_del_b = QPushButton(self.insurances)
        self.insur_del_b.setObjectName(u"insur_del_b")

        self.gridLayout_3.addWidget(self.insur_del_b, 0, 5, 1, 1)

        self.insur_ins_b = QPushButton(self.insurances)
        self.insur_ins_b.setObjectName(u"insur_ins_b")

        self.gridLayout_3.addWidget(self.insur_ins_b, 0, 6, 1, 1)

        self.insur_v = QTableView(self.insurances)
        self.insur_v.setObjectName(u"insur_v")
        self.insur_v.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.insur_v, 1, 0, 1, 7)

        self.tabWidget.addTab(self.insurances, "")
        self.doctors = QWidget()
        self.doctors.setObjectName(u"doctors")
        self.gridLayout_12 = QGridLayout(self.doctors)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_4 = QGroupBox(self.doctors)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.doctor_ln_e = QLineEdit(self.groupBox_4)
        self.doctor_ln_e.setObjectName(u"doctor_ln_e")

        self.gridLayout_8.addWidget(self.doctor_ln_e, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.doctors)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.doctor_fn_e = QLineEdit(self.groupBox_5)
        self.doctor_fn_e.setObjectName(u"doctor_fn_e")

        self.gridLayout_9.addWidget(self.doctor_fn_e, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.doctors)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_11 = QGridLayout(self.groupBox_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.doctor_mn_e = QLineEdit(self.groupBox_7)
        self.doctor_mn_e.setObjectName(u"doctor_mn_e")

        self.gridLayout_11.addWidget(self.doctor_mn_e, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_7, 0, 2, 1, 1)

        self.doctor_sel_b = QPushButton(self.doctors)
        self.doctor_sel_b.setObjectName(u"doctor_sel_b")

        self.gridLayout_12.addWidget(self.doctor_sel_b, 0, 3, 1, 1)

        self.doctor_sel_all_b = QPushButton(self.doctors)
        self.doctor_sel_all_b.setObjectName(u"doctor_sel_all_b")

        self.gridLayout_12.addWidget(self.doctor_sel_all_b, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.doctor_upd_b = QPushButton(self.doctors)
        self.doctor_upd_b.setObjectName(u"doctor_upd_b")
        self.doctor_upd_b.setIcon(icon)

        self.gridLayout_12.addWidget(self.doctor_upd_b, 0, 6, 1, 1)

        self.doctor_del_b = QPushButton(self.doctors)
        self.doctor_del_b.setObjectName(u"doctor_del_b")

        self.gridLayout_12.addWidget(self.doctor_del_b, 0, 7, 1, 1)

        self.doctor_ins_b = QPushButton(self.doctors)
        self.doctor_ins_b.setObjectName(u"doctor_ins_b")

        self.gridLayout_12.addWidget(self.doctor_ins_b, 0, 8, 1, 1)

        self.doctor_v = QTableView(self.doctors)
        self.doctor_v.setObjectName(u"doctor_v")
        self.doctor_v.setSortingEnabled(True)

        self.gridLayout_12.addWidget(self.doctor_v, 1, 0, 1, 9)

        self.tabWidget.addTab(self.doctors, "")
        self.services = QWidget()
        self.services.setObjectName(u"services")
        self.gridLayout_14 = QGridLayout(self.services)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_8 = QGroupBox(self.services)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_13 = QGridLayout(self.groupBox_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.serv_filter_e = QLineEdit(self.groupBox_8)
        self.serv_filter_e.setObjectName(u"serv_filter_e")

        self.gridLayout_13.addWidget(self.serv_filter_e, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.serv_sel_b = QPushButton(self.services)
        self.serv_sel_b.setObjectName(u"serv_sel_b")

        self.gridLayout_14.addWidget(self.serv_sel_b, 0, 1, 1, 1)

        self.serv_sel_all_b = QPushButton(self.services)
        self.serv_sel_all_b.setObjectName(u"serv_sel_all_b")

        self.gridLayout_14.addWidget(self.serv_sel_all_b, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.serv_upd_b = QPushButton(self.services)
        self.serv_upd_b.setObjectName(u"serv_upd_b")

        self.gridLayout_14.addWidget(self.serv_upd_b, 0, 4, 1, 1)

        self.serv_del_b = QPushButton(self.services)
        self.serv_del_b.setObjectName(u"serv_del_b")

        self.gridLayout_14.addWidget(self.serv_del_b, 0, 5, 1, 1)

        self.serv_ins_b = QPushButton(self.services)
        self.serv_ins_b.setObjectName(u"serv_ins_b")

        self.gridLayout_14.addWidget(self.serv_ins_b, 0, 6, 1, 1)

        self.serv_v = QTableView(self.services)
        self.serv_v.setObjectName(u"serv_v")
        self.serv_v.setSortingEnabled(True)

        self.gridLayout_14.addWidget(self.serv_v, 1, 0, 1, 7)

        self.tabWidget.addTab(self.services, "")
        self.materials = QWidget()
        self.materials.setObjectName(u"materials")
        self.gridLayout_17 = QGridLayout(self.materials)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.mater_sub_b = QPushButton(self.materials)
        self.mater_sub_b.setObjectName(u"mater_sub_b")

        self.gridLayout_17.addWidget(self.mater_sub_b, 0, 5, 1, 1)

        self.mater_sel_all_b = QPushButton(self.materials)
        self.mater_sel_all_b.setObjectName(u"mater_sel_all_b")

        self.gridLayout_17.addWidget(self.mater_sel_all_b, 0, 2, 1, 1)

        self.mater_upd_b = QPushButton(self.materials)
        self.mater_upd_b.setObjectName(u"mater_upd_b")

        self.gridLayout_17.addWidget(self.mater_upd_b, 0, 6, 1, 1)

        self.mater_ins_b = QPushButton(self.materials)
        self.mater_ins_b.setObjectName(u"mater_ins_b")

        self.gridLayout_17.addWidget(self.mater_ins_b, 0, 8, 1, 1)

        self.mater_del_b = QPushButton(self.materials)
        self.mater_del_b.setObjectName(u"mater_del_b")

        self.gridLayout_17.addWidget(self.mater_del_b, 0, 7, 1, 1)

        self.mater_v = QTableView(self.materials)
        self.mater_v.setObjectName(u"mater_v")
        self.mater_v.setSortingEnabled(True)

        self.gridLayout_17.addWidget(self.mater_v, 1, 0, 1, 9)

        self.horizontalSpacer_6 = QSpacerItem(496, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.groupBox_10 = QGroupBox(self.materials)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_16 = QGridLayout(self.groupBox_10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.mater_name_e = QLineEdit(self.groupBox_10)
        self.mater_name_e.setObjectName(u"mater_name_e")

        self.gridLayout_16.addWidget(self.mater_name_e, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.mater_sel_b = QPushButton(self.materials)
        self.mater_sel_b.setObjectName(u"mater_sel_b")

        self.gridLayout_17.addWidget(self.mater_sel_b, 0, 1, 1, 1)

        self.mater_add_b = QPushButton(self.materials)
        self.mater_add_b.setObjectName(u"mater_add_b")

        self.gridLayout_17.addWidget(self.mater_add_b, 0, 4, 1, 1)

        self.tabWidget.addTab(self.materials, "")
        self.tasks = QWidget()
        self.tasks.setObjectName(u"tasks")
        self.gridLayout_19 = QGridLayout(self.tasks)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_12 = QGroupBox(self.tasks)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_20 = QGridLayout(self.groupBox_12)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.task_dt_e = QDateEdit(self.groupBox_12)
        self.task_dt_e.setObjectName(u"task_dt_e")
        self.task_dt_e.setCalendarPopup(True)

        self.gridLayout_20.addWidget(self.task_dt_e, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_12, 0, 1, 1, 1)

        self.task_sel_b = QPushButton(self.tasks)
        self.task_sel_b.setObjectName(u"task_sel_b")

        self.gridLayout_19.addWidget(self.task_sel_b, 0, 3, 1, 1)

        self.task_upd_b = QPushButton(self.tasks)
        self.task_upd_b.setObjectName(u"task_upd_b")

        self.gridLayout_19.addWidget(self.task_upd_b, 0, 5, 1, 1)

        self.task_del_b = QPushButton(self.tasks)
        self.task_del_b.setObjectName(u"task_del_b")

        self.gridLayout_19.addWidget(self.task_del_b, 0, 6, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(467, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.groupBox_11 = QGroupBox(self.tasks)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_18 = QGridLayout(self.groupBox_11)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.task_name_e = QLineEdit(self.groupBox_11)
        self.task_name_e.setObjectName(u"task_name_e")

        self.gridLayout_18.addWidget(self.task_name_e, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.task_ins_b = QPushButton(self.tasks)
        self.task_ins_b.setObjectName(u"task_ins_b")

        self.gridLayout_19.addWidget(self.task_ins_b, 0, 7, 1, 1)

        self.task_v = QTableView(self.tasks)
        self.task_v.setObjectName(u"task_v")
        self.task_v.setSortingEnabled(True)

        self.gridLayout_19.addWidget(self.task_v, 1, 0, 1, 8)

        self.groupBox_13 = QGroupBox(self.tasks)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_21 = QGridLayout(self.groupBox_13)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.task_status_s = QComboBox(self.groupBox_13)
        self.task_status_s.addItem("")
        self.task_status_s.addItem("")
        self.task_status_s.addItem("")
        self.task_status_s.addItem("")
        self.task_status_s.addItem("")
        self.task_status_s.setObjectName(u"task_status_s")

        self.gridLayout_21.addWidget(self.task_status_s, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_13, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tasks, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 997, 37))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.show_reminder_m)
        self.menu.addAction(self.salary_report)
        self.menu.addAction(self.reports)
        self.menu_3.addAction(self.save_db)
        self.menu_3.addAction(self.change_db)
        self.menu_4.addAction(self.edit_technical)
        self.menu_4.addAction(self.edit_users)
        self.menu_4.addAction(self.change_user)
        self.menu_2.addAction(self.make_trans)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoDent", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u043a\u0442\u043e\u0440\u0430", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443 \u0434\u043e\u043a\u0442\u043e\u0440\u043e\u0432", None))
        self.add_client.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.view_clients.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.view_doctors.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443 \u0434\u043e\u043a\u0442\u043e\u0440\u043e\u0432", None))
        self.add_doctor.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u043a\u0442\u043e\u0440\u0430", None))
        self.edit_users.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.change_user.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.show_reminder_m.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f \u043e \u043f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0438", None))
        self.save_db.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0411\u0414 \u043d\u0430 \u0441\u044a\u0435\u043c\u043d\u044b\u0439 \u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c", None))
        self.change_db.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0411\u0414 \u0432 \u043f\u0430\u043c\u044f\u0442\u0438 \u043a\u043b\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430", None))
        self.edit_technical.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043a\u043b\u0438\u043d\u0438\u043a\u0435", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.actionFFF.setText(QCoreApplication.translate("MainWindow", u"FFF", None))
        self.salary_report.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043f\u043e \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u0430\u043c \u0432\u0440\u0430\u0447\u0435\u0439", None))
        self.reports.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u044b", None))
        self.make_trans.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e \u0441\u043e \u0441\u0447\u0435\u0442\u043e\u043c \u043a\u043b\u0438\u043d\u0438\u043a\u0438", None))
        self.rec_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.rec_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.rec_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calendar), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.loan_search_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.client_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.client_add_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.client_search_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.client_edit_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f:", None))
        self.next_visit_dt_s.setItemText(0, "")
        self.next_visit_dt_s.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.next_visit_dt_s.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
        self.next_visit_dt_s.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clients), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.insur_sel_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.insur_sel_all_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.insur_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.insur_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.insur_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.insurances), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u044b\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.doctor_sel_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.doctor_sel_all_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.doctor_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.doctor_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.doctor_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.doctors), QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0447\u0438", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u041c\u041a\u0411 / \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 / \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.serv_sel_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.serv_sel_all_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.serv_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.serv_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.serv_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.services), QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.mater_sub_b.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.mater_sel_all_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435", None))
        self.mater_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.mater_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.mater_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430:", None))
        self.mater_sel_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.mater_add_b.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materials), QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0434\u043e:", None))
        self.task_dt_e.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.task_sel_b.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.task_upd_b.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.task_del_b.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.task_ins_b.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.task_status_s.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043d\u0430\u0447\u0430\u0442\u043e", None))
        self.task_status_s.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e", None))
        self.task_status_s.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.task_status_s.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.task_status_s.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041b\u044e\u0431\u043e\u0439", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasks), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0430\u043d\u0441\u044b", None))
    # retranslateUi

