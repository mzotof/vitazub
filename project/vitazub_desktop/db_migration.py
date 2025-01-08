from sqlite3 import connect
import re
import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Manager\dbNewVer.mdb;')
cursor = conn.cursor()
cursor.execute('select name, phone, dec, remark from customrs')


def db_name():
    config_file = open('config.cfg', 'r')
    for line in config_file:
        if line[0:2] == 'DB':
            config_file.close()
            return line[5:-1]


db_for_idu = connect(db_name())


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


for row in cursor.fetchall():
    if row[0] in ('-', None):
        continue
    name = row[0].split(' ')
    name[0] = name[0].capitalize()
    if len(name) > 1:
        name[1] = name[1].capitalize()
    else:
        name.append('')
    if len(name) > 2:
        name[2] = name[2].capitalize()
        for i in range(3, len(name)):
            name[2] += ' ' + name[i]
    else:
        name.append('')
    if row[1] is None:
        phone = ['', '']
    else:
        phone = re.split('; |, |,|;', row[1])
        phone[0] = clean_phone(phone[0])
        if len(phone) > 1:
            phone[1] = clean_phone(phone[1])
        else:
            phone.append('')
    if row[2] is None:
        discount = 0
    else:
        discount = int(row[2])
    if row[3] is None:
        comment = ''
    else:
        comment = row[3]
    # print([name[0], name[1], name[2], phone[0], phone[1], discount, comment])
    db_for_idu.execute(f"INSERT INTO V_CLIENT (LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE, \n"
                       f"ADDITIONAL_PHONE, DISCOUNT, BIRTH_DT, COMMENT, SOURCE_SYSTEM_CD)\n"
                       f"VALUES ('{name[0]}', '{name[1]}', '{name[2]}', '{phone[0]}', '{phone[1]}', \n"
                       f"{discount}, date('1900-01-01'), '{comment}', '1');")
    db_for_idu.commit()
