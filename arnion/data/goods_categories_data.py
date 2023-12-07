from arnion.db.mysql_connection import my_connection_handler


class Goods_categoryDataObject:
    def __init__(self, goods_category_id=0, goods_category_name=''):
        self.goods_category_id = goods_category_id
        self.goods_category_name = goods_category_name


class Goods_categoryDataHandler:
    @staticmethod
    def select_list():
        goods_categories = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM goods_categories ORDER BY goods_category_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        goods_categories.append(Goods_categoryDataObject(row[0], row[1]))
            return goods_categories
        except:
            raise

    @staticmethod
    def select_by_id(goods_category_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM goods_categories WHERE goods_category_id=" + str(goods_category_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchone()
                    department = Goods_categoryDataHandler.get_goods_category(row)
                    return department
        except:
            raise

    @staticmethod
    def get_goods_category(row):
        return Goods_categoryDataObject(row[0], row[1])

    @staticmethod
    def delete_by_id(goods_category_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "DELETE FROM goods_categories WHERE goods_category_id=" + str(goods_category_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def update(goods_category: Goods_categoryDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "UPDATE goods_categories SET goods_category_name='"\
                               + goods_category.goods_category_name + "' "\
                               + "WHERE goods_category_id=" + str(goods_category.goods_category_id)
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
        except:
            raise

    @staticmethod
    def insert(goods_category: Goods_categoryDataObject):
        try:
            with my_connection_handler.get_connection() as cnn:
                insert_query = "INSERT INTO goods_categories (goods_category_name) VALUES ('"\
                               + goods_category.goods_category_name + "')"
                with cnn.cursor() as cursor:
                    cursor.execute(insert_query)
                    goods_category.goods_category_id = cursor.lastrowid
        except:
            raise
