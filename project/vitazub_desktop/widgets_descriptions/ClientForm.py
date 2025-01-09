# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClientForm(object):
    def setupUi(self, ClientForm):
        if not ClientForm.objectName():
            ClientForm.setObjectName(u"ClientForm")
        ClientForm.setBaseSize(QSize(444, 320))
        font = QFont()
        font.setPointSize(14)
        ClientForm.setFont(font)
        self.gridLayout_10 = QGridLayout(ClientForm)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(223, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 8, 1, 1, 4)

        self.gridGroupBox = QGroupBox(ClientForm)
        self.gridGroupBox.setObjectName(u"gridGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gridGroupBox.sizePolicy().hasHeightForWidth())
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.gridGroupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.notified_s = QCheckBox(self.gridGroupBox)
        self.notified_s.setObjectName(u"notified_s")
        self.notified_s.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.notified_s.sizePolicy().hasHeightForWidth())
        self.notified_s.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.notified_s, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.gridGroupBox, 1, 6, 2, 2)

        self.insur_b = QPushButton(ClientForm)
        self.insur_b.setObjectName(u"insur_b")

        self.gridLayout_10.addWidget(self.insur_b, 7, 0, 1, 2)

        self.groupBox = QGroupBox(ClientForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fn_e = QLineEdit(self.groupBox)
        self.fn_e.setObjectName(u"fn_e")
        sizePolicy1.setHeightForWidth(self.fn_e.sizePolicy().hasHeightForWidth())
        self.fn_e.setSizePolicy(sizePolicy1)
        self.fn_e.setMinimumSize(QSize(200, 0))
        self.fn_e.setReadOnly(False)

        self.gridLayout.addWidget(self.fn_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 4, 0, 1, 3)

        self.groupBox_3 = QGroupBox(ClientForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.phone_e = QLineEdit(self.groupBox_3)
        self.phone_e.setObjectName(u"phone_e")
        sizePolicy1.setHeightForWidth(self.phone_e.sizePolicy().hasHeightForWidth())
        self.phone_e.setSizePolicy(sizePolicy1)
        self.phone_e.setMinimumSize(QSize(200, 0))
        self.phone_e.setReadOnly(False)

        self.gridLayout_3.addWidget(self.phone_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 4, 3, 1, 5)

        self.groupBox_9 = QGroupBox(ClientForm)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.balance_e = QDoubleSpinBox(self.groupBox_9)
        self.balance_e.setObjectName(u"balance_e")
        self.balance_e.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.balance_e.setMaximum(1000000.000000000000000)

        self.gridLayout_9.addWidget(self.balance_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_9, 6, 6, 1, 2)

        self.save_b = QPushButton(ClientForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_10.addWidget(self.save_b, 8, 7, 1, 1)

        self.cancel_b = QPushButton(ClientForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_10.addWidget(self.cancel_b, 8, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 7, 2, 1, 2)

        self.groupBox_6 = QGroupBox(ClientForm)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.birth_dt_e = QDateEdit(self.groupBox_6)
        self.birth_dt_e.setObjectName(u"birth_dt_e")
        self.birth_dt_e.setMinimumSize(QSize(0, 0))
        self.birth_dt_e.setDateTime(QDateTime(QDate(1900, 1, 1), QTime(0, 0, 0)))
        self.birth_dt_e.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.birth_dt_e.setCalendarPopup(True)
        self.birth_dt_e.setDate(QDate(1900, 1, 1))

        self.gridLayout_6.addWidget(self.birth_dt_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_6, 1, 3, 2, 3)

        self.groupBox_7 = QGroupBox(ClientForm)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.discount_e = QSpinBox(self.groupBox_7)
        self.discount_e.setObjectName(u"discount_e")
        self.discount_e.setMinimumSize(QSize(0, 0))
        self.discount_e.setMaximum(100)
        self.discount_e.setSingleStep(5)

        self.gridLayout_7.addWidget(self.discount_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_7, 6, 3, 1, 3)

        self.del_b = QPushButton(ClientForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_10.addWidget(self.del_b, 8, 5, 1, 2)

        self.change_bal_b = QPushButton(ClientForm)
        self.change_bal_b.setObjectName(u"change_bal_b")

        self.gridLayout_10.addWidget(self.change_bal_b, 7, 4, 1, 4)

        self.groupBox_5 = QGroupBox(ClientForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.phone2_e = QLineEdit(self.groupBox_5)
        self.phone2_e.setObjectName(u"phone2_e")
        sizePolicy1.setHeightForWidth(self.phone2_e.sizePolicy().hasHeightForWidth())
        self.phone2_e.setSizePolicy(sizePolicy1)
        self.phone2_e.setMinimumSize(QSize(200, 0))
        self.phone2_e.setReadOnly(False)

        self.gridLayout_5.addWidget(self.phone2_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_5, 5, 3, 1, 5)

        self.groupBox_8 = QGroupBox(ClientForm)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy2.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy2)
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.comment_e = QLineEdit(self.groupBox_8)
        self.comment_e.setObjectName(u"comment_e")
        self.comment_e.setMinimumSize(QSize(200, 0))
        self.comment_e.setReadOnly(False)

        self.gridLayout_8.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_8, 6, 0, 1, 3)

        self.groupBox_2 = QGroupBox(ClientForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ln_e = QLineEdit(self.groupBox_2)
        self.ln_e.setObjectName(u"ln_e")
        sizePolicy1.setHeightForWidth(self.ln_e.sizePolicy().hasHeightForWidth())
        self.ln_e.setSizePolicy(sizePolicy1)
        self.ln_e.setMinimumSize(QSize(200, 0))
        self.ln_e.setReadOnly(False)

        self.gridLayout_2.addWidget(self.ln_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 1, 0, 2, 3)

        self.groupBox_4 = QGroupBox(ClientForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mn_e = QLineEdit(self.groupBox_4)
        self.mn_e.setObjectName(u"mn_e")
        sizePolicy1.setHeightForWidth(self.mn_e.sizePolicy().hasHeightForWidth())
        self.mn_e.setSizePolicy(sizePolicy1)
        self.mn_e.setMinimumSize(QSize(200, 0))
        self.mn_e.setReadOnly(False)

        self.gridLayout_4.addWidget(self.mn_e, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_4, 5, 0, 1, 3)

        QWidget.setTabOrder(self.ln_e, self.fn_e)
        QWidget.setTabOrder(self.fn_e, self.mn_e)
        QWidget.setTabOrder(self.mn_e, self.birth_dt_e)
        QWidget.setTabOrder(self.birth_dt_e, self.discount_e)
        QWidget.setTabOrder(self.discount_e, self.phone_e)
        QWidget.setTabOrder(self.phone_e, self.phone2_e)
        QWidget.setTabOrder(self.phone2_e, self.comment_e)
        QWidget.setTabOrder(self.comment_e, self.save_b)
        QWidget.setTabOrder(self.save_b, self.cancel_b)

        self.retranslateUi(ClientForm)

        QMetaObject.connectSlotsByName(ClientForm)
    # setupUi

    def retranslateUi(self, ClientForm):
        ClientForm.setWindowTitle(QCoreApplication.translate("ClientForm", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.notified_s.setText(QCoreApplication.translate("ClientForm", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d \u043e\n"
"\u0441\u043b\u0435\u0434. \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0438", None))
        self.insur_b.setText(QCoreApplication.translate("ClientForm", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClientForm", u"\u0418\u043c\u044f:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ClientForm", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("ClientForm", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u0430:", None))
        self.save_b.setText(QCoreApplication.translate("ClientForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_b.setText(QCoreApplication.translate("ClientForm", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ClientForm", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.birth_dt_e.setDisplayFormat(QCoreApplication.translate("ClientForm", u"yyyy-MM-dd", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ClientForm", u"\u0421\u043a\u0438\u0434\u043a\u0430 (0-100):", None))
        self.del_b.setText(QCoreApplication.translate("ClientForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.change_bal_b.setText(QCoreApplication.translate("ClientForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ClientForm", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ClientForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ClientForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ClientForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
    # retranslateUi

