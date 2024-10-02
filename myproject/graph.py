import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('books_data.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=10, color='blue', edgecolor='black')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(True)

plt.show()
