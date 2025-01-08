from PySide2.QtWidgets import QMessageBox


def show_error(text, yes_button=None, no_button=None):
    error = QMessageBox(QMessageBox.Critical, 'Ошибка', text)
    if yes_button is not None:
        error.addButton(QMessageBox.Yes)
        error.button(QMessageBox.Yes).setText(yes_button)
    if no_button is not None:
        error.addButton(QMessageBox.No)
        error.button(QMessageBox.No).setText(no_button)
    response = error.exec()
    if response == QMessageBox.Yes:
        return 'yes'
    elif response == QMessageBox.No:
        return 'no'


def show_confirmation(action):
    question = QMessageBox(QMessageBox.Question, 'Требуется подтверждение', 'Вы уверены, что хотите ' + action + '?',
                           QMessageBox.No | QMessageBox.Yes)
    question.button(QMessageBox.Yes).setText('Да')
    question.button(QMessageBox.No).setText('Нет')
    response = question.exec()
    if response == QMessageBox.Yes:
        return 'yes'
    elif response == QMessageBox.No:
        return 'no'


def show_question(question, action1, action2):
    question = QMessageBox(QMessageBox.Question, 'Выберите действие', question,
                           QMessageBox.No | QMessageBox.Yes)
    question.button(QMessageBox.Yes).setText(action1)
    question.button(QMessageBox.No).setText(action2)
    response = question.exec()
    if response == QMessageBox.Yes:
        return 1
    elif response == QMessageBox.No:
        return 2


def show_info(text):
    info = QMessageBox(QMessageBox.Information, 'Инфо', text, QMessageBox.Ok)
    info.exec()


def show_warning(text):
    question = QMessageBox(QMessageBox.Warning, 'Внимание', text, QMessageBox.Cancel | QMessageBox.Ok)
    question.button(QMessageBox.Cancel).setText('Отмена')
    question.button(QMessageBox.Ok).setText('Ок')
    response = question.exec()
    if response == QMessageBox.Ok:
        return 'ok'
    elif response == QMessageBox.Cancel:
        return 'cancel'
