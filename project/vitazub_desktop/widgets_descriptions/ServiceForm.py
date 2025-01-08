# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ServiceForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ServiceForm(object):
    def setupUi(self, ServiceForm):
        if not ServiceForm.objectName():
            ServiceForm.setObjectName(u"ServiceForm")
        ServiceForm.resize(304, 320)
        font = QFont()
        font.setPointSize(14)
        ServiceForm.setFont(font)
        self.gridLayout_6 = QGridLayout(ServiceForm)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cancel_b = QPushButton(ServiceForm)
        self.cancel_b.setObjectName(u"cancel_b")

        self.gridLayout_6.addWidget(self.cancel_b, 5, 0, 1, 1)

        self.del_b = QPushButton(ServiceForm)
        self.del_b.setObjectName(u"del_b")

        self.gridLayout_6.addWidget(self.del_b, 5, 1, 1, 1)

        self.save_b = QPushButton(ServiceForm)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout_6.addWidget(self.save_b, 5, 2, 1, 1)

        self.groupBox_2 = QGroupBox(ServiceForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comment_e = QLineEdit(self.groupBox_2)
        self.comment_e.setObjectName(u"comment_e")

        self.gridLayout_2.addWidget(self.comment_e, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 4, 0, 1, 3)

        self.groupBox_4 = QGroupBox(ServiceForm)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.price_e = QDoubleSpinBox(self.groupBox_4)
        self.price_e.setObjectName(u"price_e")
        self.price_e.setMaximum(9999999.990000000223517)
        self.price_e.setSingleStep(100.000000000000000)

        self.gridLayout_4.addWidget(self.price_e, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_4, 3, 0, 1, 3)

        self.groupBox = QGroupBox(ServiceForm)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_e = QLineEdit(self.groupBox)
        self.name_e.setObjectName(u"name_e")

        self.gridLayout.addWidget(self.name_e, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 3)

        self.groupBox_3 = QGroupBox(ServiceForm)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mkb_e = QLineEdit(self.groupBox_3)
        self.mkb_e.setObjectName(u"mkb_e")

        self.gridLayout_3.addWidget(self.mkb_e, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 1, 0, 1, 3)

        self.groupBox_5 = QGroupBox(ServiceForm)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.category_s = QComboBox(self.groupBox_5)
        self.category_s.setObjectName(u"category_s")

        self.gridLayout_5.addWidget(self.category_s, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 3)


        self.retranslateUi(ServiceForm)

        QMetaObject.connectSlotsByName(ServiceForm)
    # setupUi

    def retranslateUi(self, ServiceForm):
        ServiceForm.setWindowTitle(QCoreApplication.translate("ServiceForm", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.cancel_b.setText(QCoreApplication.translate("ServiceForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.del_b.setText(QCoreApplication.translate("ServiceForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.save_b.setText(QCoreApplication.translate("ServiceForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ServiceForm", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ServiceForm", u"\u0426\u0435\u043d\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("ServiceForm", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ServiceForm", u"\u041a\u043e\u0434 \u041c\u041a\u0411", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ServiceForm", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438", None))
    # retranslateUi

