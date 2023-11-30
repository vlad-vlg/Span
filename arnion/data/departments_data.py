from arnion.db.mysql_connection import my_connection_handler


class DepartmentDataObject:
    def __init__(self, department_id=0, department_name=''):
        self.department_id = department_id
        self.department_name = department_name


class DepartmentDataHandler:
    @staticmethod
    def select_list():
        departments = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM departments ORDER BY department_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        departments.append(DepartmentDataObject(row[0], row[1]))
            return departments
        except:
            raise

    @staticmethod
    def select_by_id(department_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM departments WHERE department_id=" + str(department_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchone()
                    department = DepartmentDataHandler.get_department(row)
                    return department
        except:
            raise

    @staticmethod
    def get_department(row):
        return DepartmentDataObject(row[0], row[1])

    @staticmethod
    def delete_by_id(department_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "DELETE FROM departments WHERE department_id=" + str(department_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def update(department: DepartmentDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "UPDATE departments SET department_name='"\
                               + department.department_name + "' "\
                               + "WHERE department_id=" + str(department.department_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def insert(department: DepartmentDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "INSERT INTO departments (department_name) VALUES ('"\
                               + department.department_name + "')"
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
                    department.department_id = cursor.lastrowid
        except:
            raise
