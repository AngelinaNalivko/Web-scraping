### Web Scraping and Database Manipulation

course: Big Data BPINFOR-82 

Angelina Naliuka 024712312B

Sofiia Parkhomets 024712322C

#### Overview:
This project is a web scraping and data analysis system designed to extract, store, and visualize data about books from the website [Books to Scrape](http://books.toscrape.com). The project uses the Scrapy framework to scrape book data, stores the data in a MySQL database, and provides tools to visualize and analyze the data. Key features include:
- Scraping book information from multiple categories.
- Storing data in a structured MySQL database.
- Visualizing data using graphs.
  
#### Files:

1. **`book_spider.py`** (Web Scraper)
   - This file contains the Scrapy spider responsible for scraping book data from the website. It collects information such as book category, title, price, stock status, and image URL.
   - **How it works**:
     - **Start**: The spider begins by accessing the homepage and collecting links to all book categories.
     - **Category Scraping**: For each category, the spider scrapes the books listed and extracts their data.
     - **Pagination**: The spider automatically follows "Next" page links to scrape books across multiple pages within a category.
     - **Output**: The extracted data is saved into a CSV file (`books_data.csv`) and passed to a MySQL pipeline for database insertion.
   - **Usage**: 
     - Run the spider with:
       ```bash
       scrapy crawl book_spider.py
       ```
       or:
       ```bash
       python -m scrapy crawl book_spider.py
       ```

2. **`create_db.py`** (Database Creation)
   - This script is used to set up the MySQL database and create the `books` table, which will store the scraped data.
   - **How it works**:
     - Connects to MySQL and creates a database named `books_db` if it doesn't already exist.
     - Creates a `books` table with columns for `category`, `title`, `price`, `image_url`, and `stock`.
   - **Usage**:
     - Don't forget to change host, user and password to your own.
     - Run this script before scraping data to set up the database:
       ```bash
       python create_db.py
       ```

3. **`pipelines.py`**
   - This file defines the pipeline that saves scraped data into the MySQL database.
   - **How it works**:
     - When the spider processes each book item, the pipeline inserts the item into the `books` table of the `books_db` database.
     - It uses the MySQL `pymysql` library to execute SQL `INSERT` commands.
   - **Usage**:
     - Don't forget to change host, user and password to your own.
     - Ensure the pipeline is enabled in Scrapy's settings (`settings.py`):
       ```python
       ITEM_PIPELINES = {
           'myproject.pipelines.MySQLPipeline': 300,
       }
       ```

4. **`graph.py`** (Book Price Distribution Visualization)
   - This script generates a histogram to visualize the distribution of book prices.
   - **How it works**:
     - Reads the scraped data from the `books_data.csv` file.
     - Uses `matplotlib` to plot a histogram showing how book prices are distributed across different price ranges.
   - **Usage**:
     - Ensure that `books_data.csv` exists (created by `book_spider.py`).
     - Run the script to generate and display the histogram:
       ```bash
       python graph.py
       ```
       How the graph should look like:
       
![изображение](https://github.com/user-attachments/assets/ac270054-8bbe-4128-a410-0f8b276cf297)


5. **`category_graph.py`** (Books per Category Visualization)
   - This script creates a bar chart that shows the number of books in each category.
   - **How it works**:
     - Connects to the MySQL `books_db` database to retrieve the categories of all books.
     - Uses `pandas` and `matplotlib` to generate a bar chart where the x-axis represents the categories and the y-axis represents the number of books in each category.
   - **Usage**:
     - Ensure that the MySQL database has been populated by the spider.
     - Run the script to generate and display the bar chart:
       ```bash
       python category_graph.py
       ```
       How the graph should look like:
       
![изображение](https://github.com/user-attachments/assets/aa08717d-25cc-4c84-8df7-c97063e769b6)

---

#### Database Scheme:
  ```bash
  CREATE DATABASE books_db;
  USE books_db;

CREATE TABLE books (
    category VARCHAR(255),
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price FLOAT,
    image_url TEXT,
    stock VARCHAR(255)
);

  ```

---

#### System Requirements:

- **Python environment**
- **MySQL Server** 
- **Python Libraries:**
  - `Scrapy`: For web scraping.
  - `pymysql`: For connecting to the MySQL database.
  - `pandas`: For data manipulation.
  - `matplotlib`: For data visualization.
