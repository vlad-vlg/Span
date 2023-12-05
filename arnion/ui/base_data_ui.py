class ListWindow:
    # Конструктор
    def __init__(self):
        pass

    # Функция заполнения списка
    def init_data_rows(self):
        pass

    # Функция добавления записи
    def add_record(self):
        pass

    # Функция завершения добавления записи
    def add_record_callback(self, added_data_row):
        pass

    # Функция редактирования записи
    def edit_record(self):
        pass

    # Функция завершения редактирования записи
    def edit_record_callback(self, edited_data_row):
        pass

    # Функция удаления записи
    def delete_record(self):
        pass

    # Функция обновления списка
    def refresh_listbox(self, selection: int, value: str):
        pass

    # Функция открытия окна
    def open(self):
        pass

    # Функция закрытия окна
    def close(self):
        pass


class RecordWindow:

    # Конструктор
    def __init__(self):
        pass

    # Функция открытия окна
    def open(self):
        pass

    # Функция сохранения записи и закрытия окна
    def save(self):
        pass

    # Функция закрытия окна без сохранения записи
    def close(self):
        pass

    # Функция сбора информации с полей ввода
    def collect_from_controls(self):
        pass
