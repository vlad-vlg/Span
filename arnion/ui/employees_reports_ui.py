import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
import os
from arnion.data.employees_data import EmployeeDataHandler


class EmployeesReportWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('500x450')
        self.window.title('Отчет: Сотрудники')

        # Добавление метки заголовка
        lbl_title = tk.Label(self.window, text='Список сотрудников',
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
                                   bd=3,
                                   relief='raised',
                                   overrelief='groove',
                                   command=self.close
                                   )
        self.btn_close.place(x=190, y=400, width=90, height=30)

    def get_report_text(self):
        report_text = ' ' * 17 + 'Сотрудники по отделам' + os.linesep
        report_text += '-' * 55 + os.linesep
        data_rows = EmployeeDataHandler.select_list_rpt()
        current_department_name = '#-#-#'
        for data_row in data_rows:
            # Если новый отдел, добавляется заголовок группы
            if data_row.department_name != current_department_name:
                report_text += data_row.department_name + os.linesep
                current_department_name = data_row.department_name
            # Добавляется запись
            report_text += '\t' + data_row.get_full_name() + os.linesep
        return report_text

    def open(self):
        # Перевод фокуса на созданное окно
        self.window.focus_force()
        # Перевод всех команд на созданное окно
        self.window.grab_set()

    def close(self):
        self.window.destroy()
