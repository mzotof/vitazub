from PySide2.QtCore import QTime
from PySide2.QtWidgets import QWidget

from db_intraction import *
from dialogs import *
from main import open_client_add
from widgets_descriptions.ClientFindForm import Ui_ClientFindForm
from widgets_descriptions.RecordingForm import Ui_RecordingForm


class UiClientFindFormExt(Ui_ClientFindForm):
    clients = None

    def __init__(self, client_find_form, rf):
        self.client_find_form = client_find_form
        self.setupUi(client_find_form)
        self.rf = rf
        self.sel_b.clicked.connect(self.client_find)
        self.view.doubleClicked.connect(self.close_client_find)
        self.ins_b.clicked.connect(open_client_add)

    def client_find(self):
        if len(self.ln_e.text()) > 2 or len(self.fn_e.text()) > 2:
            self.view.setModel(db_client_sel(self.ln_e.text().capitalize(), self.fn_e.text().capitalize(),
                                             self.mn_e.text().capitalize(), None, None)[1])
            self.clients = self.view.model().sourceModel().query()
            self.view.hideColumn(0)
        else:
            show_error('Для поиска необходимы фамилия или имя клиента, длиной не менее 3 символов.', 'Ок')

    def close_client_find(self):
        self.clients.seek(self.view.selectedIndexes()[0].row())
        self.rf.client_id = int(self.clients.value(0))
        self.rf.client_name.setText(self.clients.value(1) + ' ' + self.clients.value(2) + ' ' + self.clients.value(3))
        self.rf.phone.setText(self.clients.value(4))
        self.rf.phone2.setText(self.clients.value(5))
        self.rf.discount_e.setValue(int(self.clients.value(6)))
        self.rf.payment_source_s.clear()
        self.rf.payment_source_s.addItem('Выберите источник оплаты...')
        self.rf.payment_source_s.addItem('Наличные')
        self.rf.payment_source_s.addItem('Безналичный расчет')
        query = db_client_insur_sel(self.rf.client_id).sourceModel().query()
        query.first()
        self.rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
        while query.next():
            self.rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
        self.client_find_form.close()


class UiRecordingFormExt(Ui_RecordingForm):
    def __init__(self, recording_form, rec_id, client_id, selected_services):
        self.recording_form = recording_form
        self.setupUi(recording_form)
        self.rec_id = rec_id
        self.client_id = client_id
        self.selected_services = selected_services

        technical = db_technical_sel()
        start_tm = technical[1]
        self.start_time_e.setMinimumTime(QTime(int(start_tm[0:2]), int(start_tm[3:5])))
        self.end_time_e.setMinimumTime(QTime(int(start_tm[0:2]), int(start_tm[3:5])))
        end_tm = technical[2]
        self.start_time_e.setMaximumTime(QTime(int(end_tm[0:2]), int(end_tm[3:5])))
        self.end_time_e.setMaximumTime(QTime(int(end_tm[0:2]), int(end_tm[3:5])))

        self.client_find_b.clicked.connect(self.open_client_find)
        self.serv_sel_b.clicked.connect(self.rec_serv_sel)
        self.serv_v.doubleClicked.connect(self.rec_serv_sel)
        self.serv_unsel_b.clicked.connect(self.rec_serv_unsel)
        self.serv_sel_v.doubleClicked.connect(self.rec_serv_unsel)
        self.serv_e.textEdited.connect(self.serv_find)
        self.save_b.clicked.connect(self.rec_ins)
        self.del_b.clicked.connect(self.rec_del)
        self.pay_b.clicked.connect(self.pay)
        self.payment_source_s.currentIndexChanged.connect(self.client_balance_sel)
        self.cancel_b.clicked.connect(self.recording_form.close)

    def open_client_find(self):
        client_find_form = QWidget()
        cff = UiClientFindFormExt(client_find_form, self)
        cff.ln_e.clear()
        cff.fn_e.clear()
        cff.mn_e.clear()
        client_find_form.show()

    def rec_serv_sel(self):
        if len(self.serv_v.selectedIndexes()) > 0:
            rows = set()
            for i in self.serv_v.selectedIndexes():
                rows.add(i.row())
            for i in rows:
                services = self.serv_v.model().sourceModel().query()
                services.seek(i)
                if services.value(0) in self.selected_services.keys():
                    self.selected_services.update([(services.value(0), self.selected_services[services.value(0)] + 1)])
                else:
                    self.selected_services.update([(services.value(0), 1)])
                self.to_pay_e.setValue(self.to_pay_e.value() +
                                       round(float(services.value(4)) * (100 - self.discount_e.value()) / 100, 2))
                self.total_to_pay_e.setValue(self.total_to_pay_e.value() +
                                             round(float(services.value(4)) * (100 - self.discount_e.value()) / 100, 2))
            self.serv_sel_v.setModel(db_make_serv_list(self.selected_services))
            self.serv_sel_v.hideColumn(0)
        elif self.serv_v.model().rowCount() == 1:
            self.serv_v.selectColumn(1)
            self.rec_serv_sel()
        else:
            show_error('Выберите хотя-бы одну услугу из левого списка.', 'Ок')

    def rec_serv_unsel(self):
        if len(self.serv_sel_v.selectedIndexes()) > 0:
            rows = set()
            for i in self.serv_sel_v.selectedIndexes():
                rows.add(i.row())
            for i in rows:
                services = self.serv_sel_v.model().sourceModel().query()
                services.seek(i)
                self.selected_services.update([(services.value(0), self.selected_services[services.value(0)] - 1)])
                if self.selected_services[services.value(0)] == 0:
                    self.selected_services.pop(services.value(0))
                self.to_pay_e.setValue(self.to_pay_e.value() -
                                       round(float(services.value(4)) * (100 - self.discount_e.value()) / 100, 2))
                self.total_to_pay_e.setValue(self.total_to_pay_e.value() -
                                             round(float(services.value(4)) * (100 - self.discount_e.value()) / 100, 2))
            self.serv_sel_v.setModel(db_make_serv_list(self.selected_services))
            self.serv_sel_v.hideColumn(0)
        elif self.serv_sel_v.model().rowCount() == 1:
            self.serv_sel_v.selectColumn(1)
            self.rec_serv_unsel()
        else:
            show_error('Выберите хотя-бы одну услугу из правого списка.', 'Ок')

    def serv_find(self):
        self.serv_v.setModel(db_serv_sel(self.serv_e.text().capitalize()))

    def rec_ins(self):
        if self.client_id == -1:
            show_error('Выберите клиента.', 'Ок')
        elif self.end_time_e.time() <= self.start_time_e.time():
            show_error('Время начала сеанса должно быть меньше времени конца сеанса.', 'Ок')
        else:
            doctor_name = self.doctor.text().split(' ')
            doctors = db_doctor_sel(doctor_name[0], doctor_name[1], doctor_name[2]).sourceModel().query()
            doctors.first()
            start_dttm = self.date.date().toString('yyyy-MM-dd ') + self.start_time_e.time().toString('HH:mm:ss')
            end_dttm = self.date.date().toString('yyyy-MM-dd ') + self.end_time_e.time().toString('HH:mm:ss')
            if self.del_b.isVisible():
                if db_check_rec_dttm(doctors.value(0), start_dttm, end_dttm, self.rec_id):
                    db_rec_upd(self.discount_e.value(), self.selected_services, start_dttm, end_dttm,
                               self.comment_e.text(), self.rec_id)
                    if self.payed_e.value() > self.to_pay_e.value():
                        self.sum.setValue(self.to_pay_e.value() - self.payed_e.value())
                        self.payment_source_s.setCurrentIndex(3)
                        self.pay()
                    self.recording_form.close()
                    show_info(f'Запись успешно обновлена')
                else:
                    show_error('Выбранное время сеанса занято.', 'Ок')
            else:
                if db_check_rec_dttm(doctors.value(0), start_dttm, end_dttm):
                    db_rec_ins(doctors.value(0), self.client_id, self.discount_e.value(),
                               self.selected_services, start_dttm, end_dttm, self.comment_e.text())
                    self.recording_form.close()
                    show_info(f'Запись успешно добавлена')
                else:
                    show_error('Выбранное время сеанса занято.', 'Ок')

    def pay(self):
        if self.del_b.isVisible():
            client_balance = db_client_balance_sel(self.client_id)
            if self.sum.value() == 0:
                show_error('Введите сумму оплаты.', 'Ок')
            elif self.payment_source_s.currentIndex() == 0:
                show_error('Выберите источник оплаты.', 'Ок')
            elif self.sum.value() > self.total_to_pay_e.value() and self.payment_source_s.currentIndex() > 3:
                show_error('Страховая компания не может оплачивать сумму больше стоимости услуг.', 'Ок')
            elif self.sum.value() > client_balance and self.payment_source_s.currentIndex() == 3:
                show_error('На депозитном счете клиента не хватает средств.', 'Ок')
            else:
                type_of_pay = 'N'
                insurance_id = 'NULL'
                if self.payment_source_s.currentIndex() == 1 and self.sum.value() > self.total_to_pay_e.value():
                    answer = show_question('Сдача по операции составляет ' +
                                           str(self.sum.value() - self.total_to_pay_e.value()),
                                           'Выдать сдачу наличными',
                                           'Зачислить данную сумму на депозитный счет клиента')
                    if answer == 2:
                        db_change_client_balance(self.client_id, type_of_pay,
                                                 self.sum.value() - self.total_to_pay_e.value(),
                                                 f'Сдача от оплаты счета №{self.rec_id}')
                    self.sum.setValue(self.total_to_pay_e.value())
                if self.payment_source_s.currentIndex() == 2:
                    type_of_pay = 'C'
                    if self.sum.value() > self.total_to_pay_e.value():
                        answer = show_question('Сдача по операции составляет ' +
                                               str(self.sum.value() - self.total_to_pay_e.value()), 'Отмена',
                                               'Зачислить данную сумму на депозитный счет клиента')
                        if answer == 2:
                            db_change_client_balance(self.client_id, type_of_pay,
                                                     self.sum.value() - self.total_to_pay_e.value(),
                                                     f'Сдача от оплаты счета №{self.rec_id}')
                            self.sum.setValue(self.total_to_pay_e.value())
                        else:
                            return
                elif self.payment_source_s.currentIndex() == 3:
                    if self.sum.value() > self.total_to_pay_e.value():
                        self.sum.setValue(self.total_to_pay_e.value())
                    db_change_client_balance(self.client_id, 'O', -self.sum.value(), f'Оплата счета №{self.rec_id}')
                    type_of_pay = 'O'
                elif self.payment_source_s.currentIndex() > 3:
                    type_of_pay = 'I'
                    query = db_insur_sel(self.payment_source_s.currentText()
                                         [11:len(self.payment_source_s.currentText()) - 1])
                    query = query.sourceModel().query()
                    query.first()
                    insurance_id = query.value(0)
                db_pay_ins(self.rec_id, insurance_id, type_of_pay, self.sum.value(), self.pay_comment_e.text())
                self.payed_e.setValue(self.payed_e.value() + self.sum.value())
                self.total_to_pay_e.setValue(self.total_to_pay_e.value() - self.sum.value())
                self.payment_source_s.setCurrentIndex(0)
                self.sum.clear()
                self.pay_comment_e.clear()
                show_info(f'Транзакция успешно проведена')
        else:
            show_error('Сначала необходимо сохранить запись.', 'Ок')

    def client_balance_sel(self):
        if self.payment_source_s.currentIndex() == 3:
            show_info('Баланс депозитного счета клиента составляет ' +
                      str(db_client_balance_sel(self.client_id)) + ' руб')

    def rec_del(self):
        if show_confirmation('удалить выбранные записи') == 'yes':
            db_rec_del(self.rec_id)