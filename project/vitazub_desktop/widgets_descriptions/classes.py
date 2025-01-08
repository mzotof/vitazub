from PySide2.QtCore import QDate, Qt, QLocale
from PySide2.QtWidgets import QCalendarWidget, QTimeEdit, QDateTimeEdit, QComboBox
from PySide2.QtGui import QPen

from db_intraction import db_doctor_sel


class Scheduler(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.events = {
            QDate.currentDate(): ["today"]
        }
        self.setLocale(QLocale.Russian)

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        if date in self.events:
            pen = QPen(Qt.red)
            pen.setWidth(3)
            painter.setPen(pen)
            painter.drawRect(rect)


class MyTimeEdit(QTimeEdit):
    def stepBy(self, steps):
        if self.currentSection() == QDateTimeEdit.MinuteSection:
            steps *= 5
            if (steps > 0 and self.sectionText(QDateTimeEdit.MinuteSection) != "55") or steps < 0:
                super().stepBy(steps)
        else:
            super().stepBy(steps)


class DoctorSelector(QComboBox):
    def showPopup(self):
        self.clear()
        doctors = db_doctor_sel('', '', '').sourceModel().query()
        doctors.first()
        self.addItem('Выберите врача...')
        self.addItem(doctors.value(1) + ' ' + doctors.value(2) + ' ' + doctors.value(3))
        while doctors.next():
            self.addItem(doctors.value(1) + ' ' + doctors.value(2) + ' ' + doctors.value(3))
        super().showPopup()
