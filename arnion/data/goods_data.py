from arnion.db.mysql_connection import my_connection_handler


class GoodsDataObject:
    def __init__(self, goods_id=0, goods_category_id=0, goods_name='', price=0.00):
        self.goods_id = goods_id
        self.goods_category_id = goods_category_id
        self.goods_name = goods_name
        self.price = price

    def get_goods_price(self):
        goods_price = self.goods_name + '\t' + str(self.price)
        return goods_price


class GoodsDataHandler:
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
                        goods.append(GoodsDataHandler.get_goods(row))
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
                    goods = GoodsDataHandler.get_goods(row)
                    return goods
        except:
            raise

    @staticmethod
    def get_goods(row):
        return GoodsDataObject(row[0], row[1], row[2], row[3])

    @staticmethod
    def delete_by_id(goods_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "DELETE FROM goods WHERE goods_id=" + str(goods_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def update(goods_x: GoodsDataObject):
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
    def insert(goods_x: GoodsDataObject):
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
