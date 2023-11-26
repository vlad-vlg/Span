from arnion.db.mysql_connection import my_connection_handler


class OrderDataObject:
    def __init__(self, order_id=0, goods_id=0, quantity=1, date_of_order='0000-00-00 00:00:00'):
        self.order_id = order_id
        self.goods_id = goods_id
        self.quantity = quantity
        self.date_of_order = date_of_order


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
                    row = cursor.fetchall()
                    order = OrderDataHandler.get_order(row)
                    return order
        except:
            raise

    @staticmethod
    def get_order(row):
        return OrderDataObject(row[0], row[1], row[2], row[3])
