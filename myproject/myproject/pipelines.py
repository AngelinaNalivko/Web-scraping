import pymysql

class MySQLPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host='localhost',
            user='root', 
            password='root',  
            db='books_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        print("Processing item:", item)
        
        sql = """
        INSERT INTO books (category, title, price, stock, image_url)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (
            item.get('category'),  
            item.get('title'),     
            item.get('price'),   
            item.get('stock'),     
            item.get('image')     
        ))
        self.connection.commit()
        return item
