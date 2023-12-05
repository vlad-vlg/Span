from arnion.db.mysql_connection import my_connection_handler


class GoodsxDataObject:
    def __init__(self, goods_id=0, goods_category_id=0, goods_name='', price=0.00):
        self.goods_id = goods_id
        self.goods_category_id = goods_category_id
        self.goods_name = goods_name
        self.price = price

    def get_goods_price(self):
        goods_price = self.goods_name + '\t' + str(self.price)
        return goods_price


class GoodsxDataHandler:
    @staticmethod
    def select_list():
        goods = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM goods ORDER BY goods_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        goods.append(GoodsxDataHandler.get_goods(row))
            return goods
        except:
            raise

    @staticmethod
    def select_by_id(goods_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM goods WHERE goods_id=" + str(goods_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchone()
                    goods = GoodsxDataHandler.get_goods(row)
                    return goods
        except:
            raise

    @staticmethod
    def get_goods(row):
        return GoodsxDataObject(row[0], row[1], row[2], row[3])

    @staticmethod
    def delete_by_id(goods_id):
        try:
            with my_connection_handler.get_connection() as cnn:
                delete_query = "DELETE FROM goods WHERE goods_id=" + str(goods_id)
                with cnn.cursor() as cursor:
                    cursor.execute(delete_query)
        except:
            raise

    @staticmethod
    def update(goods_x):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "UPDATE goods SET "\
                               "goods_category_id=" + str(goods_x.goods_category_id) + ", "\
                               "goods_name='" + goods_x.goods_name + "', "\
                               "price=" + str(goods_x.price) + " "\
                               + "WHERE goods_id=" + str(goods_x.goods_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def insert(goods_x: GoodsxDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "INSERT INTO goods (goods_category_id, goods_name, price) VALUES ("\
                               + str(goods_x.goods_category_id) + ", '"\
                               + goods_x.goods_name + "', "\
                               + str(goods_x.price) + ")"
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
                    goods_x.goods_id = cursor.lastrowid
        except:
            raise
