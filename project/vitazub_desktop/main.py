import os
import sys
from shutil import copy2

import pandas
from PySide2.QtCore import QDate, QTime, QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QSizePolicy
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter

from dialogs import show_error, show_confirmation, show_info, show_question

from widgets_descriptions.UserForm import Ui_UserForm
from widgets_descriptions.ClientFindForm import Ui_ClientFindForm
from widgets_descriptions.ClientInsuranceForm import Ui_ClientInsuranceForm
from widgets_descriptions.DoctorForm import Ui_DoctorForm
from widgets_descriptions.MaterialAmountForm import Ui_MaterialAmountForm
from widgets_descriptions.MaterialForm import Ui_MaterialForm
from widgets_descriptions.RecordingForm import Ui_RecordingForm
from widgets_descriptions.ReportsForm import Ui_ReportsForm
from widgets_descriptions.SalaryForm import Ui_SalaryReportForm
from widgets_descriptions.ServiceForm import Ui_ServiceForm
from widgets_descriptions.ShowUsersForm import Ui_ShowUsersForm
from widgets_descriptions.TaskForm import Ui_TaskForm
from widgets_descriptions.TechnicalForm import Ui_TechnicalForm
from widgets_descriptions.TransactionForm import Ui_TransactionForm
from widgets_descriptions.ClientForm import Ui_ClientForm
from widgets_descriptions.InsuranceForm import Ui_InsuranceForm
from widgets_descriptions.LoginForm import Ui_LoginForm
from widgets_descriptions.ConfigForm import Ui_configForm
from widgets_descriptions.MainWindow import Ui_MainWindow

from db_intraction import *

from config import db_name, save_config_file

os.environ['QT_MAC_WANTS_LAYER'] = '1'

app = QApplication(sys.argv)

is_admin = -1
user_name = ''


# ############################################################################################ #
# ---------------------------------------- ОКНО ВХОДА ---------------------------------------- #
# ############################################################################################ #
LoginForm = QWidget()
ui_login = Ui_LoginForm()
ui_login.setupUi(LoginForm)


def send_login():
    error = connect_db(ui_login.loginEdit.text().lower(), ui_login.passEdit.text())
    if error[0] in ['A', 'U']:
        global is_admin, user_name
        is_admin = error[0] == 'A'
        user_name = error[1]
        LoginForm.hide()
        mw.doctor_s.addItem('Выберите врача...')
        taf.doctor_s.addItem('Выберите врача...')
        mw.task_dt_e.setDate(QDate.currentDate().addDays(7))
        df.spec_s.setModel(db_spec_sel())
        sf.category_s.setModel(db_category_sel())
        technical = db_technical_sel()
        start_tm = technical[1]
        rf.start_time_e.setMinimumTime(QTime(int(start_tm[0:2]), int(start_tm[3:5])))
        rf.end_time_e.setMinimumTime(QTime(int(start_tm[0:2]), int(start_tm[3:5])))
        end_tm = technical[2]
        rf.start_time_e.setMaximumTime(QTime(int(end_tm[0:2]), int(end_tm[3:5])))
        rf.end_time_e.setMaximumTime(QTime(int(end_tm[0:2]), int(end_tm[3:5])))

        mw.loan_start_dt_e.setDate(QDate.currentDate().addYears(-1))
        mw.loan_end_dt_e.setDate(QDate.currentDate())

        cur_dt = QDate.currentDate()
        repf.rec_start_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), 1))
        repf.rec_end_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), cur_dt.daysInMonth()))
        repf.serv_start_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), 1))
        repf.serv_end_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), cur_dt.daysInMonth()))
        repf.fin_start_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), 1))
        repf.fin_end_dt.setDate(QDate(cur_dt.year(), cur_dt.month(), cur_dt.daysInMonth()))
        rep_rec_upd()
        rep_serv_upd()
        rep_fin_upd()

        main_window.showMaximized()
        mw.doctor_s.setFocus()
    elif error[0] is None:
        if show_error('Неверный логин или пароль',
                      'Попробовать снова', 'Закрыть приложение') == 'yes':
            ui_login.passEdit.clear()
        else:
            exit(0)
    else:
        if show_error('Ошибка подключения базы данных: ' + str(error[0]),
                      'Выбрать другую БД', 'Закрыть приложение') == 'yes':
            open_config()
        else:
            exit(0)


def open_config():
    LoginForm.hide()
    ConfigForm.show()
    ui_config.dbEdit.setText(db_name())


ui_login.enterButton.clicked.connect(send_login)
ui_login.configButton.clicked.connect(open_config)
ui_login.cancelButton.clicked.connect(LoginForm.close)

# ############################################################################################# #
# ------------------------------------- ОКНО КОНФИГУРАЦИИ ------------------------------------- #
# ############################################################################################# #
ConfigForm = QWidget()
ui_config = Ui_configForm()
ui_config.setupUi(ConfigForm)


def find_db():
    ui_config.dbEdit.setText(QFileDialog.getOpenFileName(ConfigForm, 'Выбрать местоположение базы данных',
                                                         ui_config.dbEdit.text(), 'Файлы БД SQLite (*.sqlite)')[0])


def save_config():
    save_config_file(ui_config.dbEdit.text())
    open_login()


def open_login():
    ConfigForm.hide()
    ui_login.loginEdit.clear()
    ui_login.passEdit.clear()
    LoginForm.show()


ui_config.dbButton.clicked.connect(find_db)
ui_config.saveButton.clicked.connect(save_config)
ui_config.cancelButton.clicked.connect(open_login)

# ############################################################################################ #
# --------------------------------------- ГЛАВНОЕ ОКНО --------------------------------------- #
# ############################################################################################ #
main_window = QMainWindow()
mw = Ui_MainWindow()
mw.setupUi(main_window)


def open_show_users():
    suf.view.setModel(db_user_sel())
    suf.view.resizeColumnsToContents()
    show_users_form.show()


def change_user():
    main_window.close()
    open_login()


def show_reminder():
    next_visit_dt = QDate.currentDate().toString('yyyy-MM-dd')
    clients = db_client_sel('', '', '', next_visit_dt, next_visit_dt)
    if clients[0] == 0:
        show_info('Сегодня не нужно уведомлять клиентов о следующем посещении')
    else:
        answer = show_question(f'Сегодня необходимо уведомить о следующем посещении {clients[0]} клиентов',
                               'Показать клиентов', 'Закрыть')
        if answer == 1:
            mw.clients_v.setModel(clients[1])
            mw.clients_v.hideColumn(0)
            mw.clients_v.resizeColumnsToContents()
            mw.client_ln_e.clear()
            mw.client_fn_e.clear()
            mw.client_mn_e.clear()
            mw.next_visit_dt_s.setCurrentIndex(1)
            mw.tabWidget.setCurrentIndex(1)
            if clients[0] > 50:
                show_info('Выбранные фильтры не позволяют отобразить всех искомых клиентов')


def change_db():
    main_window.close()
    ui_config.dbEdit.setText(db_name())
    ConfigForm.show()


def save_db():
    filename = QFileDialog.getSaveFileName(main_window, 'Сохранение базы данных на съемный носитель',
                                           db_name(), 'Файлы БД SQLite (*.sqlite)')
    copy2(db_name(), filename[0])
    show_info('База данных успешно сохранена на съемный носитель')


def open_technical_upd():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        technical = db_technical_sel()
        tf.name_e.setText(technical[0])
        tf.start_tm_e.setTime(QTime(int(technical[1][0:2]), int(technical[1][3:5])))
        tf.end_tm_e.setTime(QTime(int(technical[2][0:2]), int(technical[2][3:5])))
        technical_form.show()


def salary_report_set_period(rep_dt=None):
    if rep_dt is not None:
        srf.start_dt_e.setDate(QDate(rep_dt.year(), rep_dt.month(), 1))
        srf.end_dt_e.setDate(QDate(rep_dt.year(), rep_dt.month(), rep_dt.daysInMonth()))
    start_dt = srf.start_dt_e.date()
    end_dt = srf.end_dt_e.date()
    file_name = start_dt.toString('\\Отчет_ЗП_yyyy-MM-dd_-_') + end_dt.toString('yyyy-MM-dd.xlsx')
    directory = os.getcwd()
    if srf.directory_e.text() != '':
        directory = os.path.dirname(srf.directory_e.text())
    srf.directory_e.setText(directory + file_name)


def open_create_salary_report():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        salary_report_set_period(QDate.currentDate().addMonths(-1))
        salary_report_form.show()


def open_reports():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        reports_form.showMaximized()


def open_transaction_form():
    transaction_form.show()


mw.edit_users.triggered.connect(open_show_users)
mw.change_user.triggered.connect(change_user)
mw.show_reminder_m.triggered.connect(show_reminder)
mw.change_db.triggered.connect(change_db)
mw.save_db.triggered.connect(save_db)
mw.edit_technical.triggered.connect(open_technical_upd)
mw.salary_report.triggered.connect(open_create_salary_report)
mw.reports.triggered.connect(open_reports)
mw.make_trans.triggered.connect(open_transaction_form)


def show_schedule():
    if mw.doctor_s.currentIndex() == 0:
        mw.rec_v.setModel(db_schedule_sel(-1, '1900-01-01'))
        mw.rec_v.hideColumn(0)
        mw.rec_v.hideColumn(1)
        mw.rec_v.hideColumn(6)
        mw.rec_v.hideColumn(8)
    else:
        doctor_name = mw.doctor_s.currentText().split(' ')
        doctors = db_doctor_sel(doctor_name[0], doctor_name[1], doctor_name[2]).sourceModel().query()
        doctors.first()
        model = db_schedule_sel(doctors.value(0), mw.date_s.selectedDate().toString('yyyy-MM-dd'))
        mw.rec_v.setModel(model)
        mw.rec_v.hideColumn(0)
        mw.rec_v.hideColumn(1)
        mw.rec_v.hideColumn(6)
        mw.rec_v.hideColumn(8)
        mw.rec_v.resizeColumnsToContents()


def open_rec_ins(checked=None, start_tm=None):
    global selected_services, selected_client_id, selected_rec_id
    if mw.doctor_s.currentIndex() > 0:
        selected_client_id = -1
        selected_rec_id = -1
        selected_services = {}
        rf.doctor.setText(mw.doctor_s.currentText())
        rf.client_find_b.setEnabled(True)
        rf.client_name.clear()
        rf.phone.clear()
        rf.phone2.clear()
        rf.discount_e.clear()
        rf.serv_e.clear()
        rf.serv_v.setModel(db_serv_sel(''))
        rf.serv_v.hideColumn(0)
        rf.serv_sel_v.setModel(db_make_serv_list(selected_services))
        rf.serv_sel_v.hideColumn(0)
        rf.date.setDate(mw.date_s.selectedDate())
        if start_tm is None:
            start_tm = rf.start_time_e.minimumTime()
        rf.start_time_e.setTime(start_tm)
        rf.end_time_e.setTime(start_tm.addSecs(1800))
        rf.comment_e.clear()
        rf.payment_source_s.clear()
        rf.sum.clear()
        rf.to_pay_e.clear()
        rf.total_to_pay_e.clear()
        rf.payed_e.clear()
        rf.del_b.setVisible(False)
        rf.save_b.setEnabled(True)
        rf.del_b.setEnabled(True)
        rf.serv_v.resizeColumnsToContents()
        rf.serv_sel_v.resizeColumnsToContents()
        recording_form.showMaximized()
    else:
        show_error('Для добавления записи необходимо выбрать врача', 'Ок')


def open_rec_upd(rec_id, doctor_name, client_id, client_name, phone, phone2, discount,
                 rec_dt, start_tm, end_tm, comment):
    global selected_services, selected_client_id, selected_rec_id
    selected_client_id = client_id
    selected_rec_id = rec_id
    selected_services = db_find_serv_list(rec_id)
    rf.doctor.setText(doctor_name)
    rf.client_find_b.setEnabled(False)
    rf.client_name.setText(client_name)
    rf.phone.setText(phone)
    rf.phone2.setText(phone2)
    rf.discount_e.setValue(discount)
    rf.serv_e.clear()
    rf.serv_v.setModel(db_serv_sel(''))
    rf.serv_v.hideColumn(0)
    rf.serv_sel_v.setModel(db_make_serv_list(selected_services))
    rf.serv_sel_v.hideColumn(0)
    rf.date.setDate(rec_dt)
    rf.start_time_e.setTime(start_tm)
    rf.end_time_e.setTime(end_tm)
    rf.comment_e.setText(comment)
    rf.payment_source_s.clear()
    rf.payment_source_s.addItem('Выберите источник оплаты...')
    rf.payment_source_s.addItem('Наличные')
    rf.payment_source_s.addItem('Безналичный расчет')
    rf.payment_source_s.addItem('Депозитный счет клиента')
    query = db_client_insur_sel(selected_client_id).sourceModel().query()
    query.first()
    if query.value(1) is not None:
        rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
    while query.next():
        rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
    rf.sum.clear()
    amounts = db_amounts_sel(rec_id)
    rf.to_pay_e.setValue(amounts[0])
    rf.payed_e.setValue(amounts[1])
    rf.total_to_pay_e.setValue(amounts[0] - amounts[1])
    rf.del_b.setVisible(True)
    rf.serv_v.resizeColumnsToContents()
    rf.serv_sel_v.resizeColumnsToContents()
    recording_form.showMaximized()


def open_rec_upd_from_schedule():
    if mw.doctor_s.currentIndex() > 0:
        if len(mw.rec_v.selectedIndexes()) == 0:
            show_error('Выберите запись, которую хотите изменить', 'ОК')
        else:
            rec = mw.rec_v.model().sourceModel().query()
            rec.seek(mw.rec_v.selectedIndexes()[0].row())
            if rec.value(4) == 'Свободно':
                open_rec_ins(False, QTime(int(rec.value(2)[0:2]), int(rec.value(2)[3:5])))
            else:
                open_rec_upd(rec.value(0), mw.doctor_s.currentText(), rec.value(1), rec.value(4), rec.value(5),
                             rec.value(6), int(rec.value(8)), mw.date_s.selectedDate(),
                             QTime(int(rec.value(2)[0:2]), int(rec.value(2)[3:5])),
                             QTime(int(rec.value(3)[0:2]), int(rec.value(3)[3:5])), rec.value(9))
    else:
        show_error('Для редактирования записи необходимо выбрать врача', 'Ок')


def rec_del():
    if len(mw.rec_v.selectedIndexes()) > 0:
        if show_confirmation('удалить выбранные записи') == 'yes':
            for i in mw.rec_v.selectedIndexes():
                if i.model().data(i.model().index(i.row(), 4)) != 'Свободно':
                    db_rec_del(i.model().data(i.model().index(i.row(), 0)))
            show_schedule()
    else:
        show_error('Выберите хотя-бы одну запись', 'ОК')


mw.date_s.clicked.connect(show_schedule)
mw.doctor_s.activated.connect(show_schedule)
mw.rec_ins_b.clicked.connect(open_rec_ins)
mw.rec_upd_b.clicked.connect(open_rec_upd_from_schedule)
mw.rec_v.doubleClicked.connect(open_rec_upd_from_schedule)
mw.rec_del_b.clicked.connect(rec_del)


def loans_sel():
    mw.loan_v.setModel(db_loan_sel(mw.loan_ln_e.text().capitalize(), mw.loan_fn_e.text().capitalize(),
                                   mw.loan_mn_e.text().capitalize(), mw.loan_start_dt_e.date().toString('yyyy-MM-dd'),
                                   mw.loan_end_dt_e.date().toString('yyyy-MM-dd')))
    mw.loan_v.hideColumn(0)
    mw.loan_v.hideColumn(1)
    mw.loan_v.hideColumn(2)
    mw.loan_v.hideColumn(8)
    mw.loan_v.hideColumn(9)
    mw.loan_v.hideColumn(10)
    mw.loan_v.hideColumn(11)
    mw.loan_v.resizeColumnsToContents()


def open_rec_upd_from_loans():
    rec = mw.loan_v.model().sourceModel().query()
    rec.seek(mw.loan_v.selectedIndexes()[0].row())
    rec_dt = QDate(int(rec.value(3)[6:10]), int(rec.value(3)[3:5]), int(rec.value(3)[0:2]))
    open_rec_upd(rec.value(0), db_doctor_sel_by_id(rec.value(1)), rec.value(2), rec.value(4), rec.value(5),
                 rec.value(10), int(rec.value(11)), rec_dt, QTime(int(rec.value(8)[0:2]), int(rec.value(8)[3:5])),
                 QTime(int(rec.value(9)[0:2]), int(rec.value(9)[3:5])), rec.value(7))


mw.loan_search_b.clicked.connect(loans_sel)
mw.loan_v.doubleClicked.connect(open_rec_upd_from_loans)


def open_client_add():
    cf.ln_e.clear()
    cf.fn_e.clear()
    cf.mn_e.clear()
    cf.phone_e.clear()
    cf.phone2_e.clear()
    cf.discount_e.clear()
    cf.birth_dt_e.clear()
    cf.comment_e.clear()
    cf.balance_e.clear()
    cf.notified_s.setChecked(False)
    cf.insur_b.setVisible(False)
    cf.change_bal_b.setVisible(False)
    cf.del_b.setVisible(False)
    client_form.show()


def find_client():
    if len(mw.client_ln_e.text()) < 3 and len(mw.client_fn_e.text()) < 3 and mw.next_visit_dt_s.currentIndex() == 0:
        show_error('Для поиска клиента необходимы его фамилия, имя или дата следующего визита. '
                   'Введите что-то из этого.', 'Ок')
    else:
        min_next_visit_dt = None
        max_next_visit_dt = None
        if mw.next_visit_dt_s.currentIndex() != 0:
            min_next_visit_dt = QDate.currentDate().toString('yyyy-MM-dd')
            max_next_visit_dt = QDate.currentDate().toString('yyyy-MM-dd')
            if mw.next_visit_dt_s.currentIndex() == 2:
                min_next_visit_dt = QDate.currentDate().addDays(-7).toString('yyyy-MM-dd')
            elif mw.next_visit_dt_s.currentIndex() == 3:
                max_next_visit_dt = QDate.currentDate().addDays(-7).toString('yyyy-MM-dd')
        clients = db_client_sel(mw.client_ln_e.text().capitalize(), mw.client_fn_e.text().capitalize(),
                                mw.client_mn_e.text().capitalize(), min_next_visit_dt, max_next_visit_dt)
        mw.clients_v.setModel(clients[1])
        mw.clients_v.hideColumn(0)
        mw.clients_v.resizeColumnsToContents()
        if clients[0] > 50:
            show_info('Выбранные фильтры не позволяют отобразить всех искомых клиентов')


def open_edit_client():
    if len(mw.clients_v.selectedIndexes()) > 0:
        model = mw.clients_v.selectedIndexes()[0].model()
        row = mw.clients_v.selectedIndexes()[0].row()
        cf.ln_e.setText(model.data(model.index(row, 1)))
        cf.fn_e.setText(model.data(model.index(row, 2)))
        cf.mn_e.setText(model.data(model.index(row, 3)))
        cf.phone_e.setText(model.data(model.index(row, 4)))
        cf.phone2_e.setText(model.data(model.index(row, 5)))
        cf.discount_e.setValue(model.data(model.index(row, 6)))
        birth_dt = model.data(model.index(row, 7))
        cf.birth_dt_e.setDate(QDate(int(birth_dt[0:4]), int(birth_dt[5:7]), int(birth_dt[8:10])))
        cf.balance_e.setValue(model.data(model.index(row, 9)))
        cf.comment_e.setText(model.data(model.index(row, 10)))
        cf.notified_s.setChecked(model.data(model.index(row, 8)) == '')
        cf.insur_b.setVisible(True)
        cf.change_bal_b.setVisible(True)
        cf.del_b.setVisible(True)
        client_form.show()
    else:
        show_error('Выберите хотя-бы одного клиента', 'ОК')


def client_delete():
    if len(mw.clients_v.selectedIndexes()) > 0:
        if show_confirmation('удалить выбранных клиентов') == 'yes':
            db_client_del(mw.clients_v.selectedIndexes())
            client_form.close()
            find_client()
    else:
        show_error('Выберите хотя-бы одного клиента', 'ОК')


mw.client_search_b.clicked.connect(find_client)
mw.client_edit_b.clicked.connect(open_edit_client)
mw.clients_v.doubleClicked.connect(open_edit_client)
mw.client_del_b.clicked.connect(client_delete)
mw.client_add_b.clicked.connect(open_client_add)


def open_insur_ins():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if_.name_e.clear()
        if_.comment_e.clear()
        if_.del_b.setVisible(False)
        insurance_form.show()


def insur_sel():
    mw.insur_v.setModel(db_insur_sel(mw.insur_name_e.text().capitalize()))
    mw.insur_v.hideColumn(0)
    mw.insur_v.resizeColumnsToContents()


def insur_sel_all():
    mw.insur_v.setModel(db_insur_sel(''))
    mw.insur_v.hideColumn(0)
    mw.insur_v.resizeColumnsToContents()


def open_insur_upd():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.insur_v.selectedIndexes()) > 0:
            model = mw.insur_v.selectedIndexes()[0].model()
            row = mw.insur_v.selectedIndexes()[0].row()
            if_.name_e.setText(model.data(model.index(row, 1)))
            if_.comment_e.setText(model.data(model.index(row, 2)))
            if_.del_b.setVisible(True)
            insurance_form.show()
        else:
            show_error('Выберите хотя-бы одну страховую компанию', 'ОК')


def insur_del():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.insur_v.selectedIndexes()) > 0:
            if show_confirmation('удалить выбранные страховые компании') == 'yes':
                db_insur_del(mw.insur_v.selectedIndexes())
                insurance_form.close()
                insur_sel()
        else:
            show_error('Выберите хотя-бы одну страховую компанию', 'ОК')


mw.insur_ins_b.clicked.connect(open_insur_ins)
mw.insur_sel_b.clicked.connect(insur_sel)
mw.insur_sel_all_b.clicked.connect(insur_sel_all)
mw.insur_upd_b.clicked.connect(open_insur_upd)
mw.insur_v.doubleClicked.connect(open_insur_upd)
mw.insur_del_b.clicked.connect(insur_del)


def open_doctor_ins():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        df.ln_e.clear()
        df.fn_e.clear()
        df.mn_e.clear()
        df.rate_e.clear()
        df.phone_e.clear()
        df.phone2_e.clear()
        df.comment_e.clear()
        df.del_b.setVisible(False)
        doctor_form.show()


def doctor_sel():
    mw.doctor_v.setModel(db_doctor_sel(mw.doctor_ln_e.text().capitalize(), mw.doctor_fn_e.text().capitalize(),
                                       mw.doctor_mn_e.text().capitalize()))
    mw.doctor_v.hideColumn(0)
    mw.doctor_v.hideColumn(6)
    mw.doctor_v.resizeColumnsToContents()


def doctor_sel_all():
    mw.doctor_v.setModel(db_doctor_sel('', '', ''))
    mw.doctor_v.hideColumn(0)
    mw.doctor_v.hideColumn(6)
    mw.doctor_v.resizeColumnsToContents()


def open_doctor_upd():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.doctor_v.selectedIndexes()) > 0:
            model = mw.doctor_v.selectedIndexes()[0].model()
            row = mw.doctor_v.selectedIndexes()[0].row()
            df.ln_e.setText(model.data(model.index(row, 1)))
            df.fn_e.setText(model.data(model.index(row, 2)))
            df.mn_e.setText(model.data(model.index(row, 3)))
            df.phone_e.setText(model.data(model.index(row, 4)))
            df.phone2_e.setText(model.data(model.index(row, 5)))
            df.rate_e.setValue(int(model.data(model.index(row, 6))))
            df.spec_s.setCurrentText(model.data(model.index(row, 7)))
            df.comment_e.setText(model.data(model.index(row, 8)))
            df.del_b.setVisible(True)
            doctor_form.show()
        else:
            show_error('Выберите хотя-бы одного врача', 'ОК')


def doctor_del():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.doctor_v.selectedIndexes()) > 0:
            if show_confirmation('удалить выбранных врачей') == 'yes':
                db_doctor_del(mw.doctor_v.selectedIndexes())
                doctor_form.close()
                doctor_sel()
        else:
            show_error('Выберите хотя-бы одного врача', 'ОК')


mw.doctor_ins_b.clicked.connect(open_doctor_ins)
mw.doctor_sel_b.clicked.connect(doctor_sel)
mw.doctor_sel_all_b.clicked.connect(doctor_sel_all)
mw.doctor_upd_b.clicked.connect(open_doctor_upd)
mw.doctor_v.doubleClicked.connect(open_doctor_upd)
mw.doctor_del_b.clicked.connect(doctor_del)


def open_serv_ins():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        sf.mkb_e.clear()
        sf.name_e.clear()
        sf.price_e.clear()
        sf.comment_e.clear()
        sf.del_b.setVisible(False)
        serv_form.show()


def serv_sel():
    mw.serv_v.setModel(db_serv_sel(mw.serv_filter_e.text().capitalize()))
    mw.serv_v.hideColumn(0)
    mw.serv_v.resizeColumnsToContents()


def serv_sel_all():
    mw.serv_v.setModel(db_serv_sel(''))
    mw.serv_v.hideColumn(0)
    mw.serv_v.resizeColumnsToContents()


def open_serv_upd():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.serv_v.selectedIndexes()) > 0:
            model = mw.serv_v.selectedIndexes()[0].model()
            row = mw.serv_v.selectedIndexes()[0].row()
            sf.mkb_e.setText(model.data(model.index(row, 1)))
            sf.name_e.setText(model.data(model.index(row, 2)))
            sf.category_s.setCurrentText(model.data(model.index(row, 3)))
            sf.price_e.setValue(float(model.data(model.index(row, 4))))
            sf.comment_e.setText(model.data(model.index(row, 5)))
            sf.del_b.setVisible(True)
            serv_form.show()
        else:
            show_error('Выберите хотя-бы одну услугу', 'ОК')


def serv_del():
    if not is_admin:
        show_error('Данное действие доступно только администраторам системы', 'Ок')
    else:
        if len(mw.serv_v.selectedIndexes()) > 0:
            if show_confirmation('удалить выбранные услуги') == 'yes':
                db_serv_del(mw.serv_v.selectedIndexes())
                serv_form.close()
                serv_sel()
        else:
            show_error('Выберите хотя-бы одну услугу', 'ОК')


mw.serv_ins_b.clicked.connect(open_serv_ins)
mw.serv_sel_b.clicked.connect(serv_sel)
mw.serv_sel_all_b.clicked.connect(serv_sel_all)
mw.serv_upd_b.clicked.connect(open_serv_upd)
mw.serv_v.doubleClicked.connect(open_serv_upd)
mw.serv_del_b.clicked.connect(serv_del)


def open_mater_ins():
    mf.name_e.clear()
    mf.comment_e.clear()
    mf.del_b.setVisible(False)
    material_form.show()


def mater_sel():
    mw.mater_v.setModel(db_mater_sel(mw.mater_name_e.text().capitalize()))
    mw.mater_v.hideColumn(0)
    mw.mater_v.resizeColumnsToContents()


def mater_sel_all():
    mw.mater_v.setModel(db_mater_sel(''))
    mw.mater_v.hideColumn(0)
    mw.mater_v.resizeColumnsToContents()


def open_mater_upd():
    if len(mw.mater_v.selectedIndexes()) > 0:
        model = mw.mater_v.selectedIndexes()[0].model()
        row = mw.mater_v.selectedIndexes()[0].row()
        mf.name_e.setText(model.data(model.index(row, 1)))
        mf.comment_e.setText(model.data(model.index(row, 3)))
        mf.del_b.setVisible(True)
        material_form.show()
    else:
        show_error('Выберите хотя-бы один материал', 'ОК')


def mater_del():
    if len(mw.mater_v.selectedIndexes()) > 0:
        if show_confirmation('удалить выбранные материалы') == 'yes':
            db_mater_del(mw.mater_v.selectedIndexes())
            material_form.close()
            mater_sel()
    else:
        show_error('Выберите хотя-бы один материал', 'ОК')


def open_mater_add():
    if len(mw.mater_v.selectedIndexes()) == 1:
        maf.amount_e.setValue(1)
        maf.add_b.setText('Добавить')
        material_amount_form.show()
    else:
        show_error('Выберите материал, количество которого хотите увеличить', 'ОК')


def open_mater_sub():
    if len(mw.mater_v.selectedIndexes()) == 1:
        maf.amount_e.setValue(1)
        maf.add_b.setText('Уменьшить')
        material_amount_form.show()
    else:
        show_error('Выберите материал, количество которого хотите уменьшить', 'ОК')


mw.mater_ins_b.clicked.connect(open_mater_ins)
mw.mater_sel_b.clicked.connect(mater_sel)
mw.mater_sel_all_b.clicked.connect(mater_sel_all)
mw.mater_upd_b.clicked.connect(open_mater_upd)
mw.mater_v.doubleClicked.connect(open_mater_upd)
mw.mater_del_b.clicked.connect(mater_del)
mw.mater_add_b.clicked.connect(open_mater_add)
mw.mater_sub_b.clicked.connect(open_mater_sub)


def open_task_ins():
    taf.name_e.clear()
    taf.dt_e.setDate(QDate.currentDate().addDays(7))
    taf.status_s.setCurrentIndex(0)
    taf.doctor_s.setCurrentIndex(0)
    taf.comment_e.clear()
    taf.del_b.setVisible(False)
    task_form.show()


def task_sel():
    mw.task_v.setModel(db_task_sel(mw.task_name_e.text().capitalize(), mw.task_dt_e.date().toString('yyyy-MM-dd'),
                                    mw.task_status_s.currentText()))
    mw.task_v.hideColumn(0)
    mw.task_v.hideColumn(4)
    mw.task_v.resizeColumnsToContents()


def open_task_upd():
    if len(mw.task_v.selectedIndexes()) > 0:
        model = mw.task_v.selectedIndexes()[0].model()
        row = mw.task_v.selectedIndexes()[0].row()
        taf.name_e.setText(model.data(model.index(row, 1)))
        dt = model.data(model.index(row, 2)).split('-')
        taf.dt_e.setDate(QDate(int(dt[0]), int(dt[1]), int(dt[2])))
        taf.status_s.setCurrentIndex(int(model.data(model.index(row, 4))))
        taf.doctor_s.setCurrentText(model.data(model.index(row, 5)))
        taf.comment_e.setText(model.data(model.index(row, 6)))
        taf.del_b.setVisible(True)
        task_form.show()
    else:
        show_error('Выберите хотя-бы одну задачу', 'ОК')


def task_del():
    if len(mw.task_v.selectedIndexes()) > 0:
        if show_confirmation('удалить выбранные задачи') == 'yes':
            db_task_del(mw.task_v.selectedIndexes())
            task_form.close()
            task_sel()
    else:
        show_error('Выберите хотя-бы одну задачу', 'ОК')


mw.task_ins_b.clicked.connect(open_task_ins)
mw.task_sel_b.clicked.connect(task_sel)
mw.task_upd_b.clicked.connect(open_task_upd)
mw.task_v.doubleClicked.connect(open_task_upd)
mw.task_del_b.clicked.connect(task_del)

# ########################################################################################### #
# -------------------------------------- ФОРМА КЛИЕНТА -------------------------------------- #
# ########################################################################################### #
client_form = QWidget()
cf = Ui_ClientForm()
cf.setupUi(client_form)


def clean_phone(not_cleaned_phone):
    phone = ''
    for i in not_cleaned_phone:
        if i.isdigit():
            phone += i
    if len(phone) > 0:
        if phone[0] in ('7', '8') and len(phone) == 11:
            phone = phone[1:]
        if phone[0] in ('9', '4') and len(phone) == 10:
            return '+7-' + phone[0:3] + '-' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10]
    return not_cleaned_phone


def clean_client_phone():
    cf.phone_e.setText(clean_phone(cf.phone_e.text()))


def clean_client_additional_phone():
    cf.phone2_e.setText(clean_phone(cf.phone2_e.text()))


def client_save():
    if cf.ln_e.text() == '' or cf.fn_e.text() == '':
        show_error('Введите ФИО клиента', 'Ок')
    else:
        fio = cf.ln_e.text().capitalize() + ' ' + cf.fn_e.text().capitalize() \
              + ' ' + cf.mn_e.text().capitalize()
        if cf.del_b.isVisible():
            model = mw.clients_v.selectedIndexes()[0].model()
            row = mw.clients_v.selectedIndexes()[0].row()
            db_client_upd(cf.ln_e.text().capitalize(), cf.fn_e.text().capitalize(),
                          cf.mn_e.text().capitalize(), cf.phone_e.text(), cf.phone2_e.text(),
                          cf.birth_dt_e.text(), cf.discount_e.text(), cf.comment_e.text(),
                          cf.notified_s.isChecked(), model.data(model.index(row, 0)))
            show_info(f'Клиент "{fio}" успешно изменен')
            find_client()
        else:
            db_client_ins(cf.ln_e.text().capitalize(), cf.fn_e.text().capitalize(),
                              cf.mn_e.text().capitalize(), cf.phone_e.text(), cf.phone2_e.text(),
                              cf.birth_dt_e.text(), cf.discount_e.text(), cf.comment_e.text())
            show_info(f'Клиент "{fio}" успешно добавлен')
        client_form.close()


def open_client_insur_ins():
    model = mw.clients_v.selectedIndexes()[0].model()
    row = mw.clients_v.selectedIndexes()[0].row()
    client_insur_sel(model.data(model.index(row, 0)))
    insurances = db_insur_sel('').sourceModel().query()
    insurances.first()
    cif.insur_s.clear()
    cif.insur_s.addItem('Выберите страховую компанию...')
    cif.insur_s.addItem(insurances.value(1))
    while insurances.next():
        cif.insur_s.addItem(insurances.value(1))
    cif.start_dt_e.setDate(QDate.currentDate())
    cif.end_dt_e.setDate(QDate.currentDate().addMonths(6))
    cif.comment_e.clear()
    cif.save_b.setText('Создать')
    client_insurance_form.show()


def open_change_client_balance():
    ccbf.trans_source_s.setCurrentIndex(0)
    ccbf.amount_e.clear()
    ccbf.comment_e.clear()
    change_client_balance_form.show()


cf.phone_e.editingFinished.connect(clean_client_phone)
cf.phone2_e.editingFinished.connect(clean_client_additional_phone)
cf.save_b.clicked.connect(client_save)
cf.del_b.clicked.connect(client_delete)
cf.insur_b.clicked.connect(open_client_insur_ins)
cf.change_bal_b.clicked.connect(open_change_client_balance)
cf.cancel_b.clicked.connect(client_form.close)

# ########################################################################################### #
# ----------------------------- ФОРМА ИЗМЕНЕНИЯ БАЛАНСА КЛИЕНТА ----------------------------- #
# ########################################################################################### #
change_client_balance_form = QWidget()
ccbf = Ui_TransactionForm()
ccbf.setupUi(change_client_balance_form)


def change_client_balance():
    if ccbf.trans_source_s.currentIndex() == 0:
        show_error('Выберите источник оплаты', 'Ок')
    elif ccbf.amount_e.value() == 0:
        show_error('Введите сумму транзакции', 'Ок')
    elif cf.balance_e.value() + ccbf.amount_e.value() < 0:
        show_error('Баланс клиента не может быть отрицательным', 'Ок')
    else:
        model = mw.clients_v.selectedIndexes()[0].model()
        row = mw.clients_v.selectedIndexes()[0].row()
        type_of_trans = 'N'
        if ccbf.trans_source_s.currentText() == 'Безналичный расчет':
            type_of_trans = 'C'
        db_change_client_balance(model.data(model.index(row, 0)), type_of_trans, ccbf.amount_e.value(),
                                 ccbf.comment_e.text())
        cf.balance_e.setValue(cf.balance_e.value() + ccbf.amount_e.value())
        change_client_balance_form.close()
        find_client()
        show_info('Транзакция успешно проведена')


ccbf.make_b.clicked.connect(change_client_balance)
ccbf.cancel_b.clicked.connect(change_client_balance_form.close)

# ########################################################################################### #
# ----------------------------- ФОРМА СВЯЗИ КЛИЕНТА И СТРАХОВКИ ----------------------------- #
# ########################################################################################### #
client_insurance_form = QWidget()
cif = Ui_ClientInsuranceForm()
cif.setupUi(client_insurance_form)


def client_insur_sel(c_id):
    cif.view.setModel(db_client_insur_sel(c_id))
    cif.view.hideColumn(0)
    cif.view.resizeColumnsToContents()


def client_insur_ins():
    if cif.insur_s.currentIndex() != 0:
        if cif.save_b.text() == 'Создать':
            model = mw.clients_v.selectedIndexes()[0].model()
            row = mw.clients_v.selectedIndexes()[0].row()
            db_client_insur_ins(model.data(model.index(row, 0)), cif.insur_s.currentText(),
                                cif.start_dt_e.text(), cif.end_dt_e.text(), cif.comment_e.text())
            client_insur_sel(model.data(model.index(row, 0)))
            cif.insur_s.setCurrentIndex(0)
            cif.start_dt_e.setDate(QDate.currentDate())
            cif.end_dt_e.setDate(QDate.currentDate().addMonths(6))
            cif.comment_e.clear()
            show_info(f'Страхование успешно добавлено')
        else:
            model = cif.view.selectedIndexes()[0].model()
            row = cif.view.selectedIndexes()[0].row()
            db_client_insur_upd(cif.insur_s.currentText(), cif.start_dt_e.text(), cif.end_dt_e.text(),
                                cif.comment_e.text(), model.data(model.index(row, 0)))
            client_insur_sel(model.data(model.index(row, 0)))
            model = mw.clients_v.selectedIndexes()[0].model()
            row = mw.clients_v.selectedIndexes()[0].row()
            client_insur_sel(model.data(model.index(row, 0)))
            cif.insur_s.setCurrentIndex(0)
            cif.start_dt_e.setDate(QDate.currentDate())
            cif.end_dt_e.setDate(QDate.currentDate().addMonths(6))
            cif.comment_e.clear()
            cif.save_b.setText('Создать')
            show_info(f'Страхование успешно изменено')
    else:
        show_error('Выберите страховую компанию', 'Ок')


def client_insur_upd():
    if len(cif.view.selectedIndexes()) > 0:
        model = cif.view.selectedIndexes()[0].model()
        row = cif.view.selectedIndexes()[0].row()
        cif.insur_s.setCurrentText(model.data(model.index(row, 1)))
        start_dt = model.data(model.index(row, 2))
        cif.start_dt_e.setDate(QDate(int(start_dt[0:4]), int(start_dt[5:7]), int(start_dt[8:10])))
        end_dt = model.data(model.index(row, 3))
        cif.start_dt_e.setDate(QDate(int(end_dt[0:4]), int(end_dt[5:7]), int(end_dt[8:10])))
        cif.comment_e.setText(model.data(model.index(row, 4)))
        cif.save_b.setText('Сохранить')
    else:
        show_error('Выберите хотя-бы одну страховку', 'Ок')


def client_insur_del():
    if len(cif.view.selectedIndexes()) > 0:
        if show_confirmation('удалить выбранные страховки') == 'yes':
            db_client_insur_del(cif.view.selectedIndexes())
            model = mw.clients_v.selectedIndexes()[0].model()
            row = mw.clients_v.selectedIndexes()[0].row()
            client_insur_sel(model.data(model.index(row, 0)))
    else:
        show_error('Выберите хотя-бы одну страховку', 'ОК')


cif.save_b.clicked.connect(client_insur_ins)
cif.upd_b.clicked.connect(client_insur_upd)
cif.view.doubleClicked.connect(client_insur_upd)
cif.del_b.clicked.connect(client_insur_del)

# ########################################################################################### #
# ------------------------------------- ФОРМА СТРАХОВОЙ ------------------------------------- #
# ########################################################################################### #
insurance_form = QWidget()
if_ = Ui_InsuranceForm()
if_.setupUi(insurance_form)


def insur_save():
    if if_.name_e.text() == '':
        show_error('Введите название страховой компании', 'Ок')
    else:
        if if_.del_b.isVisible():
            sel = mw.insur_v.selectedIndexes()[0]
            db_insur_upd(if_.name_e.text().capitalize(), if_.comment_e.text(),
                         sel.model().data(sel.model().index(sel.row(), 0)))
            show_info(f'Страховая компания "{if_.name_e.text().capitalize()}" успешно изменена')
            insur_sel()
        else:
            db_insur_ins(if_.name_e.text().capitalize(), if_.comment_e.text())
            show_info(f'Страховая компания "{if_.name_e.text().capitalize()}" успешно добавлена')
        insurance_form.close()


if_.save_b.clicked.connect(insur_save)
if_.del_b.clicked.connect(insur_del)
if_.cancel_b.clicked.connect(insurance_form.close)

# ########################################################################################### #
# -------------------------------------- ФОРМА ДОКТОРА -------------------------------------- #
# ########################################################################################### #
doctor_form = QWidget()
df = Ui_DoctorForm()
df.setupUi(doctor_form)


def doctor_save():
    if df.ln_e.text() == '' or df.fn_e.text() == '':
        show_error('Введите ФИО врача', 'Ок')
    elif df.phone_e.text() == '':
        show_error('Введите телефон врача', 'Ок')
    else:
        fio = df.ln_e.text().capitalize() + ' ' + df.fn_e.text().capitalize() + ' ' + df.mn_e.text().capitalize()
        if df.del_b.isVisible():
            sel = mw.doctor_v.selectedIndexes()[0]
            db_doctor_upd(df.ln_e.text().capitalize(), df.fn_e.text().capitalize(), df.mn_e.text().capitalize(),
                          df.phone_e.text(), df.phone2_e.text(), df.rate_e.value(), df.spec_s.currentText(),
                          df.comment_e.text(), sel.model().data(sel.model().index(sel.row(), 0)))
            show_info(f'Врач "{fio}" успешно изменен')
            doctor_sel()
        else:
            db_doctor_ins(df.ln_e.text().capitalize(), df.fn_e.text().capitalize(), df.mn_e.text().capitalize(),
                          df.phone_e.text(), df.phone2_e.text(), df.rate_e.value(), df.spec_s.currentText(),
                          df.comment_e.text())
            show_info(f'Врач "{fio}" успешно добавлен')
        doctor_form.close()


def clean_doctor_phone():
    df.phone_e.setText(clean_phone(df.phone_e.text()))


def clean_doctor_additional_phone():
    df.phone2_e.setText(clean_phone(df.phone2_e.text()))


df.phone_e.editingFinished.connect(clean_doctor_phone)
df.phone2_e.editingFinished.connect(clean_doctor_additional_phone)
df.save_b.clicked.connect(doctor_save)
df.del_b.clicked.connect(doctor_del)
df.cancel_b.clicked.connect(doctor_form.close)

# ########################################################################################### #
# -------------------------------------- ФОРМА УСЛУГИ --------------------------------------- #
# ########################################################################################### #
serv_form = QWidget()
sf = Ui_ServiceForm()
sf.setupUi(serv_form)


def serv_save():
    if sf.mkb_e.text() == '':
        show_error('Введите код МКБ', 'Ок')
    elif sf.name_e.text() == '':
        show_error('Введите название услуги', 'Ок')
    elif sf.category_s.currentIndex() == 0:
        show_error('Выберите категорию услуги', 'Ок')
    else:
        if sf.del_b.isVisible():
            sel = mw.serv_v.selectedIndexes()[0]
            db_serv_upd(sf.category_s.currentText(), sf.mkb_e.text().upper(), sf.name_e.text().capitalize(),
                        sf.price_e.value(), sf.comment_e.text(), sel.model().data(sel.model().index(sel.row(), 0)))
            show_info(f'Услуга "{sf.name_e.text().capitalize()}" успешно изменена')
            serv_sel()
        else:
            db_serv_ins(sf.category_s.currentText(), sf.mkb_e.text().upper(), sf.name_e.text().capitalize(),
                        sf.price_e.value(), sf.comment_e.text())
            show_info(f'Услуга "{sf.name_e.text().capitalize()}" успешно добавлена')
        serv_form.close()


sf.save_b.clicked.connect(serv_save)
sf.del_b.clicked.connect(serv_del)
sf.cancel_b.clicked.connect(serv_form.close)

# ############################################################################################ #
# --------------------------------------- ФОРМА ЗАПИСИ --------------------------------------- #
# ############################################################################################ #


class RecordingFormWidget(QWidget):
    def closeEvent(self, event):
        show_schedule()
        loans_sel()


recording_form = RecordingFormWidget()
rf = Ui_RecordingForm()
rf.setupUi(recording_form)
selected_client_id = -1
selected_rec_id = -1
selected_services = {}


def open_client_find():
    global selected_client_id
    selected_client_id = -1
    cff.ln_e.clear()
    cff.fn_e.clear()
    cff.mn_e.clear()
    cff.view.setModel(QSqlQueryModel())
    client_find_form.show()


def rec_serv_sel():
    global selected_services
    if len(rf.serv_v.selectedIndexes()) > 0:
        rows = set()
        for i in rf.serv_v.selectedIndexes():
            rows.add(i.row())
        for i in rows:
            services = rf.serv_v.model().sourceModel().query()
            services.seek(i)
            if services.value(0) in selected_services.keys():
                selected_services.update([(services.value(0), selected_services[services.value(0)] + 1)])
            else:
                selected_services.update([(services.value(0), 1)])
            rf.to_pay_e.setValue(rf.to_pay_e.value() +
                                 round(float(services.value(4)) * (100 - rf.discount_e.value()) / 100, 2))
            rf.total_to_pay_e.setValue(rf.total_to_pay_e.value() +
                                       round(float(services.value(4)) * (100 - rf.discount_e.value()) / 100, 2))
        rf.serv_sel_v.setModel(db_make_serv_list(selected_services))
        rf.serv_sel_v.hideColumn(0)
        rf.serv_v.resizeColumnsToContents()
        rf.serv_sel_v.resizeColumnsToContents()
    elif rf.serv_v.model().rowCount() == 1:
        rf.serv_v.selectColumn(1)
        rec_serv_sel()
    else:
        show_error('Выберите хотя-бы одну услугу из левого списка.', 'Ок')


def rec_serv_unsel():
    global selected_services
    if len(rf.serv_sel_v.selectedIndexes()) > 0:
        rows = set()
        for i in rf.serv_sel_v.selectedIndexes():
            rows.add(i.row())
        for i in rows:
            services = rf.serv_sel_v.model().sourceModel().query()
            services.seek(i)
            selected_services.update([(services.value(0), selected_services[services.value(0)] - 1)])
            if selected_services[services.value(0)] == 0:
                selected_services.pop(services.value(0))
            rf.to_pay_e.setValue(rf.to_pay_e.value() -
                                 round(float(services.value(4)) * (100 - rf.discount_e.value()) / 100, 2))
            rf.total_to_pay_e.setValue(rf.total_to_pay_e.value() -
                                       round(float(services.value(4)) * (100 - rf.discount_e.value()) / 100, 2))
        rf.serv_sel_v.setModel(db_make_serv_list(selected_services))
        rf.serv_sel_v.hideColumn(0)
        rf.serv_v.resizeColumnsToContents()
        rf.serv_sel_v.resizeColumnsToContents()
    elif rf.serv_sel_v.model().rowCount() == 1:
        rf.serv_sel_v.selectColumn(1)
        rec_serv_unsel()
    else:
        show_error('Выберите хотя-бы одну услугу из правого списка.', 'Ок')


def serv_find():
    rf.serv_v.setModel(db_serv_sel(rf.serv_e.text().capitalize()))
    rf.serv_v.resizeColumnsToContents()
    rf.serv_sel_v.resizeColumnsToContents()


def rec_ins():
    if selected_client_id == -1:
        show_error('Выберите клиента.', 'Ок')
    elif rf.end_time_e.time() <= rf.start_time_e.time():
        show_error('Время начала сеанса должно быть меньше времени конца сеанса.', 'Ок')
    else:
        doctor_name = rf.doctor.text().split(' ')
        doctors = db_doctor_sel(doctor_name[0], doctor_name[1], doctor_name[2]).sourceModel().query()
        doctors.first()
        start_dttm = rf.date.date().toString('yyyy-MM-dd ') + rf.start_time_e.time().toString('HH:mm:ss')
        end_dttm = rf.date.date().toString('yyyy-MM-dd ') + rf.end_time_e.time().toString('HH:mm:ss')
        if rf.del_b.isVisible():
            if db_check_rec_dttm(doctors.value(0), start_dttm, end_dttm, selected_rec_id):
                db_rec_upd(rf.discount_e.value(), selected_services, start_dttm, end_dttm,
                           rf.comment_e.text(), selected_rec_id)
                if rf.payed_e.value() > rf.to_pay_e.value():
                    rf.sum.setValue(rf.to_pay_e.value() - rf.payed_e.value())
                    rf.payment_source_s.setCurrentIndex(3)
                    pay()
                recording_form.close()
                show_schedule()
                show_info(f'Запись успешно обновлена')
            else:
                show_error('Выбранное время сеанса занято.', 'Ок')
        else:
            if db_check_rec_dttm(doctors.value(0), start_dttm, end_dttm):
                db_rec_ins(doctors.value(0), selected_client_id, rf.discount_e.value(), selected_services,
                           start_dttm, end_dttm, rf.comment_e.text())
                recording_form.close()
                show_schedule()
                show_info(f'Запись успешно добавлена')
            else:
                show_error('Выбранное время сеанса занято.', 'Ок')


def rec_form_del():
    if show_confirmation('удалить данную запись') == 'yes':
        db_rec_del(selected_rec_id)


def pay(pay_all_flag: bool = False):
    if rf.del_b.isVisible():
        if pay_all_flag:
            rf.sum.setValue(rf.total_to_pay_e.value())
        client_balance = db_client_balance_sel(selected_client_id)
        if rf.sum.value() == 0:
            show_error('Введите сумму оплаты.', 'Ок')
        elif rf.payment_source_s.currentIndex() == 0:
            show_error('Выберите источник оплаты.', 'Ок')
        elif rf.sum.value() > rf.total_to_pay_e.value() and rf.payment_source_s.currentIndex() > 3:
            show_error('Страховая компания не может оплачивать сумму больше стоимости услуг.', 'Ок')
        elif rf.sum.value() > client_balance and rf.payment_source_s.currentIndex() == 3:
            show_error('На депозитном счете клиента не хватает средств.', 'Ок')
        else:
            type_of_pay = 'N'
            insurance_id = 'NULL'
            if rf.payment_source_s.currentIndex() == 1 and rf.sum.value() > rf.total_to_pay_e.value():
                answer = show_question('Сдача по операции составляет ' +
                                       str(rf.sum.value() - rf.total_to_pay_e.value()), 'Выдать сдачу наличными',
                                       'Зачислить данную сумму на депозитный счет клиента')
                if answer == 2:
                    db_change_client_balance(selected_client_id, type_of_pay,
                                             rf.sum.value() - rf.total_to_pay_e.value(),
                                             f'Сдача от оплаты счета №{selected_rec_id}')
                rf.sum.setValue(rf.total_to_pay_e.value())
            if rf.payment_source_s.currentIndex() == 2:
                type_of_pay = 'C'
                if rf.sum.value() > rf.total_to_pay_e.value():
                    answer = show_question('Сдача по операции составляет ' +
                                           str(rf.sum.value() - rf.total_to_pay_e.value()), 'Отмена',
                                           'Зачислить данную сумму на депозитный счет клиента')
                    if answer == 2:
                        db_change_client_balance(selected_client_id, type_of_pay,
                                                 rf.sum.value() - rf.total_to_pay_e.value(),
                                                 f'Сдача от оплаты счета №{selected_rec_id}')
                        rf.sum.setValue(rf.total_to_pay_e.value())
                    else:
                        return
            elif rf.payment_source_s.currentIndex() == 3:
                if rf.sum.value() > rf.total_to_pay_e.value():
                    rf.sum.setValue(rf.total_to_pay_e.value())
                db_change_client_balance(selected_client_id, 'O', -rf.sum.value(), f'Оплата счета №{selected_rec_id}')
                type_of_pay = 'O'
            elif rf.payment_source_s.currentIndex() > 3:
                type_of_pay = 'I'
                query = db_insur_sel(rf.payment_source_s.currentText()[11:len(rf.payment_source_s.currentText()) - 1])
                query = query.sourceModel().query()
                query.first()
                insurance_id = query.value(0)
            db_pay_ins(selected_rec_id, insurance_id, type_of_pay, rf.sum.value(), rf.pay_comment_e.text())
            rf.payed_e.setValue(rf.payed_e.value() + rf.sum.value())
            rf.total_to_pay_e.setValue(rf.total_to_pay_e.value() - rf.sum.value())
            rf.payment_source_s.setCurrentIndex(0)
            rf.sum.clear()
            rf.pay_comment_e.clear()
            show_info(f'Транзакция успешно проведена')
    else:
        show_error('Сначала необходимо сохранить запись.', 'Ок')


def pay_all():
    pay(pay_all_flag=True)


def client_balance_sel():
    if rf.payment_source_s.currentIndex() == 3:
        rec = mw.rec_v.model().sourceModel().query()
        rec.seek(mw.rec_v.selectedIndexes()[0].row())
        show_info('Баланс депозитного счета клиента составляет ' + str(db_client_balance_sel(rec.value(1))) + ' руб')


rf.client_find_b.clicked.connect(open_client_find)
rf.serv_sel_b.clicked.connect(rec_serv_sel)
rf.serv_v.doubleClicked.connect(rec_serv_sel)
rf.serv_unsel_b.clicked.connect(rec_serv_unsel)
rf.serv_sel_v.doubleClicked.connect(rec_serv_unsel)
rf.serv_e.textEdited.connect(serv_find)
rf.save_b.clicked.connect(rec_ins)
rf.del_b.clicked.connect(rec_form_del)
rf.pay_b.clicked.connect(pay)
rf.pay_all_b.clicked.connect(pay_all)
rf.payment_source_s.currentIndexChanged.connect(client_balance_sel)
rf.cancel_b.clicked.connect(recording_form.close)

# ############################################################################################ #
# ----------------------------------- ФОРМА ПОИСКА КЛИЕНТА ----------------------------------- #
# ############################################################################################ #
client_find_form = QWidget()
cff = Ui_ClientFindForm()
cff.setupUi(client_find_form)


def client_find():
    if len(cff.ln_e.text()) > 2 or len(cff.fn_e.text()) > 2:
        cff.view.setModel(db_client_sel(cff.ln_e.text().capitalize(), cff.fn_e.text().capitalize(),
                                        cff.mn_e.text().capitalize(), None, None)[1])
        cff.view.hideColumn(0)
    else:
        show_error('Для поиска необходимы фамилия или имя клиента, длиной не менее 3 символов.', 'Ок')


def close_client_find():
    global selected_client_id
    clients = cff.view.model().sourceModel().query()
    clients.seek(cff.view.selectedIndexes()[0].row())
    selected_client_id = int(clients.value(0))
    rf.client_name.setText(clients.value(1) + ' ' + clients.value(2) + ' ' + clients.value(3))
    rf.phone.setText(clients.value(4))
    rf.phone2.setText(clients.value(5))
    rf.discount_e.setValue(int(clients.value(6)))
    rf.payment_source_s.clear()
    rf.payment_source_s.addItem('Выберите источник оплаты...')
    rf.payment_source_s.addItem('Наличные')
    rf.payment_source_s.addItem('Безналичный расчет')
    query = db_client_insur_sel(selected_client_id).sourceModel().query()
    query.first()
    if query.value(1):
        rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
        while query.next():
            rf.payment_source_s.addItem('Страховая "' + query.value(1) + '"')
    client_find_form.close()


cff.sel_b.clicked.connect(client_find)
cff.view.doubleClicked.connect(close_client_find)
cff.ins_b.clicked.connect(open_client_add)

# ########################################################################################### #
# ------------------------------------ ТЕХНИЧЕСКАЯ ФОРМА ------------------------------------ #
# ########################################################################################### #
technical_form = QWidget()
tf = Ui_TechnicalForm()
tf.setupUi(technical_form)


def technical_upd():
    db_technical_upd(tf.name_e.text(), tf.start_tm_e.time().toString('HH:mm'),
                     tf.end_tm_e.time().toString('HH:mm'))
    rf.start_time_e.setMinimumTime(tf.start_tm_e.time())
    rf.end_time_e.setMinimumTime(tf.start_tm_e.time())
    rf.start_time_e.setMaximumTime(tf.end_tm_e.time())
    rf.end_time_e.setMaximumTime(tf.end_tm_e.time())
    technical_form.close()
    show_info('Информация успешно сохранена')


tf.save_b.clicked.connect(technical_upd)
tf.cancel_b.clicked.connect(technical_form.close)

# ########################################################################################### #
# ------------------------------- ФОРМА СОЗДАНИЯ ОТЧЕТА ПО ЗП ------------------------------- #
# ########################################################################################### #
salary_report_form = QWidget()
srf = Ui_SalaryReportForm()
srf.setupUi(salary_report_form)


def set_cur_month_period():
    salary_report_set_period(QDate.currentDate())


def set_pre_month_period():
    salary_report_set_period(QDate.currentDate().addMonths(-1))


def reset_period():
    salary_report_set_period()


def find_directory():
    filename = QFileDialog.getSaveFileName(salary_report_form, 'Сохранение отчета по зарплатам врачей',
                                           srf.directory_e.text(), 'Файлы Excel (*.xlsx)')[0]
    filename = filename.replace('/', '\\')
    srf.directory_e.setText(filename)


def create_salary_report():
    if srf.start_dt_e.date() > srf.end_dt_e.date():
        show_error('Начало периода должно быть меньше или равно концу периода', 'Ок')
    elif not os.path.isdir(os.path.dirname(srf.directory_e.text())):
        show_error('Выберите существующую директорию', 'Ок')
    elif os.path.splitext(srf.directory_e.text())[1] != '.xlsx':
        show_error('Файл должен иметь расширение .xlsx', 'Ок')
    else:
        report = pandas.DataFrame(db_salary_report_sel(srf.start_dt_e.date().toString('yyyy-MM-dd'),
                                                       srf.end_dt_e.date().toString('yyyy-MM-dd')))
        sheet_name = srf.start_dt_e.date().toString('yyyy-MM-dd - ') + srf.end_dt_e.date().toString('yyyy-MM-dd')
        report.to_excel(srf.directory_e.text(), sheet_name=sheet_name, index=False)
        salary_report_form.close()
        show_info('Отчет успешно создан и сохранен. Путь к файлу: ' + srf.directory_e.text())


srf.cur_month_b.clicked.connect(set_cur_month_period)
srf.pre_month_b.clicked.connect(set_pre_month_period)
srf.start_dt_e.dateChanged.connect(reset_period)
srf.end_dt_e.dateChanged.connect(reset_period)
srf.find_dir_b.clicked.connect(find_directory)
srf.create_b.clicked.connect(create_salary_report)
srf.cancel_b.clicked.connect(salary_report_form.close)

# ########################################################################################### #
# ------------------------------------ ФОРМА МАТЕРИАЛОВ ------------------------------------- #
# ########################################################################################### #
material_form = QWidget()
mf = Ui_MaterialForm()
mf.setupUi(material_form)


def mater_save():
    if mf.name_e.text() == '':
        show_error('Введите название материала', 'Ок')
    else:
        if mf.del_b.isVisible():
            sel = mw.mater_v.selectedIndexes()[0]
            db_mater_upd(mf.name_e.text().capitalize(), mf.comment_e.text(),
                         sel.model().data(sel.model().index(sel.row(), 0)))
            show_info(f'Материал "{mf.name_e.text().capitalize()}" успешно изменен')
            mater_sel()
        else:
            db_mater_ins(mf.name_e.text().capitalize(), mf.comment_e.text())
            show_info(f'Материал "{mf.name_e.text().capitalize()}" успешно добавлен')
        material_form.close()


mf.save_b.clicked.connect(mater_save)
mf.del_b.clicked.connect(mater_del)
mf.cancel_b.clicked.connect(material_form.close)

# ########################################################################################### #
# ---------------------------- ФОРМА ИЗМЕНЕНИЕ КОЛ-ВА МАТЕРИАЛОВ ---------------------------- #
# ########################################################################################### #
material_amount_form = QWidget()
maf = Ui_MaterialAmountForm()
maf.setupUi(material_amount_form)


def mater_add():
    sel = mw.mater_v.selectedIndexes()[0]
    amount = maf.amount_e.value()
    if maf.add_b.text() == 'Уменьшить':
        amount *= -1
    if int(sel.model().data(sel.model().index(sel.row(), 2))) + amount >= 0:
        db_mater_add(amount, sel.model().data(sel.model().index(sel.row(), 0)))
        mater_sel()
        material_amount_form.close()
        show_info(f'Количество материала успешно изменено')
    else:
        show_error('Количество материала после изменения должно быть больше либо равно 0', 'Ок')


maf.add_b.clicked.connect(mater_add)
maf.cancel_b.clicked.connect(material_amount_form.close)

# ########################################################################################### #
# --------------------------------------- ФОРМА ЗАДАЧ --------------------------------------- #
# ########################################################################################### #
task_form = QWidget()
taf = Ui_TaskForm()
taf.setupUi(task_form)


def task_save():
    if taf.name_e.text() == '':
        show_error('Введите название задачи', 'Ок')
    else:
        if taf.del_b.isVisible():
            sel = mw.task_v.selectedIndexes()[0]
            db_task_upd(taf.name_e.text().capitalize(), taf.dt_e.date().toString('yyyy-MM-dd'),
                        taf.status_s.currentIndex(), taf.doctor_s.currentText(), taf.comment_e.text(),
                        sel.model().data(sel.model().index(sel.row(), 0)))
            task_sel()
            show_info(f'Задача "{mf.name_e.text().capitalize()}" успешно изменена')
        else:
            db_task_ins(taf.name_e.text().capitalize(), taf.dt_e.date().toString('yyyy-MM-dd'),
                        taf.status_s.currentIndex(), taf.doctor_s.currentText(), taf.comment_e.text())
            show_info(f'Задача "{taf.name_e.text().capitalize()}" успешно добавлена')
        task_form.close()


taf.save_b.clicked.connect(task_save)
taf.del_b.clicked.connect(task_del)
taf.cancel_b.clicked.connect(task_form.close)

# ########################################################################################### #
# -------------------------------------- ФОРМА ОТЧЕТОВ -------------------------------------- #
# ########################################################################################### #
reports_form = QWidget()
repf = Ui_ReportsForm()
repf.setupUi(reports_form)


def create_histogram(sets, categories, x_name, y_name):
    series = QtCharts.QStackedBarSeries()
    for s in sets:
        bar_set = QtCharts.QBarSet(s)
        bar_set.append(sets[s])
        series.append(bar_set)
    chart = QtCharts.QChart()
    chart.addSeries(series)
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
    axis_x = QtCharts.QBarCategoryAxis()
    axis_x.append(categories)
    axis_x.setTitleText(x_name)
    axis_y = QtCharts.QValueAxis()
    axis_y.setTitleText(y_name)
    chart.addAxis(axis_x, Qt.AlignBottom)
    chart.addAxis(axis_y, Qt.AlignLeft)
    series.attachAxis(axis_x)
    series.attachAxis(axis_y)
    chart_view = QtCharts.QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)
    chart_view.chart().setTheme(QtCharts.QChart.ChartThemeLight)
    size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    size_policy.setHeightForWidth(chart_view.sizePolicy().hasHeightForWidth())
    chart_view.setSizePolicy(size_policy)
    chart_view.setMinimumSize(QSize(0, 300))
    return chart_view


def rep_rec_upd():
    if repf.rec_v.itemAt(0) is not None:
        repf.rec_v.itemAt(0).widget().deleteLater()
    lists = db_rec_report(repf.rec_start_dt.date().toString('yyyy-MM-dd'),
                          repf.rec_end_dt.date().toString('yyyy-MM-dd'),
                          repf.rec_days_r.isChecked())
    repf.rec_v.addWidget(create_histogram({'Первичные приемы': lists[1], 'Повторные приемы': lists[2]}, lists[0],
                                          'Период', 'Кол-во приемов'))


def rep_rec_days():
    repf.rec_months_r.setChecked(False)


def rep_rec_months():
    repf.rec_days_r.setChecked(False)


def rep_serv_upd():
    if repf.serv_v.itemAt(0) is not None:
        repf.serv_v.itemAt(0).widget().deleteLater()
    keys, values = db_serv_report(repf.serv_start_dt.date().toString('yyyy-MM-dd'),
                                  repf.serv_end_dt.date().toString('yyyy-MM-dd'), repf.serv_cat_r.isChecked())
    repf.serv_v.addWidget(create_histogram({'Услуги': values}, keys, '', 'Количество'))


def rep_serv_serv():
    repf.serv_cat_r.setChecked(False)


def rep_serv_cat():
    repf.serv_serv_r.setChecked(False)


def rep_fin_upd():
    if repf.fin_v.itemAt(0) is not None:
        repf.fin_v.itemAt(0).widget().deleteLater()
    name = 'Доход'
    osx = 'Период'
    osy = 'Сумма'
    report_type = 0
    if repf.fin_outcome_r.isChecked():
        name = 'Расход'
        report_type = 1
    elif repf.fin_profit_r.isChecked():
        name = 'Прибыль'
        report_type = 2
    elif repf.fin_payment_type_r.isChecked():
        name = 'Тип платежа'
        osx = ''
        osy = 'Количество'
        report_type = 3
    keys, values = db_fin_report(repf.fin_start_dt.date().toString('yyyy-MM-dd'),
                                 repf.fin_end_dt.date().toString('yyyy-MM-dd'), repf.fin_days_r.isChecked(),
                                 report_type)
    repf.fin_v.addWidget(create_histogram({name: values}, keys, osx, osy))


def rep_fin_days():
    repf.fin_months_r.setChecked(False)


def rep_fin_months():
    repf.fin_days_r.setChecked(False)


def rep_fin_income():
    repf.fin_outcome_r.setChecked(False)
    repf.fin_profit_r.setChecked(False)
    repf.fin_payment_type_r.setChecked(False)


def rep_fin_outcome():
    repf.fin_income_r.setChecked(False)
    repf.fin_profit_r.setChecked(False)
    repf.fin_payment_type_r.setChecked(False)


def rep_fin_profit():
    repf.fin_outcome_r.setChecked(False)
    repf.fin_income_r.setChecked(False)
    repf.fin_payment_type_r.setChecked(False)


def rep_fin_payment_type():
    repf.fin_outcome_r.setChecked(False)
    repf.fin_profit_r.setChecked(False)
    repf.fin_income_r.setChecked(False)


repf.rec_upd_b.clicked.connect(rep_rec_upd)
repf.rec_days_r.clicked.connect(rep_rec_days)
repf.rec_months_r.clicked.connect(rep_rec_months)
repf.serv_upd_b.clicked.connect(rep_serv_upd)
repf.serv_serv_r.clicked.connect(rep_serv_serv)
repf.serv_cat_r.clicked.connect(rep_serv_cat)
repf.fin_upd_b.clicked.connect(rep_fin_upd)
repf.fin_days_r.clicked.connect(rep_fin_days)
repf.fin_months_r.clicked.connect(rep_fin_months)
repf.fin_income_r.clicked.connect(rep_fin_income)
repf.fin_outcome_r.clicked.connect(rep_fin_outcome)
repf.fin_profit_r.clicked.connect(rep_fin_profit)
repf.fin_payment_type_r.clicked.connect(rep_fin_payment_type)

# ########################################################################################### #
# -------------------------------- ФОРМА СОЗДАНИЯ ТРАНЗАКЦИИ -------------------------------- #
# ########################################################################################### #
transaction_form = QWidget()
trf = Ui_TransactionForm()
trf.setupUi(transaction_form)


def make_transaction():
    if trf.trans_source_s.currentIndex() == 0:
        show_error('Выберите источник оплаты', 'Ок')
    elif trf.amount_e.value() == 0:
        show_error('Введите сумму транзакции', 'Ок')
    else:
        type_of_trans = 'N'
        if ccbf.trans_source_s.currentText() == 'Безналичный расчет':
            type_of_trans = 'C'
        db_make_transaction(type_of_trans, trf.amount_e.value(), trf.comment_e.text())
        transaction_form.close()
        show_info('Транзакция успешно проведена')


trf.make_b.clicked.connect(make_transaction)
trf.cancel_b.clicked.connect(transaction_form.close)

# ########################################################################################### #
# ------------------------------ ФОРМА ПРОСМОТРА ПОЛЬЗОВАТЕЛЕЙ ------------------------------ #
# ########################################################################################### #
show_users_form = QWidget()
suf = Ui_ShowUsersForm()
suf.setupUi(show_users_form)


def open_user_ins():
    if is_admin:
        uf.login_e.clear()
        uf.login_e.setEnabled(True)
        uf.pass_e.clear()
        uf.pass2_e.clear()
        uf.type_s.setCurrentIndex(0)
        uf.comment_e.clear()
        uf.del_b.setVisible(False)
        user_form.show()
    else:
        show_error('Создание пользователей доступно только администраторам системы', 'ОК')


def open_user_upd():
    if len(suf.view.selectedIndexes()) > 0:
        model = suf.view.selectedIndexes()[0].model()
        row = suf.view.selectedIndexes()[0].row()
        if is_admin or model.data(model.index(row, 0)) == user_name:
            uf.login_e.setText(model.data(model.index(row, 0)))
            uf.login_e.setEnabled(False)
            uf.pass_e.clear()
            uf.pass2_e.clear()
            uf.type_s.setCurrentIndex(1)
            if model.data(model.index(row, 1)) == 'Пользователь':
                uf.type_s.setCurrentIndex(0)
                uf.type_s.setEnabled(False)
            uf.comment_e.setText(model.data(model.index(row, 2)))
            uf.del_b.setVisible(True)
            user_form.show()
        else:
            show_error('Пользователям разрешено изменять только свои данные', 'Ок')
    else:
        show_error('Выберите хотя-бы одного пользователя', 'ОК')


def user_del():
    if is_admin:
        if len(suf.view.selectedIndexes()) > 0:
            rows = []
            for i in suf.view.selectedIndexes():
                if i.model().data(i.model().index(i.row(), 1)) == 'Администратор' and i.row() not in rows:
                    rows.append(i.row())
                if i.model().data(i.model().index(i.row(), 0)) == user_name:
                    show_error('Удалять текущего пользователя запрещено', 'Ок')
                    return 0
            if db_admin_cnt_sel() - len(rows) == 0:
                show_error('Удалять всех администраторов системы запрещено', 'Ок')
            elif show_confirmation('удалить выбранных пользователей') == 'yes':
                db_user_del(suf.view.selectedIndexes())
                suf.view.setModel(db_user_sel())
                suf.view.resizeColumnsToContents()
                user_form.close()
        else:
            show_error('Выберите хотя-бы одного пользователя', 'ОК')
    else:
        show_error('Удаление пользователей доступно только администраторам системы', 'ОК')


suf.ins_b.clicked.connect(open_user_ins)
suf.upd_b.clicked.connect(open_user_upd)
suf.view.doubleClicked.connect(open_user_upd)
suf.del_b.clicked.connect(user_del)
suf.cancel_b.clicked.connect(show_users_form.close)

# ########################################################################################### #
# ------------------------------ ФОРМА ИЗМЕНЕНИЙ ПОЛЬЗОВАТЕЛЯ ------------------------------- #
# ########################################################################################### #
user_form = QWidget()
uf = Ui_UserForm()
uf.setupUi(user_form)


def user_save():
    if uf.login_e.text() == '' or uf.pass_e.text() == '' or uf.pass2_e.text() == '':
        show_error('Введите имя пользователя и его пароль дважды', 'Ок')
    elif uf.pass_e.text() != uf.pass2_e.text():
        show_error('Пароль не совпадает с его подтверждением', 'Ок')
        uf.pass_e.clear()
        uf.pass2_e.clear()
    else:
        user_type = 'A'
        if uf.type_s.currentIndex() == 0:
            user_type = 'U'
        if uf.del_b.isVisible():
            db_user_upd(uf.login_e.text().lower(), uf.pass_e.text(), user_type, uf.comment_e.text())
            suf.view.setModel(db_user_sel())
            suf.view.resizeColumnsToContents()
            show_info(f'Пользователь "{uf.login_e.text().lower()}" успешно изменен')
            global is_admin
            is_admin = db_check_user(uf.login_e.text().lower())[0] == 'A'
        else:
            if db_check_user(uf.login_e.text().lower())[0] is None:
                db_user_ins(uf.login_e.text().lower(), uf.pass_e.text(), user_type, uf.comment_e.text())
                show_info(f'Пользователь "{uf.login_e.text().lower()}" успешно создан')
            else:
                show_error(f'Пользователь {uf.login_e.text().lower()} уже существует', 'Ок')
                uf.login_e.clear()
                uf.pass_e.clear()
                uf.pass2_e.clear()
                uf.comment_e.clear()
                return 0
        suf.view.setModel(db_user_sel())
        suf.view.resizeColumnsToContents()
        user_form.close()


uf.save_b.clicked.connect(user_save)
uf.del_b.clicked.connect(user_del)
uf.cancel_b.clicked.connect(user_form.close)

# ########################################################################################### #
# ------------------------------------ ЗАПУСК ПРИЛОЖЕНИЯ ------------------------------------ #
# ########################################################################################### #
LoginForm.show()

# ТЕСТ #
ui_login.loginEdit.setText('admin')
ui_login.passEdit.setText('admin')
ui_login.enterButton.click()
# ТЕСТ #

sys.exit(app.exec_())
