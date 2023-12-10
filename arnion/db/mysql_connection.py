from mysql.connector import connect, connection, Error
import json


class ConnectionHandler:
    def __init__(self):
        self.read_from_config()

    def read_from_config(self):
        with open("config.json", "r") as f:
            data = json.load(f)
        self.host = data["host"]
        self.database = data["database"]
        self.user = data["user"]
        self.password = data["password"]

    def do_test(self):
        with connect(host=self.host, database=self.database, user=self.user, password=self.password) as cnn:
            select_query = "SELECT * FROM departments ORDER BY department_id"
            with cnn.cursor() as cursor:
                cursor.execute(select_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

    def check_connection(self) -> bool:
        try:
            with self.get_connection() as cnn:
                select_query = "SELECT 1"
                with cnn.cursor() as crs:
                    crs.execute(select_query)
                    crs.fetchall()
            return True
        except Error as e:
            return False

    def get_connection(self) -> connection:
        return connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            autocommit=True
        )


my_connection_handler = ConnectionHandler()
