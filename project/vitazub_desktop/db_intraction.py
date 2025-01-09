from sqlite3 import connect

from PySide2.QtCore import QSortFilterProxyModel, Qt, QModelIndex
from PySide2.QtGui import QBrush, QColor
from PySide2.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from config import db_name

db_for_idu = connect('')


def db_check_user(login, password=None):
    query = f"SELECT TYPE, NAME\n" +\
            f"FROM D_USER\n" +\
            f"WHERE NAME = '{login}'"
    if password is not None:
        query += f" AND PASSWORD = '{password}'"
    query = QSqlQuery(query + ';')
    query.first()
    return [query.value(0), query.value(1)]


def connect_db(login, password):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_name())
    db.open()
    if db.isOpenError():
        return [db.lastError()]
    else:
        global db_for_idu
        db_for_idu = connect(db_name())
        return db_check_user(login, password)


def db_client_sel(ln, fn, mn, min_next_visit_dt, max_next_visit_dt):
    client_count = f"SELECT COUNT(1) FROM V_CLIENT\n"\
                   f"WHERE LAST_NAME LIKE '%{ln}%' AND FIRST_NAME LIKE '%{fn}%'\n"\
                   f"      AND MIDDLE_NAME LIKE '%{mn}%'\n"
    if min_next_visit_dt is not None:
        client_count += f"      AND NEXT_VISIT_DT BETWEEN DATE('{min_next_visit_dt}') AND DATE('{max_next_visit_dt}')\n"
    client_count = QSqlQuery(client_count + ';')
    client_count.first()
    client_count = client_count.value(0)
    query = f"SELECT H_CLIENT_ID, LAST_NAME AS \"Фамилия\", FIRST_NAME AS \"Имя\", \n"\
            f"       MIDDLE_NAME AS \"Отчество\", PHONE AS \"Телефон\", "\
            f"       ADDITIONAL_PHONE AS \"Дополнительный телефон\", DISCOUNT AS \"Скидка\", \n"\
            f"       BIRTH_DT AS \"Дата рождения\", NEXT_VISIT_DT AS \"Дата следующего посещения\", \n"\
            f"       BALANCE_AMT AS \"Баланс\", COMMENT AS \"Комментарий\"\n"\
            f"FROM V_CLIENT\n"\
            f"WHERE LAST_NAME LIKE '%{ln}%' AND FIRST_NAME LIKE '%{fn}%' AND MIDDLE_NAME LIKE '%{mn}%'\n"
    if min_next_visit_dt is not None:
        query += f"      AND NEXT_VISIT_DT BETWEEN DATE('{min_next_visit_dt}') AND DATE('{max_next_visit_dt}')\n"
    query += f"ORDER BY NEXT_VISIT_DT DESC\nLIMIT 100;"
    model = QSqlQueryModel()
    model.setQuery(query)
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return [client_count, sorting_model]


def db_client_ins(s_name, f_name, l_name, phone, phone2, birth_dt, discount, comment):
    discount = discount or 0
    db_for_idu.execute(f"INSERT INTO V_CLIENT (LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE, \n"
                       f"ADDITIONAL_PHONE, DISCOUNT, BIRTH_DT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{s_name}', '{f_name}', '{l_name}', '{phone}', '{phone2}', \n"
                       f"{discount}, date('{birth_dt}'), '{comment}', '1');")
    db_for_idu.commit()


def db_client_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_CLIENT\n"
                           f"WHERE H_CLIENT_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()
    return 0


def db_client_upd(ln, fn, mn, phone, phone2, birth_dt, discount, comment, is_notified, id):
    query = f"UPDATE S_CLIENT\n"\
            f"SET LAST_NAME = '{ln}', FIRST_NAME = '{fn}', MIDDLE_NAME = '{mn}', PHONE = '{phone}', \n"\
            f"    ADDITIONAL_PHONE = '{phone2}', DISCOUNT = {discount}, BIRTH_DT = date('{birth_dt}'), \n"\
            f"    COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'"
    if is_notified:
        query += ', NEXT_VISIT_DT = NULL'
    query += f"\nWHERE H_CLIENT_ID = {id};"
    db_for_idu.execute(query)
    db_for_idu.commit()


def db_insur_ins(name, comment):
    db_for_idu.execute(f"INSERT INTO V_INSURANCE (NAME, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{name}', '{comment}', '1');")
    db_for_idu.commit()


def db_insur_sel(name):
    model = QSqlQueryModel()
    model.setQuery(f"SELECT H_INSURANCE_ID, NAME AS \"Название\", COMMENT AS \"Комментарий\"\n"
                   f"FROM V_INSURANCE\n"
                   f"WHERE NAME LIKE '%{name}%'\n"
                   f"ORDER BY NAME ASC;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_insur_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_INSURANCE\n"
                           f"WHERE H_INSURANCE_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()
    return 0


def db_insur_upd(name, comment, id):
    db_for_idu.execute(f"UPDATE S_INSURANCE\n"
                       f"SET NAME = '{name}', COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE H_INSURANCE_ID = {id};")
    db_for_idu.commit()


def db_doctor_ins(ln, fn, mn, phone, phone2, rate, spec, comment):
    db_for_idu.execute(f"INSERT INTO V_DOCTOR (LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE, ADDITIONAL_PHONE, RATE, \n"
                       f"    SPECIALIZATION, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{ln}', '{fn}', '{mn}', '{phone}', '{phone2}', {rate}, '{spec}', '{comment}', '1');")
    db_for_idu.commit()


def db_doctor_sel(ln, fn, mn):
    model = QSqlQueryModel()
    model.setQuery(f"SELECT H_DOCTOR_ID, LAST_NAME AS \"Фамилия\", FIRST_NAME AS \"Имя\",MIDDLE_NAME AS \"Отчество\",\n"
                   f"       PHONE AS \"Телефон\", ADDITIONAL_PHONE AS \"Дополнительный телефон\", \n"
                   f"       RATE AS \"Ставка\", SPECIALIZATION AS \"Специализация\", COMMENT AS \"Комментарий\"\n"
                   f"FROM V_DOCTOR\n"
                   f"WHERE LAST_NAME LIKE '%{ln}%' AND FIRST_NAME LIKE '%{fn}%' AND MIDDLE_NAME LIKE '%{mn}%'\n"
                   f"ORDER BY LAST_NAME, FIRST_NAME, MIDDLE_NAME ASC;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_doctor_sel_by_id(doctor_id):
    query = QSqlQuery(f"SELECT LAST_NAME || ' ' || FIRST_NAME || ' ' || MIDDLE_NAME\n"
                      f"FROM V_DOCTOR\n"
                      f"WHERE H_DOCTOR_ID = {doctor_id};")
    query.first()
    return query.value(0)


def db_doctor_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_DOCTOR\n"
                           f"WHERE H_DOCTOR_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()
    return 0


def db_doctor_upd(ln, fn, mn, phone, phone2, rate, spec, comment, id):
    db_for_idu.execute(f"UPDATE S_DOCTOR\n"
                       f"SET LAST_NAME = '{ln}', FIRST_NAME = '{fn}', MIDDLE_NAME = '{mn}', PHONE = '{phone}', \n"
                       f"    ADDITIONAL_PHONE = '{phone2}', RATE = {rate}, \n"
                       f"    D_SPECIALIZATION_ID = (SELECT D_SPECIALIZATION_ID FROM D_SPECIALIZATION\n"
                       f"                           WHERE NAME = '{spec}'),\n"
                       f"    COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE H_DOCTOR_ID = {id};")
    db_for_idu.commit()


def db_spec_sel():
    model = QSqlQueryModel()
    model.setQuery("SELECT \"Выберите специализацию врача...\" AS NAME\n"
                   "UNION ALL\n"
                   "SELECT NAME FROM D_SPECIALIZATION\n"
                   "UNION ALL\n"
                   "SELECT \"Отсутствует\" AS NAME;")
    return model


def db_serv_ins(serv_category, mkb, name, price, comment):
    db_for_idu.execute(f"INSERT INTO V_SERVICE (SERVICE_CATEGORY, MKB_ID, NAME, PRICE, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{serv_category}', '{mkb}', '{name}', {price}, '{comment}', '1');")
    db_for_idu.commit()


def db_serv_sel(filter):
    model = QSqlQueryModel()
    model.setQuery(f"SELECT H_SERVICE_ID, MKB_ID AS \"Номер МКБ\", NAME AS \"Название\", \n"
                   f"       SERVICE_CATEGORY AS \"Категория\", PRICE AS \"Цена\", \n"
                   f"       COMMENT AS \"Комментарий\"\n"
                   f"FROM V_SERVICE\n"
                   f"WHERE MKB_ID LIKE '%{filter.upper()}%' OR NAME LIKE '%{filter}%' "
                   f"      OR SERVICE_CATEGORY LIKE '%{filter}%'\n"
                   f"ORDER BY NAME ASC;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_serv_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_SERVICE\n"
                           f"WHERE H_SERVICE_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()
    return 0


def db_serv_upd(serv_category, mkb, name, price, comment, id):
    db_for_idu.execute(f"UPDATE S_SERVICE\n"
                       f"SET MKB_ID = '{mkb}', \n"
                       f"    D_SERVICE_CATEGORY_ID = (SELECT D_SERVICE_CATEGORY_ID FROM D_SERVICE_CATEGORY\n"
                       f"                             WHERE NAME = '{serv_category}'), \n"
                       f"    NAME = '{name}', PRICE = '{price}', COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE H_SERVICE_ID = {id};")
    db_for_idu.commit()


def db_make_serv_list(serv_dict):
    model = QSqlQueryModel()
    query = ''
    if serv_dict == {}:
        query = f"SELECT H_SERVICE_ID, MKB_ID AS \"Номер МКБ\", NAME AS \"Название\", \n" \
                 f"       SERVICE_CATEGORY AS \"Категория\", PRICE AS \"Цена\", 0 AS \"Количество\"\n" \
                 f"FROM V_SERVICE\n" \
                 f"WHERE H_SERVICE_ID = -1\n" \
                 f"UNION ALL\n"
    else:
        for i in serv_dict.keys():
            query += f"SELECT H_SERVICE_ID, MKB_ID AS \"Номер МКБ\", NAME AS \"Название\", \n" \
                     f"       SERVICE_CATEGORY AS \"Категория\", PRICE AS \"Цена\", {serv_dict[i]} AS \"Количество\"\n" \
                     f"FROM V_SERVICE\n" \
                     f"WHERE H_SERVICE_ID = {i}\n" \
                     f"UNION ALL\n"
    query = query[0:len(query)-11] + ';'
    model.setQuery(query)
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_find_serv_list(rec_id):
    selected_services = {}
    query = QSqlQuery(f"SELECT H_SERVICE_ID, AMOUNT\n"
                      f"FROM L_REC_SERVICE\n"
                      f"WHERE L_RECORDING_ID = {rec_id};")
    if query.first():
        while True:
            selected_services.update([(query.value(0), query.value(1))])
            if not query.next():
                break
    return selected_services


def db_category_sel():
    model = QSqlQueryModel()
    model.setQuery("SELECT \"Выберите категорию услуги...\" AS NAME\n"
                   "UNION ALL\n"
                   "SELECT NAME FROM D_SERVICE_CATEGORY;")
    return model


def db_client_insur_sel(c_id, is_active=False):
    model = QSqlQueryModel()
    query = f"SELECT L_CLIENT_INSURANCE_ID, NAME AS \"Страховая компания\", \n"\
            f"       EFFECTIVE_FROM_DT AS \"Начало действия\", EFFECTIVE_TO_DT AS \"Конец действия\", \n"\
            f"       COMMENT AS \"Комментарий\"\n"\
            f"FROM V_CLIENT_INSURANCE\n"\
            f"WHERE H_CLIENT_ID = {c_id}\n"
    if is_active:
        query += "    AND DATETIME(CURRENT_TIMESTAMP, 'localtime') BETWEEN EFFECTIVE_FROM_DT AND EFFECTIVE_TO_DT\n"
    query += f"ORDER BY EFFECTIVE_FROM_DT ASC;"
    model.setQuery(query)
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_client_insur_ins(c_id, name, start_dt, end_dt, comment):
    db_for_idu.execute(f"INSERT INTO V_CLIENT_INSURANCE (H_CLIENT_ID, NAME, EFFECTIVE_FROM_DT, EFFECTIVE_TO_DT, \n"
                       f"    COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ({c_id}, '{name}', '{start_dt}', '{end_dt}', '{comment}', '1');")
    db_for_idu.commit()


def db_client_insur_upd(name, start_dt, end_dt, comment, ci_id):
    db_for_idu.execute(f"UPDATE L_CLIENT_INSURANCE\n"
                       f"SET H_INSURANCE_ID = (SELECT H_INSURANCE_ID FROM S_INSURANCE WHERE NAME = '{name}'), \n"
                       f"    EFFECTIVE_FROM_DT = '{start_dt}', EFFECTIVE_TO_DT = '{end_dt}', COMMENT = '{comment}', \n"
                       f"    SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE L_CLIENT_INSURANCE_ID = {ci_id};")
    db_for_idu.commit()


def db_client_insur_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM L_CLIENT_INSURANCE\n"
                           f"WHERE L_CLIENT_INSURANCE_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()


def db_check_rec_dttm(doctor_id, start_dttm, end_dttm, rec_id=None):
    query = str(f"SELECT COUNT(*) FROM V_RECORDING\n"
                f"WHERE H_DOCTOR_ID = {doctor_id} AND\n")
    if rec_id is not None:
        query += f"      L_RECORDING_ID <> {rec_id} AND\n"
    query += str(f"      (DATETIME('{start_dttm}') BETWEEN START_DTTM AND DATETIME(END_DTTM, '-1 second') OR\n"
                 f"       DATETIME('{end_dttm}') BETWEEN DATETIME(START_DTTM, '+1 second') AND END_DTTM OR\n"
                 f"       START_DTTM BETWEEN DATETIME('{start_dttm}') AND\n"
                 f"                          DATETIME(DATETIME('{end_dttm}'), '-1 second') OR\n"
                 f"       END_DTTM BETWEEN DATETIME(DATETIME('{start_dttm}'), '+1 second') AND\n"
                 f"                        DATETIME('{end_dttm}'));")
    query = QSqlQuery(query)
    query.first()
    return int(query.value(0)) == 0


def db_rec_ins(doctor_id, client_id, discount, services, start_dttm, end_dttm, comment):
    db_for_idu.execute(f"INSERT INTO V_RECORDING (H_DOCTOR_ID, H_CLIENT_ID, DISCOUNT, START_DTTM, END_DTTM, \n"
                       f"    COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ({doctor_id}, {client_id}, {discount}, '{start_dttm}', '{end_dttm}', '{comment}'\n"
                       f"        , '1');")
    db_for_idu.commit()
    rec_id = QSqlQuery(f"SELECT MAX(L_RECORDING_ID) FROM L_RECORDING;")
    rec_id.first()
    rec_id = rec_id.value(0)
    if services != {}:
        for i in services.keys():
            db_for_idu.execute(f"INSERT INTO L_REC_SERVICE (L_RECORDING_ID, H_SERVICE_ID, AMOUNT, SOURCE_SYSTEM_CD)\n"
                               f"VALUES ({rec_id}, {i}, {services[i]}, '1');")
        db_for_idu.commit()
    db_for_idu.execute(f"UPDATE S_L_RECORDING\n"
                       f"SET  DISCOUNT = {discount}\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.commit()


def db_rec_upd(discount, services, start_dttm, end_dttm, comment, rec_id):
    if services != {}:
        for i in services.keys():
            db_for_idu.execute(f"DELETE FROM L_REC_SERVICE\n"
                               f"WHERE L_RECORDING_ID = {rec_id};")
            db_for_idu.commit()
            db_for_idu.execute(f"INSERT INTO L_REC_SERVICE (L_RECORDING_ID, H_SERVICE_ID, AMOUNT, SOURCE_SYSTEM_CD)\n"
                               f"VALUES ({rec_id}, {i}, {services[i]}, '1');")
            db_for_idu.commit()
    db_for_idu.execute(f"UPDATE S_L_RECORDING\n"
                       f"SET  DISCOUNT = {discount}, START_DTTM = '{start_dttm}', END_DTTM = '{end_dttm}',\n"
                       f"     COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.commit()


def db_rec_del(rec_id):
    db_for_idu.execute(f"DELETE FROM S_L_RECORDING\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.execute(f"DELETE FROM L_REC_SERVICE\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.execute(f"DELETE FROM L_RECORDING\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.commit()


class ScheduleModel(QSqlQueryModel):
    def data(self, item: QModelIndex, role=None):
        if role == Qt.BackgroundRole:
            rec = self.query()
            rec.seek(item.row())
            if rec.value(4) == 'Свободно':
                return QBrush(QColor(153, 255, 153, 255))
            else:
                return QBrush(Qt.transparent)
        else:
            return super().data(item, role)


def db_schedule_sel(doctor_id, rec_dt):
    model = ScheduleModel()
    model.setQuery(f"SELECT L_RECORDING_ID, H_CLIENT_ID, START_TM \"Начало\", END_TM \"Конец\",\n"
                   f"       FIO \"ФИО клиента\", PHONE \"Телефон\", ADDITIONAL_PHONE \"Дополнительный телефон\",\n"
                   f"       IS_PAID \"Оплачено\", DISCOUNT \"Скидка\", COMMENT \"Комментарий\"\n"
                   f"FROM\n"
                   f"(SELECT NULL L_RECORDING_ID, NULL H_CLIENT_ID, \n"
                   f"    (SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='START_TM') START_TM, \n"
                   f"    COALESCE(STRFTIME('%H:%M', MIN(START_DTTM)), \n"
                   f"    (SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='END_TM')) END_TM, \n"
                   f"    'Свободно' FIO, NULL PHONE, NULL ADDITIONAL_PHONE, NULL IS_PAID, NULL DISCOUNT, NULL COMMENT\n"
                   f"FROM V_RECORDING\n"
                   f"WHERE H_DOCTOR_ID = {doctor_id}\n"
                   f"    AND STRFTIME('%Y-%m-%d', START_DTTM) = '{rec_dt}'\n"
                   f"UNION ALL\n"
                   f"SELECT L_RECORDING_ID, H_CLIENT_ID, \n"
                   f"    STRFTIME('%H:%M', START_DTTM) START_TM, \n"
                   f"    STRFTIME('%H:%M', END_DTTM) END_TM, \n"
                   f"    FIO, PHONE, ADDITIONAL_PHONE, IS_PAID, DISCOUNT, COMMENT\n"
                   f"FROM V_RECORDING\n"
                   f"WHERE H_DOCTOR_ID = {doctor_id}\n"
                   f"    AND STRFTIME('%Y-%m-%d', START_DTTM) = '{rec_dt}'\n"
                   f"UNION ALL\n"
                   f"SELECT NULL L_RECORDING_ID, NULL H_CLIENT_ID, \n"
                   f"    STRFTIME('%H:%M', END_DTTM) START_TM, \n"
                   f"    COALESCE(STRFTIME('%H:%M', LEAD(START_DTTM) OVER (ORDER BY START_DTTM)), \n"
                   f"             (SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='END_TM')) END_TM, \n"
                   f"    'Свободно' FIO, NULL PHONE, NULL ADDITIONAL_PHONE, NULL IS_PAID, NULL DISCOUNT, NULL COMMENT\n"
                   f"FROM V_RECORDING\n"
                   f"WHERE H_DOCTOR_ID = {doctor_id}\n"
                   f"    AND STRFTIME('%Y-%m-%d', START_DTTM) = '{rec_dt}') SH\n"
                   f"WHERE NOT (FIO == 'Свободно' AND START_TM == END_TM)\n"
                   f"ORDER BY START_TM;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_amounts_sel(rec_id):
    query = QSqlQuery(f"SELECT TO_PAY_AMOUNT, PAID_AMOUNT\n"
                      f"FROM S_L_RECORDING\n"
                      f"WHERE L_RECORDING_ID = {rec_id};")
    query.first()
    return [query.value(0), query.value(1)]


def db_pay_ins(rec_id, insurance_id, type_of_pay, amount, comment):
    db_for_idu.execute(f"INSERT INTO V_TRANSACTION (L_RECORDING_ID, H_CLIENT_ID, H_INSURANCE_ID, "
                       f"    TYPE, AMOUNT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ({rec_id}, NULL, {insurance_id}, '{type_of_pay}', {amount}, '{comment}' , '1');")
    db_for_idu.execute(f"UPDATE S_L_RECORDING\n"
                       f"SET PAID_AMOUNT = (SELECT PAID_AMOUNT FROM S_L_RECORDING WHERE L_RECORDING_ID = {rec_id})\n"
                       f"                  + {amount}\n"
                       f"WHERE L_RECORDING_ID = {rec_id};")
    db_for_idu.commit()


def db_change_client_balance(client_id, type_of_trans, amount, comment):
    db_for_idu.execute(f"INSERT INTO V_TRANSACTION (L_RECORDING_ID, H_CLIENT_ID, H_INSURANCE_ID, "
                       f"    TYPE, AMOUNT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES (NULL, {client_id}, NULL, '{type_of_trans}', {amount}, '{comment}' , '1');")
    db_for_idu.execute(f"UPDATE S_CLIENT\n"
                       f"SET BALANCE_AMT = (SELECT BALANCE_AMT FROM S_CLIENT WHERE H_CLIENT_ID = {client_id})\n"
                       f"                  + {amount}\n"
                       f"WHERE H_CLIENT_ID = {client_id};")
    db_for_idu.commit()


def db_client_balance_sel(client_id):
    balance = QSqlQuery(f"SELECT BALANCE_AMT FROM S_CLIENT WHERE H_CLIENT_ID={client_id};")
    balance.first()
    balance = balance.value(0)
    return balance


def db_technical_sel():
    name = QSqlQuery("SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='CLINIC_NAME';")
    start_tm = QSqlQuery("SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='START_TM';")
    end_tm = QSqlQuery("SELECT D_VALUE FROM D_TECHNICAL WHERE D_KEY='END_TM';")
    name.first()
    start_tm.first()
    end_tm.first()
    return [name.value(0), start_tm.value(0), end_tm.value(0)]


def db_technical_upd(name, start_tm, end_tm):
    db_for_idu.execute(f"UPDATE D_TECHNICAL\n"
                       f"SET D_VALUE = '{name}'\n"
                       f"WHERE D_KEY = 'CLINIC_NAME';")
    db_for_idu.execute(f"UPDATE D_TECHNICAL\n"
                       f"SET D_VALUE = '{start_tm}'\n"
                       f"WHERE D_KEY = 'START_TM';")
    db_for_idu.execute(f"UPDATE D_TECHNICAL\n"
                       f"SET D_VALUE = '{end_tm}'\n"
                       f"WHERE D_KEY = 'END_TM';")
    db_for_idu.commit()


def db_salary_report_sel(start_dt, end_dt):
    report = {'ФИО врача': [], 'Начало периода': [], 'Конец периода': [], 'Кол-во отработанных дней': [],
              'Кол-во проведенных приемов': [], 'Прибыль': [], 'Тариф': [], 'Заработная плата за период': []}
    sql_report = QSqlQuery(f"SELECT LAST_NAME || ' ' || FIRST_NAME || ' ' || MIDDLE_NAME FIO\n"
                           f"       ,'{start_dt}'\n"
                           f"       ,'{end_dt}'\n"
                           f"       ,COUNT(DISTINCT DATE(START_DTTM))\n"
                           f"       ,COUNT(1)\n"
                           f"       ,SUM(TO_PAY_AMOUNT)\n"
                           f"       ,RATE\n"
                           f"       ,ROUND(SUM(TO_PAY_AMOUNT) * RATE / 100, 2)\n"
                           f"FROM S_L_RECORDING S\n"
                           f"INNER JOIN L_RECORDING L\n"
                           f"ON S.L_RECORDING_ID = L.L_RECORDING_ID\n"
                           f"INNER JOIN S_DOCTOR D\n"
                           f"ON L.H_DOCTOR_ID = D.H_DOCTOR_ID\n"
                           f"WHERE DATE(START_DTTM) BETWEEN DATE('{start_dt}') AND DATE('{end_dt}')\n"
                           f"GROUP BY FIO, RATE;")
    sql_report.first()
    while True:
        for i, j in zip(report, range(8)):
            report[i].append(sql_report.value(j))
        if not sql_report.next():
            break
    return report


def db_mater_sel(name):
    model = QSqlQueryModel()
    model.setQuery(f"SELECT H_MATERIAL_ID, NAME AS \"Название\", AMOUNT AS \"Количество\", \n"
                   f"       COMMENT AS \"Комментарий\"\n"
                   f"FROM V_MATERIAL\n"
                   f"WHERE NAME LIKE '%{name}%'\n"
                   f"ORDER BY NAME ASC;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_mater_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_MATERIAL\n"
                           f"WHERE H_MATERIAL_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()


def db_mater_ins(name, comment):
    db_for_idu.execute(f"INSERT INTO V_MATERIAL (NAME, AMOUNT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{name}', 0, '{comment}', '1');")
    db_for_idu.commit()


def db_mater_upd(name, comment, id):
    db_for_idu.execute(f"UPDATE S_MATERIAL\n"
                       f"SET NAME = '{name}', COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE H_MATERIAL_ID = {id};")
    db_for_idu.commit()


def db_mater_add(amount, id):
    db_for_idu.execute(f"UPDATE S_MATERIAL\n"
                       f"SET AMOUNT = AMOUNT + {amount}\n"
                       f"WHERE H_MATERIAL_ID = {id};")
    db_for_idu.commit()


def db_task_sel(name, deadline, status):
    query = f"SELECT H_TASK_ID, NAME \"Название\", DEADLINE_DT \"Дедлайн\",\n"\
            f"       CASE WHEN DATE(CURRENT_TIMESTAMP, 'localtime') > DEADLINE_DT AND STATUS_CD <> '2' " \
            f"                 THEN 'Просрочено'\n"\
            f"            WHEN STATUS_CD = '0' THEN 'Не начато'\n"\
            f"            WHEN STATUS_CD = '1' THEN 'В работе'\n"\
            f"            WHEN STATUS_CD = '2' THEN 'Выполнено'\n"\
            f"       END \"Статус\", STATUS_CD, FIO \"Ответственный\", COMMENT \"Комментарий\"\n"\
            f"FROM V_TASK\n"\
            f"WHERE NAME LIKE '%{name}%'\n"\
            f"      AND DEADLINE_DT <= DATE('{deadline}')\n"
    if status == 'Не начато':
        query += f"      AND STATUS_CD == '0'\n"
    elif status == 'Просрочено':
        query += f"      AND DATE(CURRENT_TIMESTAMP, 'localtime') > DEADLINE_DT AND STATUS_CD <> '2'\n"
    elif status == 'В работе':
        query += f"      AND STATUS_CD == '1'\n"
    elif status == 'Выполнено':
        query += f"      AND STATUS_CD == '2'\n"
    query += f"ORDER BY DEADLINE_DT ASC;"
    model = QSqlQueryModel()
    model.setQuery(query)
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_task_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM V_TASK\n"
                           f"WHERE H_TASK_ID = {i.model().data(i.model().index(i.row(), 0))};")
    db_for_idu.commit()


def db_task_ins(name, deadline, status, fio, comment):
    db_for_idu.execute(f"INSERT INTO V_TASK (NAME, DEADLINE_DT, STATUS_CD, FIO, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{name}', '{deadline}', '{status}', '{fio}', '{comment}', '1');")
    db_for_idu.commit()


def db_task_upd(name, deadline, status, fio, comment, id):
    db_for_idu.execute(f"UPDATE V_TASK\n"
                       f"SET NAME = '{name}', DEADLINE_DT = '{deadline}', STATUS_CD = '{status}', FIO = '{fio}', \n"
                       f"    COMMENT = '{comment}', SOURCE_SYSTEM_CD = '1'\n"
                       f"WHERE H_TASK_ID = {id};")
    db_for_idu.commit()


def db_rec_report(start_dt, end_dt, by_day):
    dt_format = '%m.%Y'
    if by_day:
        dt_format = '%d.' + dt_format
    query = QSqlQuery(f"SELECT * FROM(\n"
                      f"	WITH F(REC_DT, CNT) AS (\n"
                      f"			SELECT STRFTIME('{dt_format}', REC_DT), COUNT(1)\n"
                      f"			FROM (SELECT H_CLIENT_ID, MIN(DATE(START_DTTM)) REC_DT\n"
                      f"			    FROM V_RECORDING\n"
                      f"			    GROUP BY H_CLIENT_ID)\n"
                      f"			WHERE REC_DT BETWEEN '{start_dt}' AND '{end_dt}'\n"
                      f"			GROUP BY 1\n"
                      f"		), R(REC_DT, CNT) AS (\n"
                      f"			SELECT STRFTIME('{dt_format}', REC_DT) REC_DT, COUNT(1) CNT\n"
                      f"			FROM (SELECT DATE(START_DTTM) REC_DT, \n"
                      f"				  MIN(DATE(START_DTTM)) OVER (PARTITION BY H_CLIENT_ID) FIRST_REC_DT\n"
                      f"				  FROM V_RECORDING)\n"
                      f"			WHERE REC_DT <> FIRST_REC_DT\n"
                      f"				  AND REC_DT BETWEEN '{start_dt}' AND '{end_dt}'\n"
                      f"			GROUP BY 1\n"
                      f"		)\n"
                      f"	SELECT F.REC_DT, F.CNT F_REC_CNT, COALESCE(R.CNT, 0) R_REC_CNT\n"
                      f"	FROM F\n"
                      f"	LEFT JOIN R\n"
                      f"	ON F.REC_DT = R.REC_DT\n"
                      f"	UNION ALL\n"
                      f"	SELECT R.REC_DT, 0 F_REC_CNT, R.CNT R_REC_CNT\n"
                      f"	FROM R\n"
                      f"	LEFT JOIN F\n"
                      f"	ON F.REC_DT = R.REC_DT\n"
                      f"	WHERE F.REC_DT IS NULL)\n"
                      f"ORDER BY REC_DT;")
    query.first()
    dates = []
    first_rec_cnt = []
    re_rec_cnt = []
    if query.value(0) is not None:
        while True:
            dates.append(query.value(0))
            first_rec_cnt.append(query.value(1))
            re_rec_cnt.append(query.value(2))
            if not query.next():
                break
    return [dates, first_rec_cnt, re_rec_cnt]


def sql_report_to_lists(query):
    query.first()
    keys = []
    values = []
    if query.value(0) is not None:
        while True:
            keys.append(query.value(0))
            values.append(query.value(1))
            if not query.next():
                break
    return keys, values


def db_serv_report(start_dt, end_dt, by_cat):
    name = 'S'
    join_cat = ''
    if by_cat:
        name = 'C'
        join_cat = 'JOIN D_SERVICE_CATEGORY C\nON S.D_SERVICE_CATEGORY_ID = C.D_SERVICE_CATEGORY_ID\n'
    query = QSqlQuery(f"SELECT {name}.NAME, SUM(RS.AMOUNT)\n"
                      f"FROM S_L_RECORDING R\n"
                      f"JOIN L_REC_SERVICE RS\n"
                      f"ON R.L_RECORDING_ID = RS.L_RECORDING_ID\n"
                      f"JOIN S_SERVICE S\n"
                      f"ON RS.H_SERVICE_ID = S.H_SERVICE_ID\n{join_cat}"
                      f"WHERE DATE(R.START_DTTM) BETWEEN '{start_dt}' AND '{end_dt}'\n"
                      f"GROUP BY 1\n"
                      f"ORDER BY 1;")
    return sql_report_to_lists(query)


def db_fin_report(start_dt, end_dt, by_day, report_type):
    dt_format = '%m.%Y'
    if by_day:
        dt_format = '%d.' + dt_format
    query = [QSqlQuery(f"SELECT STRFTIME('{dt_format}', LOAD_DTTM), SUM(AMOUNT)\n"
                       f"FROM V_TRANSACTION\n"
                       f"WHERE AMOUNT > 0\n"
                       f"    AND H_CLIENT_ID IS NULL\n"
                       f"    AND LOAD_DTTM BETWEEN '{start_dt}' AND '{end_dt}'\n"
                       f"GROUP BY 1\n"
                       f"ORDER BY 1;"),
             QSqlQuery(f"SELECT STRFTIME('{dt_format}', LOAD_DTTM), SUM(-AMOUNT)\n"
                       f"FROM V_TRANSACTION\n"
                       f"WHERE AMOUNT < 0\n"
                       f"    AND H_CLIENT_ID IS NULL\n"
                       f"    AND LOAD_DTTM BETWEEN '{start_dt}' AND '{end_dt}'\n"
                       f"GROUP BY 1\n"
                       f"ORDER BY 1;"),
             QSqlQuery(f"SELECT STRFTIME('{dt_format}', LOAD_DTTM), SUM(AMOUNT)\n"
                       f"FROM V_TRANSACTION\n"
                       f"WHERE H_CLIENT_ID IS NULL\n"
                       f"    AND LOAD_DTTM BETWEEN '{start_dt}' AND '{end_dt}'\n"
                       f"GROUP BY 1\n"
                       f"HAVING SUM(AMOUNT) <> 0\n"
                       f"ORDER BY 1;"),
             QSqlQuery(f"SELECT CASE TYPE WHEN 'O' THEN 'Депозит'\n"
                       f"                 WHEN 'C' THEN 'Безналичная оплата'\n"
                       f"                 WHEN 'N' THEN 'Наличные'\n"
                       f"       END , COUNT(1)\n"
                       f"FROM V_TRANSACTION\n"
                       f"WHERE H_CLIENT_ID IS NULL\n"
                       f"    AND LOAD_DTTM BETWEEN '{start_dt}' AND '{end_dt}'\n"
                       f"GROUP BY 1\n"
                       f"ORDER BY 1;")]
    return sql_report_to_lists(query[report_type])


def db_loan_sel(ln, fn, mn, start_dt, end_dt):
    model = QSqlQueryModel()
    model.setQuery(f"SELECT L_RECORDING_ID, H_DOCTOR_ID, H_CLIENT_ID, \n"
                   f"    STRFTIME('%d.%m.%Y', START_DTTM) \"Дата приема\", \n"
                   f"    FIO \"ФИО\", PHONE \"Телефон\", TOTAL_TO_PAY_AMT \"Неоплаченная сумма\", "
                   f"    COMMENT \"Комментарий\", STRFTIME('%H:%M', START_DTTM) START_TM, \n"
                   f"    STRFTIME('%H:%M', END_DTTM) END_TM, ADDITIONAL_PHONE, DISCOUNT\n"
                   f"FROM V_RECORDING\n"
                   f"WHERE IS_PAID = 'Нет'\n"
                   f"    AND LAST_NAME LIKE '%{ln}%' AND FIRST_NAME LIKE '%{fn}%' \n"
                   f"    AND MIDDLE_NAME LIKE '%{mn}%'\n"
                   f"    AND DATE(START_DTTM) BETWEEN '{start_dt}' AND '{end_dt}'\n"
                   f"LIMIT 100;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_make_transaction(type_of_trans, amount, comment):
    db_for_idu.execute(f"INSERT INTO V_TRANSACTION (L_RECORDING_ID, H_CLIENT_ID, H_INSURANCE_ID, "
                       f"    TYPE, AMOUNT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES (NULL, NULL, NULL, '{type_of_trans}', {amount}, '{comment}' , '1');")
    db_for_idu.commit()


def db_user_sel():
    model = QSqlQueryModel()
    model.setQuery(f"SELECT NAME \"Логин\", \n"
                   f"    CASE TYPE WHEN 'A' THEN 'Администратор' WHEN 'U' THEN 'Пользователь' END \"Тип\","
                   f"    COMMENT \"Комментарий\"\n"
                   f"FROM D_USER\n"
                   f"ORDER BY 1;")
    sorting_model = QSortFilterProxyModel()
    sorting_model.setSourceModel(model)
    return sorting_model


def db_admin_cnt_sel():
    query = QSqlQuery(f"SELECT COUNT(1)\n"
                      f"FROM D_USER\n"
                      f"WHERE TYPE = 'A';")
    query.first()
    return query.value(0)


def db_user_del(selected_indexes):
    for i in selected_indexes:
        db_for_idu.execute(f"DELETE FROM D_USER\n"
                           f"WHERE NAME = '{i.model().data(i.model().index(i.row(), 0))}';")
    db_for_idu.commit()


def db_user_ins(login, password, user_type, comment):
    db_for_idu.execute(f"INSERT INTO D_USER (NAME, PASSWORD, TYPE, COMMENT)\n"
                       f"VALUES ('{login}', '{password}', '{user_type}', '{comment}');")
    db_for_idu.commit()


def db_user_upd(login, password, user_type, comment):
    db_for_idu.execute(f"UPDATE D_USER\n"
                       f"SET PASSWORD = '{password}', TYPE = '{user_type}', COMMENT = '{comment}'\n"
                       f"WHERE NAME = '{login}';")
    db_for_idu.commit()
