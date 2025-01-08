# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowUsersForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShowUsersForm(object):
    def setupUi(self, ShowUsersForm):
        if not ShowUsersForm.objectName():
            ShowUsersForm.setObjectName(u"ShowUsersForm")
        ShowUsersForm.resize(428, 287)
        font = QFont()
        font.setPointSize(14)
        ShowUsersForm.setFont(font)
        self.gridLayout = QGridLayout(ShowUsersForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ins_b = QPushButton(ShowUsersForm)
        self.ins_b.setObjectName(u"ins_b")

        self.gridLayout.addWidget(self.ins_b, 1, 4, 1, 1)

        self.upd_b = QPushButton(ShowUsersForm)
        self.upd_b.setObjectName(u"upd_b")

        self.gridLayout.addWidget(self.upd_b, 1, 2, 1, 1)

        self.del_b = QPushButton(ShowUsersForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout.addWidget(self.del_b, 1, 3, 1, 1)

        self.cancel_b = QPushButton(ShowUsersForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout.addWidget(self.cancel_b, 1, 0, 1, 1)

        self.view = QTableView(ShowUsersForm)
        self.view.setObjectName(u"view")

        self.gridLayout.addWidget(self.view, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        QWidget.setTabOrder(self.ins_b, self.view)
        QWidget.setTabOrder(self.view, self.upd_b)
        QWidget.setTabOrder(self.upd_b, self.del_b)
        QWidget.setTabOrder(self.del_b, self.cancel_b)

        self.retranslateUi(ShowUsersForm)

        QMetaObject.connectSlotsByName(ShowUsersForm)
    # setupUi

    def retranslateUi(self, ShowUsersForm):
        ShowUsersForm.setWindowTitle(QCoreApplication.translate("ShowUsersForm", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.ins_b.setText(QCoreApplication.translate("ShowUsersForm", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.upd_b.setText(QCoreApplication.translate("ShowUsersForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.del_b.setText(QCoreApplication.translate("ShowUsersForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cancel_b.setText(QCoreApplication.translate("ShowUsersForm", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

