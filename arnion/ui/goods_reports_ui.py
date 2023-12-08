import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
import os
from arnion.data.goods_data import GoodsxDataHandler


class GoodsReportWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('500x435+730+400')
        self.window.title('Отчет: Товары')
        self.window.resizable(False, False)

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window, text='Список товаров',
                             font=('Helvetica', 16, 'bold'),
                             fg='#0000cc',
                             justify='center'
                             )
        lbl_title.place(x=25, y=15, width=450, height=50)

        # Добавление окна вывода текста
        self.txt_output = st(self.window, font=('Courier New', 10, 'bold'))
        self.txt_output.insert(tk.END, self.get_report_text())
        self.txt_output.place(x=15, y=75, width=470, height=300)

        # Добавление кнопки закрытия окна
        self.btn_close = tk.Button(self.window, text='Закрыть',
                                   font=('Helvetica', 10, 'bold'),
                                   bg='#ccffcc',
                                   bd=2,
                                   relief='raised',
                                   overrelief='ridge',
                                   activebackground='#345',
                                   activeforeground='white',
                                   command=self.close
                                   )
        self.btn_close.place(x=190, y=390, width=90, height=30)

    def get_report_text(self):
        report_text = ' ' * 24 + 'Товары' + os.linesep
        report_text += '-' * 55 + os.linesep
        data_rows = GoodsxDataHandler.select_list()
        for data_row in data_rows:
            report_text += data_row.goods_name + os.linesep
        return report_text

    def open(self):
        # Перевод фокуса на созданное окно
        self.window.focus_force()
        # Перевод всех команд на созданное окно
        self.window.grab_set()

    def close(self):
        self.window.destroy()
