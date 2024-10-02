import pymysql

def create_database_and_table():

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root' 
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS books_db;")
            cursor.execute("USE books_db;")

            create_table_query = """
            CREATE TABLE IF NOT EXISTS books (
                category VARCHAR(255),
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                price FLOAT,
                image_url TEXT,
                stock VARCHAR(255)
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Database is successfully created.")
    finally:
        connection.close()

if __name__ == '__main__':
    create_database_and_table()
