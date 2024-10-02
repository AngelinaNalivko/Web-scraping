import matplotlib.pyplot as plt
import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root', 
    db='books_db'
)

query = "SELECT category FROM books"
df = pd.read_sql(query, connection)

connection.close()

category_counts = df['category'].value_counts()

plt.figure(figsize=(12, 8))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Books by Category')
plt.xlabel('Category')
plt.ylabel('Number of Books')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
