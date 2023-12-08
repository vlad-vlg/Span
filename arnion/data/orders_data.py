from arnion.db.mysql_connection import my_connection_handler


class OrderDataObject:
    def __init__(self, order_id=0, order_number='', goods_id=0, quantity=1, date_of_order='0000-00-00 00:00:00'):
        self.order_id = order_id
        self.order_number = order_number
        self.goods_id = goods_id
        self.quantity = quantity
        self.date_of_order = date_of_order

    def get_order_data(self):
        order_data = self.order_number + ' | ' + str(self.goods_id) + ' | ' + str(self.quantity) + ' | ' + str(self.date_of_order)
        return order_data


class OrderRptDataObject(OrderDataObject):
    def __init__(self, order_id=0, order_number='', goods_id=0, quantity=1, date_of_order='0000-00-00 00:00:00', goods_category_id=0,
                 goods_name='', price=0.00, goods_category_name=''):
        super().__init__(order_id, order_number, goods_id, quantity, date_of_order)
        self.goods_category_id = goods_category_id
        self.goods_name = goods_name
        self.price = price
        self.goods_category_name = goods_category_name

    def get_order_data(self):
        order_data = self.order_number + ' | ' + self.goods_name + ' | ' + str(self.quantity) + ' | ' + str(self.date_of_order)
        return order_data

class OrderDataHandler:
    @staticmethod
    def select_list():
        orders = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM orders ORDER BY order_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        orders.append(OrderDataHandler.get_order(row))
            return orders
        except:
            raise

    @staticmethod
    def select_by_id(order_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM orders WHERE order_id=" + str(order_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchone()
                    order = OrderDataHandler.get_order(row)
                    return order
        except:
            raise

    @staticmethod
    def get_order(row):
        return OrderDataObject(row[0], row[1], row[2], row[3], row[4])

    @staticmethod
    def select_list_rpt():
        orders = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT o.*, g.goods_category_id, g.goods_name, g.price, cat.goods_category_name "\
                               "FROM goods g " \
                               "JOIN orders o " \
                               "ON o.goods_id = g.goods_id " \
                                "JOIN goods_categories cat " \
                                "ON cat.goods_category_id = g.goods_category_id "\
                               "ORDER BY goods_category_id, order_number"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        orders.append(OrderDataHandler.get_order_rpt(row))
            return orders
        except:
            raise

    @staticmethod
    def get_order_rpt(row):
        return OrderRptDataObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    @staticmethod
    def delete_by_id(order_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "DELETE FROM orders WHERE order_id=" + str(order_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def update(order: OrderDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "UPDATE orders SET "\
                               "order_number='" + order.order_number + "', "\
                               "goods_id=" + str(order.goods_id) + ", "\
                               "quantity=" + str(order.quantity) + ", "\
                               "date_of_order='" + str(order.date_of_order) + "' "\
                               + "WHERE order_id=" + str(order.order_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def insert(order: OrderDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "INSERT INTO orders (order_number, goods_id, quantity, date_of_order) "\
                                "VALUES ('"\
                               + order.order_number + "', "\
                               + str(order.goods_id) + ", "\
                               + str(order.quantity) + ", '"\
                               + order.date_of_order + "')"
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
                    order.order_id = cursor.lastrowid
        except:
            raise
