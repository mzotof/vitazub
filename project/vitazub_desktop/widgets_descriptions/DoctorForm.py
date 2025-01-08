# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DoctorForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DoctorForm(object):
    def setupUi(self, DoctorForm):
        if not DoctorForm.objectName():
            DoctorForm.setObjectName(u"DoctorForm")
        DoctorForm.resize(499, 320)
        font = QFont()
        font.setPointSize(14)
        DoctorForm.setFont(font)
        self.gridLayout_9 = QGridLayout(DoctorForm)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_2 = QGroupBox(DoctorForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ln_e = QLineEdit(self.groupBox_2)
        self.ln_e.setObjectName(u"ln_e")
        self.ln_e.setMinimumSize(QSize(200, 0))
        self.ln_e.setReadOnly(False)

        self.gridLayout_2.addWidget(self.ln_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_2, 0, 0, 1, 3)

        self.groupBox = QGroupBox(DoctorForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fn_e = QLineEdit(self.groupBox)
        self.fn_e.setObjectName(u"fn_e")
        self.fn_e.setMinimumSize(QSize(200, 0))
        self.fn_e.setReadOnly(False)

        self.gridLayout.addWidget(self.fn_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 1, 3)

        self.groupBox_3 = QGroupBox(DoctorForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.phone_e = QLineEdit(self.groupBox_3)
        self.phone_e.setObjectName(u"phone_e")
        self.phone_e.setMinimumSize(QSize(200, 0))
        self.phone_e.setReadOnly(False)

        self.gridLayout_3.addWidget(self.phone_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_3, 1, 3, 1, 3)

        self.groupBox_4 = QGroupBox(DoctorForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mn_e = QLineEdit(self.groupBox_4)
        self.mn_e.setObjectName(u"mn_e")
        self.mn_e.setMinimumSize(QSize(200, 0))
        self.mn_e.setReadOnly(False)

        self.gridLayout_4.addWidget(self.mn_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 2, 0, 1, 3)

        self.groupBox_5 = QGroupBox(DoctorForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.phone2_e = QLineEdit(self.groupBox_5)
        self.phone2_e.setObjectName(u"phone2_e")
        self.phone2_e.setMinimumSize(QSize(200, 0))
        self.phone2_e.setReadOnly(False)

        self.gridLayout_5.addWidget(self.phone2_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 2, 3, 1, 3)

        self.groupBox_8 = QGroupBox(DoctorForm)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_8 = QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.spec_s = QComboBox(self.groupBox_8)
        self.spec_s.setObjectName(u"spec_s")

        self.gridLayout_8.addWidget(self.spec_s, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_8, 3, 0, 1, 6)

        self.groupBox_7 = QGroupBox(DoctorForm)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_7 = QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.comment_e = QLineEdit(self.groupBox_7)
        self.comment_e.setObjectName(u"comment_e")
        self.comment_e.setMinimumSize(QSize(200, 0))
        self.comment_e.setReadOnly(False)

        self.gridLayout_7.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_7, 4, 0, 1, 6)

        self.cancel_b = QPushButton(DoctorForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_9.addWidget(self.cancel_b, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.del_b = QPushButton(DoctorForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_9.addWidget(self.del_b, 5, 2, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(129, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 5, 4, 1, 1)

        self.save_b = QPushButton(DoctorForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_9.addWidget(self.save_b, 5, 5, 1, 1)

        self.groupBox_6 = QGroupBox(DoctorForm)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.rate_e = QSpinBox(self.groupBox_6)
        self.rate_e.setObjectName(u"rate_e")
        self.rate_e.setMaximum(100)

        self.gridLayout_6.addWidget(self.rate_e, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 0, 3, 1, 3)

        QWidget.setTabOrder(self.ln_e, self.fn_e)
        QWidget.setTabOrder(self.fn_e, self.mn_e)
        QWidget.setTabOrder(self.mn_e, self.phone_e)
        QWidget.setTabOrder(self.phone_e, self.phone2_e)
        QWidget.setTabOrder(self.phone2_e, self.save_b)
        QWidget.setTabOrder(self.save_b, self.cancel_b)

        self.retranslateUi(DoctorForm)

        QMetaObject.connectSlotsByName(DoctorForm)
    # setupUi

    def retranslateUi(self, DoctorForm):
        DoctorForm.setWindowTitle(QCoreApplication.translate("DoctorForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0442\u043e\u0440\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DoctorForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.groupBox.setTitle(QCoreApplication.translate("DoctorForm", u"\u0418\u043c\u044f:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DoctorForm", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("DoctorForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("DoctorForm", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("DoctorForm", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("DoctorForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.cancel_b.setText(QCoreApplication.translate("DoctorForm", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.del_b.setText(QCoreApplication.translate("DoctorForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.save_b.setText(QCoreApplication.translate("DoctorForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("DoctorForm", u"\u0421\u0442\u0430\u0432\u043a\u0430:", None))
    # retranslateUi

