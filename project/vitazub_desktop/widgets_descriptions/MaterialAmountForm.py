# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaterialAmountForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MaterialAmountForm(object):
    def setupUi(self, MaterialAmountForm):
        if not MaterialAmountForm.objectName():
            MaterialAmountForm.setObjectName(u"MaterialAmountForm")
        MaterialAmountForm.resize(237, 92)
        font = QFont()
        font.setPointSize(14)
        MaterialAmountForm.setFont(font)
        self.gridLayout_3 = QGridLayout(MaterialAmountForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(MaterialAmountForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.amount_e = QSpinBox(self.groupBox)
        self.amount_e.setObjectName(u"amount_e")
        self.amount_e.setMinimum(1)
        self.amount_e.setMaximum(10000)

        self.gridLayout.addWidget(self.amount_e, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 3)

        self.cancel_b = QPushButton(MaterialAmountForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_3.addWidget(self.cancel_b, 1, 0, 1, 1)

        self.add_b = QPushButton(MaterialAmountForm)
        self.add_b.setObjectName(u"add_b")

        self.gridLayout_3.addWidget(self.add_b, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.retranslateUi(MaterialAmountForm)

        QMetaObject.connectSlotsByName(MaterialAmountForm)
    # setupUi

    def retranslateUi(self, MaterialAmountForm):
        MaterialAmountForm.setWindowTitle(QCoreApplication.translate("MaterialAmountForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("MaterialAmountForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.cancel_b.setText(QCoreApplication.translate("MaterialAmountForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.add_b.setText(QCoreApplication.translate("MaterialAmountForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

