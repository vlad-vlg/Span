from  arnion.db.mysql_connection import my_connection_handler


class EmployeeDataObject:
    def __init__(self, employee_id=0, first_name='', middle_name='', last_name='', department_id=0):
        self.employee_id = employee_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.department_id = department_id

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        return full_name


class EmployeeDataHandler:
    @staticmethod
    def select_list():
        employees = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM employees ORDER BY employee_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        employees.append(EmployeeDataHandler.get_employee(row))
            return employees
        except:
            raise

    @staticmethod
    def select_by_id(employee_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM employees WHERE employee_id=" + str(employee_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchall()
                    employee = EmployeeDataHandler.get_employee(row)
                    return employee
        except:
            raise

    @staticmethod
    def get_employee(row):
        return EmployeeDataObject(row[0], row[1], row[2], row[3], row[4])
