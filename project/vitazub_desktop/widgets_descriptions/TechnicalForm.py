# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TechnicalForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TechnicalForm(object):
    def setupUi(self, TechnicalForm):
        if not TechnicalForm.objectName():
            TechnicalForm.setObjectName(u"TechnicalForm")
        TechnicalForm.resize(193, 206)
        font = QFont()
        font.setPointSize(14)
        TechnicalForm.setFont(font)
        self.gridLayout_4 = QGridLayout(TechnicalForm)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(TechnicalForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_e = QLineEdit(self.groupBox)
        self.name_e.setObjectName(u"name_e")

        self.gridLayout.addWidget(self.name_e, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(TechnicalForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.start_tm_e = QTimeEdit(self.groupBox_2)
        self.start_tm_e.setObjectName(u"start_tm_e")

        self.gridLayout_2.addWidget(self.start_tm_e, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox_3 = QGroupBox(TechnicalForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.end_tm_e = QTimeEdit(self.groupBox_3)
        self.end_tm_e.setObjectName(u"end_tm_e")

        self.gridLayout_3.addWidget(self.end_tm_e, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.cancel_b = QPushButton(TechnicalForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_4.addWidget(self.cancel_b, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.save_b = QPushButton(TechnicalForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_4.addWidget(self.save_b, 3, 2, 1, 1)


        self.retranslateUi(TechnicalForm)

        QMetaObject.connectSlotsByName(TechnicalForm)
    # setupUi

    def retranslateUi(self, TechnicalForm):
        TechnicalForm.setWindowTitle(QCoreApplication.translate("TechnicalForm", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043a\u043b\u0438\u043d\u0438\u043a\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("TechnicalForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u043d\u0438\u043a\u0438:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TechnicalForm", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u043b\u0438\u043d\u0438\u043a\u0438:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TechnicalForm", u"\u041a\u043e\u043d\u0435\u0446 \u0440\u0430\u0431\u043e\u0442\u044b \u043a\u043b\u0438\u043d\u0438\u043a\u0438:", None))
        self.cancel_b.setText(QCoreApplication.translate("TechnicalForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_b.setText(QCoreApplication.translate("TechnicalForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

