# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientFindForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ClientFindForm(object):
    def setupUi(self, ClientFindForm):
        if not ClientFindForm.objectName():
            ClientFindForm.setObjectName(u"ClientFindForm")
        ClientFindForm.resize(1091, 478)
        font = QFont()
        font.setPointSize(14)
        ClientFindForm.setFont(font)
        self.gridLayout = QGridLayout(ClientFindForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(ClientFindForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ln_e = QLineEdit(self.groupBox)
        self.ln_e.setObjectName(u"ln_e")

        self.gridLayout_7.addWidget(self.ln_e, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(ClientFindForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.fn_e = QLineEdit(self.groupBox_2)
        self.fn_e.setObjectName(u"fn_e")

        self.gridLayout_8.addWidget(self.fn_e, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(ClientFindForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.mn_e = QLineEdit(self.groupBox_3)
        self.mn_e.setObjectName(u"mn_e")

        self.gridLayout_9.addWidget(self.mn_e, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.sel_b = QPushButton(ClientFindForm)
        self.sel_b.setObjectName(u"sel_b")

        self.gridLayout.addWidget(self.sel_b, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(233, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.ins_b = QPushButton(ClientFindForm)
        self.ins_b.setObjectName(u"ins_b")

        self.gridLayout.addWidget(self.ins_b, 0, 5, 1, 1)

        self.view = QTableView(ClientFindForm)
        self.view.setObjectName(u"view")
        self.view.setSortingEnabled(True)

        self.gridLayout.addWidget(self.view, 1, 0, 1, 6)


        self.retranslateUi(ClientFindForm)

        QMetaObject.connectSlotsByName(ClientFindForm)
    # setupUi

    def retranslateUi(self, ClientFindForm):
        ClientFindForm.setWindowTitle(QCoreApplication.translate("ClientFindForm", u"\u041f\u043e\u0438\u0441\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("ClientFindForm", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ClientFindForm", u"\u0418\u043c\u044f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ClientFindForm", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.sel_b.setText(QCoreApplication.translate("ClientFindForm", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.ins_b.setText(QCoreApplication.translate("ClientFindForm", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

