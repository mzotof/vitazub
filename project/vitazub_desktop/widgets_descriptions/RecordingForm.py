# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecordingForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RecordingForm(object):
    def setupUi(self, RecordingForm):
        if not RecordingForm.objectName():
            RecordingForm.setObjectName(u"RecordingForm")
        RecordingForm.resize(949, 770)
        font = QFont()
        font.setPointSize(14)
        RecordingForm.setFont(font)
        self.gridLayout_19 = QGridLayout(RecordingForm)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_9 = QGroupBox(RecordingForm)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_9 = QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_10 = QGridLayout(self.groupBox_11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.serv_e = QLineEdit(self.groupBox_11)
        self.serv_e.setObjectName(u"serv_e")

        self.gridLayout_10.addWidget(self.serv_e, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_11)

        self.groupBox_15 = QGroupBox(self.groupBox_9)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_15 = QGridLayout(self.groupBox_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.to_pay_e = QDoubleSpinBox(self.groupBox_15)
        self.to_pay_e.setObjectName(u"to_pay_e")
        self.to_pay_e.setReadOnly(True)
        self.to_pay_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.to_pay_e.setMaximum(1000000.000000000000000)
        self.to_pay_e.setSingleStep(100.000000000000000)

        self.gridLayout_15.addWidget(self.to_pay_e, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_15)

        self.groupBox_8 = QGroupBox(self.groupBox_9)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_5 = QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.discount_e = QSpinBox(self.groupBox_8)
        self.discount_e.setObjectName(u"discount_e")
        self.discount_e.setMaximum(100)

        self.gridLayout_5.addWidget(self.discount_e, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_8)

        self.groupBox_17 = QGroupBox(self.groupBox_9)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_17 = QGridLayout(self.groupBox_17)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.payed_e = QDoubleSpinBox(self.groupBox_17)
        self.payed_e.setObjectName(u"payed_e")
        self.payed_e.setReadOnly(True)
        self.payed_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.payed_e.setMaximum(1000000.000000000000000)
        self.payed_e.setSingleStep(100.000000000000000)

        self.gridLayout_17.addWidget(self.payed_e, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_17)

        self.groupBox_20 = QGroupBox(self.groupBox_9)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_22 = QGridLayout(self.groupBox_20)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.total_to_pay_e = QDoubleSpinBox(self.groupBox_20)
        self.total_to_pay_e.setObjectName(u"total_to_pay_e")
        self.total_to_pay_e.setReadOnly(True)
        self.total_to_pay_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.total_to_pay_e.setMaximum(1000000.000000000000000)
        self.total_to_pay_e.setSingleStep(100.000000000000000)

        self.gridLayout_22.addWidget(self.total_to_pay_e, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_20)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 0, 1, 4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_12 = QGroupBox(self.groupBox_9)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.groupBox_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.serv_v = QTableView(self.groupBox_12)
        self.serv_v.setObjectName(u"serv_v")
        sizePolicy.setHeightForWidth(self.serv_v.sizePolicy().hasHeightForWidth())
        self.serv_v.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        self.serv_v.setFont(font1)

        self.gridLayout_13.addWidget(self.serv_v, 0, 0, 6, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_12)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 121, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.serv_sel_b = QPushButton(self.groupBox_9)
        self.serv_sel_b.setObjectName(u"serv_sel_b")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.serv_sel_b.sizePolicy().hasHeightForWidth())
        self.serv_sel_b.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.serv_sel_b)

        self.serv_unsel_b = QPushButton(self.groupBox_9)
        self.serv_unsel_b.setObjectName(u"serv_unsel_b")
        sizePolicy1.setHeightForWidth(self.serv_unsel_b.sizePolicy().hasHeightForWidth())
        self.serv_unsel_b.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.serv_unsel_b)

        self.verticalSpacer_2 = QSpacerItem(20, 121, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.groupBox_13 = QGroupBox(self.groupBox_9)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy)
        self.gridLayout_14 = QGridLayout(self.groupBox_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.serv_sel_v = QTableView(self.groupBox_13)
        self.serv_sel_v.setObjectName(u"serv_sel_v")
        sizePolicy.setHeightForWidth(self.serv_sel_v.sizePolicy().hasHeightForWidth())
        self.serv_sel_v.setSizePolicy(sizePolicy)
        self.serv_sel_v.setFont(font1)

        self.gridLayout_14.addWidget(self.serv_sel_v, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_13)


        self.gridLayout_9.addLayout(self.horizontalLayout_6, 1, 0, 1, 4)


        self.gridLayout_19.addWidget(self.groupBox_9, 7, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer, 9, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_2, 9, 3, 1, 1)

        self.save_b = QPushButton(RecordingForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_19.addWidget(self.save_b, 9, 4, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_4 = QGroupBox(RecordingForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.start_time_e = QTimeEdit(self.groupBox_4)
        self.start_time_e.setObjectName(u"start_time_e")
        self.start_time_e.setReadOnly(False)
        self.start_time_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.start_time_e.setProperty("showGroupSeparator", False)
        self.start_time_e.setMaximumTime(QTime(21, 59, 59))
        self.start_time_e.setMinimumTime(QTime(9, 0, 0))
        self.start_time_e.setCalendarPopup(False)
        self.start_time_e.setTime(QTime(9, 0, 0))

        self.gridLayout_6.addWidget(self.start_time_e, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_4, 1, 2, 1, 1)

        self.groupBox_5 = QGroupBox(RecordingForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.end_time_e = QTimeEdit(self.groupBox_5)
        self.end_time_e.setObjectName(u"end_time_e")
        self.end_time_e.setReadOnly(False)
        self.end_time_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.end_time_e.setMaximumTime(QTime(22, 0, 0))
        self.end_time_e.setMinimumTime(QTime(9, 0, 0))
        self.end_time_e.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.end_time_e.setTime(QTime(9, 0, 0))

        self.gridLayout_7.addWidget(self.end_time_e, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_5, 1, 3, 1, 1)

        self.groupBox_10 = QGroupBox(RecordingForm)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.comment_e = QLineEdit(self.groupBox_10)
        self.comment_e.setObjectName(u"comment_e")

        self.gridLayout_12.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_10, 2, 0, 1, 4)

        self.groupBox_2 = QGroupBox(RecordingForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.doctor = QLineEdit(self.groupBox_2)
        self.doctor.setObjectName(u"doctor")
        self.doctor.setReadOnly(True)

        self.gridLayout_2.addWidget(self.doctor, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_2, 0, 0, 1, 4)

        self.groupBox_6 = QGroupBox(RecordingForm)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_8 = QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.date = QDateEdit(self.groupBox_6)
        self.date.setObjectName(u"date")
        self.date.setReadOnly(True)
        self.date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.gridLayout_8.addWidget(self.date, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_6, 1, 0, 1, 2)


        self.gridLayout_19.addLayout(self.gridLayout_11, 0, 0, 3, 2)

        self.del_b = QPushButton(RecordingForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_19.addWidget(self.del_b, 9, 2, 1, 1)

        self.cancel_b = QPushButton(RecordingForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_19.addWidget(self.cancel_b, 9, 0, 1, 1)

        self.groupBox_14 = QGroupBox(RecordingForm)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_18 = QGridLayout(self.groupBox_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_16 = QGridLayout(self.groupBox_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.payment_source_s = QComboBox(self.groupBox_16)
        self.payment_source_s.setObjectName(u"payment_source_s")

        self.gridLayout_16.addWidget(self.payment_source_s, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_16, 0, 0, 1, 4)

        self.pay_b = QPushButton(self.groupBox_14)
        self.pay_b.setObjectName(u"pay_b")

        self.gridLayout_18.addWidget(self.pay_b, 3, 3, 1, 1)

        self.pay_all_b = QPushButton(self.groupBox_14)
        self.pay_all_b.setObjectName(u"pay_all_b")

        self.gridLayout_18.addWidget(self.pay_all_b, 4, 3, 1, 1)

        self.groupBox_19 = QGroupBox(self.groupBox_14)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_21 = QGridLayout(self.groupBox_19)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.pay_comment_e = QLineEdit(self.groupBox_19)
        self.pay_comment_e.setObjectName(u"pay_comment_e")

        self.gridLayout_21.addWidget(self.pay_comment_e, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_19, 3, 2, 2, 1)

        self.groupBox_18 = QGroupBox(self.groupBox_14)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_20 = QGridLayout(self.groupBox_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.sum = QDoubleSpinBox(self.groupBox_18)
        self.sum.setObjectName(u"sum")
        self.sum.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.sum.setMinimum(-1000000.000000000000000)
        self.sum.setMaximum(1000000.000000000000000)
        self.sum.setSingleStep(100.000000000000000)

        self.gridLayout_20.addWidget(self.sum, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_18, 3, 0, 2, 2)


        self.gridLayout_19.addWidget(self.groupBox_14, 8, 0, 1, 5)

        self.verticalGroupBox_2 = QGroupBox(RecordingForm)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.client_find_b = QPushButton(self.verticalGroupBox_2)
        self.client_find_b.setObjectName(u"client_find_b")

        self.verticalLayout_2.addWidget(self.client_find_b)

        self.groupBox = QGroupBox(self.verticalGroupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.client_name = QLineEdit(self.groupBox)
        self.client_name.setObjectName(u"client_name")
        self.client_name.setReadOnly(True)

        self.gridLayout.addWidget(self.client_name, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.verticalGroupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.phone = QLineEdit(self.groupBox_3)
        self.phone.setObjectName(u"phone")
        self.phone.setReadOnly(True)

        self.gridLayout_3.addWidget(self.phone, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(self.verticalGroupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_4 = QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.phone2 = QLineEdit(self.groupBox_7)
        self.phone2.setObjectName(u"phone2")
        self.phone2.setReadOnly(True)

        self.gridLayout_4.addWidget(self.phone2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_7)


        self.gridLayout_19.addWidget(self.verticalGroupBox_2, 0, 2, 3, 3)


        self.retranslateUi(RecordingForm)

        QMetaObject.connectSlotsByName(RecordingForm)
    # setupUi

    def retranslateUi(self, RecordingForm):
        RecordingForm.setWindowTitle(QCoreApplication.translate("RecordingForm", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("RecordingForm", u"\u041e\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("RecordingForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u041c\u041a\u0411 / \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 / \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e:", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("RecordingForm", u"\u0412\u0441\u0435\u0433\u043e \u043a \u043e\u043f\u043b\u0430\u0442\u0435:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("RecordingForm", u"\u0421\u043a\u0438\u0434\u043a\u0430:", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("RecordingForm", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e:", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("RecordingForm", u"\u0418\u0442\u043e\u0433\u043e \u043a \u043e\u043f\u043b\u0430\u0442\u0435:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("RecordingForm", u"\u0412\u0441\u0435 \u0443\u0441\u043b\u0443\u0433\u0438:", None))
        self.serv_sel_b.setText(QCoreApplication.translate("RecordingForm", u">", None))
        self.serv_unsel_b.setText(QCoreApplication.translate("RecordingForm", u"<", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("RecordingForm", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438:", None))
        self.save_b.setText(QCoreApplication.translate("RecordingForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("RecordingForm", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0441\u0435\u0430\u043d\u0441\u0430:", None))
        self.start_time_e.setDisplayFormat(QCoreApplication.translate("RecordingForm", u"HH:mm", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("RecordingForm", u"\u041a\u043e\u043d\u0435\u0446 \u0441\u0435\u0430\u043d\u0441\u0430:", None))
        self.end_time_e.setDisplayFormat(QCoreApplication.translate("RecordingForm", u"HH:mm", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("RecordingForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RecordingForm", u"\u0412\u0440\u0430\u0447", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("RecordingForm", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0438\u0441\u0438:", None))
        self.date.setDisplayFormat(QCoreApplication.translate("RecordingForm", u"yyyy-MM-dd", None))
        self.del_b.setText(QCoreApplication.translate("RecordingForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cancel_b.setText(QCoreApplication.translate("RecordingForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("RecordingForm", u"\u041e\u043f\u043b\u0430\u0442\u0430:", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("RecordingForm", u"\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u043e\u043f\u043b\u0430\u0442\u044b:", None))
        self.pay_b.setText(QCoreApplication.translate("RecordingForm", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
        self.pay_all_b.setText(QCoreApplication.translate("RecordingForm", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("RecordingForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("RecordingForm", u"\u0421\u0443\u043c\u043c\u0430:", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("RecordingForm", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.client_find_b.setText(QCoreApplication.translate("RecordingForm", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("RecordingForm", u"\u0424\u0418\u041e:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RecordingForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("RecordingForm", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d:", None))
    # retranslateUi

