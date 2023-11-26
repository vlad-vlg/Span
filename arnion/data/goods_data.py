from arnion.db.mysql_connection import my_connection_handler


class GoodsDataObject:
    def __init__(self, goods_id=0, goods_category_id=0, goods='', price=0.00):
        self.goods_id = goods_id
        self.goods_category_id = goods_category_id
        self.goods = goods
        self.price = price

    def get_goods_price(self):
        goods_price = self.goods + '    ' + str(self.price)
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
                    row = cursor.fetchall()
                    goods = GoodsDataHandler.get_goods(row)
                    return goods
        except:
            raise

    @staticmethod
    def get_goods(row):
        return GoodsDataObject(row[0], row[1], row[2], row[3])
