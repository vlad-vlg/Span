import copy
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

from arnion.data.goods_categories_data import Goods_categoryDataHandler
from arnion.data.goods_data import GoodsxDataHandler, GoodsxDataObject


class GoodsWindow:
    # Конструктор
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('500x435')
        self.window.title('Товары')
        self.window.resizable(False, False)

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window,
                             text='Список товаров',
                             font=('Helvetica', 16, 'bold'),
                             fg='#0000cc',
                             justify='center'
                             )
        lbl_title.place(x=25, y=15, width=450, height=50)

        # Контейнер для списка и полосы прокрутки
        self.frame = tk.Frame(self.window)
        self.frame.place(x=15, y=75, width=470, height=300)
        # Добавление списка записей
        self.lbox_data_rows = tk.Listbox(self.frame,
                                         bd=2,
                                         selectmode='single',
                                         activestyle='none',
                                         font=('Courier New', 10, 'bold')
                                         )
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.config(command=self.lbox_data_rows.yview)
        self.scrollbar.place(x=450, y=0, width=20, height=300)
        self.lbox_data_rows.config(yscrollcommand=self.scrollbar.set)
        self.lbox_data_rows.place(x=0, y=0, width=450, height=300)

        self.init_data_rows()

        # Добавление кнопки "Добавить"
        self.btn_add = tk.Button(self.window,
                                 text='Добавить',
                                 font=('Helvetica', 10, 'bold'),
                                 bg='#ccffff',
                                 bd=2,
                                 relief='raised',
                                 overrelief='ridge',
                                 activebackground='#345',
                                 activeforeground='white',
                                 command=self.add_record
                                 )
        self.btn_add.place(x=20, y=390, width=90, height=30)

        # Добавление кнопки "Изменить"
        self.btn_edit = tk.Button(self.window,
                                  text='Изменить',
                                  font=('Helvetica', 10, 'bold'),
                                  bg='#ccffff',
                                  bd=2,
                                  relief='raised',
                                  overrelief='ridge',
                                  activebackground='#345',
                                  activeforeground='white',
                                  command=self.edit_record
                                  )
        self.btn_edit.place(x=120, y=390, width=90, height=30)

        # Добавление кнопки "Удалить"
        self.btn_delete = tk.Button(self.window,
                                    text='Удалить',
                                    font=('Helvetica', 10, 'bold'),
                                    bg='#ccffff',
                                    bd=2,
                                    relief='raised',
                                    overrelief='ridge',
                                    activebackground='#345',
                                    activeforeground='white',
                                    command=self.delete_record
                                    )
        self.btn_delete.place(x=220, y=390, width=90, height=30)

        # Добавление кнопки закрытия окна
        self.btn_close = tk.Button(self.window,
                                   text='Закрыть',
                                   font=('Helvetica', 10, 'bold'),
                                   bg='#ccffcc',
                                   bd=2,
                                   relief='raised',
                                   overrelief='ridge',
                                   activebackground='#345',
                                   activeforeground='white',
                                   command=self.close
                                   )
        self.btn_close.place(x=390, y=390, width=90, height=30)

    # Функция заполнения списка
    def init_data_rows(self):
        self.data_rows = GoodsxDataHandler.select_list()
        for data_rows in self.data_rows:
            self.lbox_data_rows.insert('end', data_rows.goods_name)
        if len(self.data_rows) > 0:
            self.lbox_data_rows.select_set(0)

    # Функция добавления записи
    def add_record(self):
        self.data_row = GoodsxDataObject()
        self.record_window = GoodsxWindow(True, self.data_row, self)
        self.record_window.open()

    # Функция завершения добавления записи
    def add_record_callback(self, added_data_row: GoodsxDataObject):
        GoodsxDataHandler.insert(added_data_row)
        self.data_rows.append(added_data_row)
        self.lbox_data_rows.insert('end', added_data_row.goods_name)
        self.lbox_data_rows.selection_clear(0, 'end')
        self.lbox_data_rows.selection_set('end')

    # Функция редактирования записи
    def edit_record(self):
        self.selection = self.lbox_data_rows.curselection()[0]
        self.data_row = copy.deepcopy(self.data_rows[self.selection])
        self.record_window = GoodsxWindow(False, self.data_row, self)
        self.record_window.open()

    # Функция завершения редактирования записи
    def edit_record_callback(self, edited_data_row: GoodsxDataObject):
        GoodsxDataHandler.update(edited_data_row)
        self.data_rows[self.selection] = edited_data_row
        self.refresh_listbox(self.selection, edited_data_row.goods_name)

    # Функция удаления записи
    def delete_record(self):
        answer = mb.askokcancel(parent=self.window, title='Подтверждение',
                                message='Вы действительно хотите удалить запись?')
        if not answer:
            return
        self.selection = self.lbox_data_rows.curselection()[0]
        id = self.data_rows[self.selection].goods_id
        GoodsxDataHandler.delete_by_id(id)
        self.data_rows.pop(self.selection)
        self.lbox_data_rows.delete(self.selection)

    # Функция обновления списка
    def refresh_listbox(self, selection: int, value: str):
        self.lbox_data_rows.delete(selection, selection)
        self.lbox_data_rows.insert(selection, value)
        self.lbox_data_rows.select_set(selection)

    # Функция открытия окна
    def open(self):
        # Перевод фокуса на созданное окно
        self.window.focus_force()
        # Перевод всех команд на созданное окно
        self.window.grab_set()

    # Функция закрытия окна
    def close(self):
        self.window.destroy()


class GoodsxWindow:
    # Конструктор
    def __init__(self, add_new: bool, data_row: GoodsxDataObject, parent: GoodsWindow):

        if add_new:
            title_text = 'Новый товар'
        else:
            title_text = 'Редактирование товара'

        self.add_new = add_new
        self.data_row = data_row
        self.parent = parent

        self.window = tk.Toplevel()
        self.window.geometry('560x250')
        self.window.title(title_text)
        self.window.resizable(False, False)

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window,
                             text=title_text,
                             font=('Helvetica', 16, 'bold'),
                             fg='#0000cc',
                             justify='center'
                             )
        lbl_title.place(x=60, y=15, width=450, height=50)

        # Добавление полей ввода
        lbl_name = tk.Label(self.window,
                            text='Наименование товара:',
                            font=('Helvetica', 10, 'bold')
                            )
        lbl_name.place(x=15, y=85)
        self.ent_name = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_name.place(x=175, y=85, width=370, height=25)
        self.ent_name.insert(tk.END, data_row.goods_name)

        lbl_price = tk.Label(self.window,
                             text='Цена:',
                             font=('Helvetica', 10, 'bold')
                             )
        lbl_price.place(x=15, y=155)
        self.ent_price = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_price.place(x=175, y=155, width=370, height=25)
        self.ent_price.insert(tk.END, data_row.price)

        lbl_goods_category = tk.Label(self.window,
                                      text='Категория товара:',
                                      font=('Helvetica', 10, 'bold')
                                      )
        lbl_goods_category.place(x=15, y=120)
        self.cbo_goods_category = ttk.Combobox(self.window, font=('Helvetica', 10, 'bold'))
        self.init_combobox()
        # Запрет на ввод произвольных значений
        self.cbo_goods_category['state'] = 'readonly'
        self.set_id_to_combobox(data_row.goods_category_id)
        self.cbo_goods_category.place(x=175, y=120, width=370, height=25)

        # Добавление кнопки "Сохранить"
        self.btn_ok = tk.Button(self.window,
                                text='Сохранить',
                                font=('Helvetica', 10, 'bold'),
                                bg='#ccffcc',
                                bd=2,
                                relief='raised',
                                overrelief='ridge',
                                activebackground='#345',
                                activeforeground='white',
                                command=self.save
                                )
        self.btn_ok.place(x=170, y=200, width=90, height=30)

        # Добавление кнопки "Отмена"
        self.btn_cancel = tk.Button(self.window,
                                    text='Отмена',
                                    font=('Helvetica', 10, 'bold'),
                                    bg='#ffffee',
                                    bd=2,
                                    relief='raised',
                                    overrelief='ridge',
                                    activebackground='#345',
                                    activeforeground='white',
                                    command=self.close
                                    )
        self.btn_cancel.place(x=280, y=200, width=90, height=30)

    # Функция заполнения выпадающего списка
    def init_combobox(self):
        self.cbox_ids = []
        self.cbox_values = []
        data_rows = Goods_categoryDataHandler.select_list()
        for data_row in data_rows:
            self.cbox_ids.append(data_row.goods_category_id)
            self.cbox_values.append(data_row.goods_category_name)
        self.cbo_goods_category['values'] = self.cbox_values

    # Функция применения id к выпадающему списку
    def set_id_to_combobox(self, id):
        try:
            id_index = self.cbox_ids.index(int(id))
            self.cbo_goods_category.set(self.cbox_values[id_index])
        except ValueError as e:
            self.cbo_goods_category.set('')

    # Функция считывания id из выпадающего списка
    def get_id_from_combobox(self, value: str) -> int:
        try:
            id_index = self.cbox_values.index(value)
            return self.cbox_ids[id_index]
        except ValueError as e:
            return 0

    # Функция открытия окна
    def open(self):
        # Перевод фокуса на созданное окно
        self.window.focus_force()
        # Перевод всех команд на созданное окно
        self.window.grab_set()

    # Функция сохранения записи и закрытия окна
    def save(self):
        self.collect_from_controls()
        if self.add_new:
            self.parent.add_record_callback(self.data_row)
        else:
            self.parent.edit_record_callback(self.data_row)
        self.close()

    # Функция закрытия окна
    def close(self):
        self.window.destroy()

    # Функция сбора информации с полей ввода
    def collect_from_controls(self):
        self.data_row.goods_name = str(self.ent_name.get())
        self.data_row.price = str(self.ent_price.get())
        self.data_row.goods_category_id = str(self.get_id_from_combobox(self.cbo_goods_category.get()))
