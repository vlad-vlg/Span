import tkinter as tk
from arnion.db.mysql_connection import ConnectionHandler
from arnion.data.departments_data import DepartmentDataHandler
from arnion.data.employees_data import EmployeeDataHandler
from arnion.data.goods_data import GoodsDataHandler
from arnion.data.orders_data import OrderDataHandler
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_reports_ui import EmployeesReportWindow
from arnion.ui.goodts_reports_ui import GoodsReportWindow
from arnion.ui.orders_reports_ui import OrdersReportWindow


class MainWindow:
    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('330x430')
        self.window.title('SPAN')
        self.window.resizable(False, False)

        # Добавление метки заголовка
        lbl_title = tk.Label(text='SPAN',
                             font=('Helvetica', 16, 'bold'),
                             fg='#0000cc',
                             justify='center'
                             )
        lbl_title.place(x=25, y=15, width=250, height=30)

        # Добавление метки заголовка данных
        lbl_title1 = tk.Label(text='Данные',
                              font=('Helvetica', 12, 'bold'),
                              fg='#0066ff',
                              justify='center'
                              )
        lbl_title1.place(x=25, y=40, width=120, height=50)

        # Добавление кнопки данных "Отделы"
        btn_data1 = tk.Button(self.window, text='Отделы',
                              font=('Helvetica', 10, 'bold'),
                              bg='#ccffcc',
                              bd=3,
                              relief='raised',
                              overrelief='groove'
                              )
        btn_data1.place(x=25, y=90, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_data2 = tk.Button(self.window, text='Сотрудники',
                              font=('Helvetica', 10, 'bold'),
                              bg='#ccffcc',
                              bd=3,
                              relief='raised',
                              overrelief='groove'
                              )
        btn_data2.place(x=25, y=150, width=120, height=50)

        # Добавление кнопки данных "Товары"
        btn_data3 = tk.Button(self.window, text='Товары',
                              font=('Helvetica', 10, 'bold'),
                              bg='#ccffcc',
                              bd=3,
                              relief='raised',
                              overrelief='groove'
                              )
        btn_data3.place(x=25, y=210, width=120, height=50)

        # Добавление кнопки данных "Заказы"
        btn_data4 = tk.Button(self.window, text='Заказы',
                              font=('Helvetica', 10, 'bold'),
                              bg='#ccffcc',
                              bd=3,
                              relief='raised',
                              overrelief='groove'
                              )
        btn_data4.place(x=25, y=270, width=120, height=50)

        # Добавление метки заголовка отчетов
        lbl_title2 = tk.Label(text='Отчеты',
                              font=('Helvetica', 12, 'bold'),
                              fg='#0066ff',
                              justify='center'
                              )
        lbl_title2.place(x=170, y=40, width=120, height=50)

        # Добавление кнопки отчетов "Отделы"
        btn_report1 = tk.Button(self.window, text='Отделы',
                                font=('Helvetica', 10, 'bold'),
                                bg='#ccffcc',
                                bd=3,
                                relief='raised',
                                overrelief='groove',
                                command=self.do_report_departments
                                )
        btn_report1.place(x=170, y=90, width=120, height=50)

        # Добавление кнопки отчетов "Сотрудники"
        btn_report2 = tk.Button(self.window, text='Сотрудники',
                                font=('Helvetica', 10, 'bold'),
                                bg='#ccffcc',
                                bd=3,
                                relief='raised',
                                overrelief='groove',
                                command=self.do_report_employees
                                )
        btn_report2.place(x=170, y=150, width=120, height=50)

        # Добавление кнопки отчетов "Товары"
        btn_report3 = tk.Button(self.window, text='Товары',
                                font=('Helvetica', 10, 'bold'),
                                bg='#ccffcc',
                                bd=3,
                                relief='raised',
                                overrelief='groove',
                                command=self.do_report_goods
                                )
        btn_report3.place(x=170, y=210, width=120, height=50)

        # Добавление кнопки отчетов "Заказы"
        btn_report4 = tk.Button(self.window, text='Заказы',
                                font=('Helvetica', 10, 'bold'),
                                bg='#ccffcc',
                                bd=3,
                                relief='raised',
                                overrelief='groove',
                                command=self.do_report_orders
                                )
        btn_report4.place(x=170, y=270, width=120, height=50)

        # Добавление кнопки "Тест"
        btn_test = tk.Button(self.window, text='Тест',
                             font=('Helvetica', 10, 'bold'),
                             bg='#ffffcc',
                             bd=3,
                             relief='raised',
                             overrelief='groove',
                             command=self.do_test
                             )
        btn_test.place(x=25, y=360, width=120, height=40)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text='Выход',
                              font=('Helvetica', 10, 'bold'),
                              bg='#ccffcc',
                              bd=3,
                              relief='raised',
                              overrelief='groove',
                              command=self.close
                              )
        btn_close.place(x=170, y=360, width=120, height=40)

    # Функция "Тест"
    def do_test(self):
        ch = ConnectionHandler()
        ch.do_test()
        print('-' * 30)
        departments = DepartmentDataHandler.select_list()
        for department in departments:
            print(department.department_name)
        print('-' * 30)
        employees = EmployeeDataHandler.select_list()
        for employee in employees:
            print(employee.get_full_name())
        print('-' * 30)
        goods = GoodsDataHandler.select_list()
        for good in goods:
            print(good.get_goods_price())
        print('-' * 30)
        orders = OrderDataHandler.select_list()
        print("Код товара", "Количество", "Дата заказа", sep='\t' * 2)
        for order in orders:
            print(order.goods_id, order.quantity, order.date_of_order, sep='\t' * 4)

    # Открытие отчета "Отделы"
    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    # Открытие отчета "Сотрудники"
    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

    # Открытие отчета "Товары"
    def do_report_goods(self):
        rpt = GoodsReportWindow()
        rpt.open()

    # Открытие отчета "Заказы"
    def do_report_orders(self):
        rpt = OrdersReportWindow()
        rpt.open()

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()
