import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
import os
from arnion.data.orders_data import OrderDataHandler


class OrdersReportWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('500x450')
        self.window.title('Отчет: Заказы')
        self.window.resizable(False, False)

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window, text='Список заказов',
                             font=('Helvetica', 16, 'bold'),
                             fg='#0000cc',
                             justify='center'
                             )
        lbl_title.place(x=25, y=15, width=450, height=50)

        # Добавление окна вывода текста
        self.txt_output = st(self.window, font=('Courier New', 10, 'bold'))
        self.txt_output.insert(tk.END, self.get_report_text())
        self.txt_output.place(x=15, y=75, width=470, height=310)

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
        self.btn_close.place(x=190, y=400, width=90, height=30)

    def get_report_text(self):
        report_text = ' ' * 15 + 'Заказы по категориям' + os.linesep * 2
        report_text += 'Код' + '\t' + 'Наименование' + '\t' * 4 + 'Количество' + '\t' + 'Сумма' + os.linesep
        report_text += 'категории' + '\t' + 'товара' + os.linesep
        report_text += '-' * 55 + os.linesep
        data_rows = OrderDataHandler.select_list_rpt()
        current_goods_category_id = '#-#-#'
        for data_row in data_rows:
            # Если новая категория товара, добавляется заголовок группы
            if data_row.goods_category_id != current_goods_category_id:
                report_text += str(data_row.goods_category_id) + os.linesep
                current_goods_category_id = data_row.goods_category_id
            # Добавляется запись
            report_text += '\t' + str(data_row.goods_id) + '\t' * 4 + str(data_row.goods_name) + '\t' + str(data_row.quantity * data_row.goods_name) + os.linesep
        return report_text

    def open(self):
        # Перевод фокуса на созданное окно
        self.window.focus_force()
        # Перевод всех команд на созданное окно
        self.window.grab_set()

    def close(self):
        self.window.destroy()
