# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_configForm(object):
    def setupUi(self, configForm):
        if not configForm.objectName():
            configForm.setObjectName(u"configForm")
        configForm.resize(405, 93)
        font = QFont()
        font.setPointSize(14)
        configForm.setFont(font)
        self.gridLayout_3 = QGridLayout(configForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.saveButton = QPushButton(configForm)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(125, 0))

        self.gridLayout_3.addWidget(self.saveButton, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.cancelButton = QPushButton(configForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(125, 0))

        self.gridLayout_3.addWidget(self.cancelButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.groupBox = QGroupBox(configForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dbEdit = QLineEdit(self.groupBox)
        self.dbEdit.setObjectName(u"dbEdit")
        self.dbEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.dbEdit, 0, 0, 1, 1)

        self.dbButton = QPushButton(self.groupBox)
        self.dbButton.setObjectName(u"dbButton")
        self.dbButton.setMinimumSize(QSize(75, 0))

        self.gridLayout.addWidget(self.dbButton, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 5)


        self.retranslateUi(configForm)

        QMetaObject.connectSlotsByName(configForm)
    # setupUi

    def retranslateUi(self, configForm):
        configForm.setWindowTitle(QCoreApplication.translate("configForm", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.saveButton.setText(QCoreApplication.translate("configForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("configForm", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("configForm", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.dbButton.setText(QCoreApplication.translate("configForm", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

