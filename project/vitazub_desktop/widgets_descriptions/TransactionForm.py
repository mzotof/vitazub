# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransactionForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TransactionForm(object):
    def setupUi(self, TransactionForm):
        if not TransactionForm.objectName():
            TransactionForm.setObjectName(u"TransactionForm")
        TransactionForm.resize(385, 206)
        font = QFont()
        font.setPointSize(14)
        TransactionForm.setFont(font)
        self.gridLayout_4 = QGridLayout(TransactionForm)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(TransactionForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.trans_source_s = QComboBox(self.groupBox)
        self.trans_source_s.addItem("")
        self.trans_source_s.addItem("")
        self.trans_source_s.addItem("")
        self.trans_source_s.setObjectName(u"trans_source_s")

        self.gridLayout.addWidget(self.trans_source_s, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(TransactionForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.amount_e = QDoubleSpinBox(self.groupBox_2)
        self.amount_e.setObjectName(u"amount_e")
        self.amount_e.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.amount_e.setDecimals(2)
        self.amount_e.setMinimum(-1000000.000000000000000)
        self.amount_e.setMaximum(1000000.000000000000000)

        self.gridLayout_2.addWidget(self.amount_e, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.groupBox_3 = QGroupBox(TransactionForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comment_e = QLineEdit(self.groupBox_3)
        self.comment_e.setObjectName(u"comment_e")

        self.gridLayout_3.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.cancel_b = QPushButton(TransactionForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_4.addWidget(self.cancel_b, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.make_b = QPushButton(TransactionForm)
        self.make_b.setObjectName(u"make_b")

        self.gridLayout_4.addWidget(self.make_b, 3, 2, 1, 1)


        self.retranslateUi(TransactionForm)

        QMetaObject.connectSlotsByName(TransactionForm)
    # setupUi

    def retranslateUi(self, TransactionForm):
        TransactionForm.setWindowTitle(QCoreApplication.translate("TransactionForm", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0431\u0430\u043b\u0430\u043d\u0441\u0430 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("TransactionForm", u"\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438:", None))
        self.trans_source_s.setItemText(0, QCoreApplication.translate("TransactionForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438...", None))
        self.trans_source_s.setItemText(1, QCoreApplication.translate("TransactionForm", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u0435", None))
        self.trans_source_s.setItemText(2, QCoreApplication.translate("TransactionForm", u"\u0411\u0435\u0437\u043d\u0430\u043b\u0438\u0447\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0435\u0442", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("TransactionForm", u"\u0421\u0443\u043c\u043c\u0430:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TransactionForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.cancel_b.setText(QCoreApplication.translate("TransactionForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.make_b.setText(QCoreApplication.translate("TransactionForm", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

