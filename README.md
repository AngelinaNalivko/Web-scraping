### Project Documentation: Web Scraping and Data Analysis System for Books

#### Overview:
This project is a web scraping and data analysis system designed to extract, store, and visualize data about books from the website [Books to Scrape](http://books.toscrape.com). The project uses the Scrapy framework to scrape book data, stores the data in a MySQL database, and provides tools to visualize and analyze the data. Key features include:
- Scraping book information from multiple categories.
- Storing data in a structured MySQL database.
- Visualizing data using graphs (e.g., book price distributions and book counts by category).

#### Components:

1. **`book_spider.py`** (Web Scraper)
   - **Purpose**: This file contains the Scrapy spider responsible for scraping book data from the website. It collects information such as book category, title, price, stock status, and image URL.
   - **How it works**:
     - **Start**: The spider begins by accessing the homepage and collecting links to all book categories.
     - **Category Scraping**: For each category, the spider scrapes the books listed and extracts their data.
     - **Pagination**: The spider automatically follows "Next" page links to scrape books across multiple pages within a category.
     - **Output**: The extracted data is saved into a CSV file (`books_data.csv`) and passed to a MySQL pipeline for database insertion.
   - **Usage**: 
     - Run the spider with:
       ```bash
       scrapy runspider book_spider.py
       ```
     - Output data is stored in `books_data.csv` and inserted into the MySQL database.

2. **`create_db.py`** (Database Creation)
   - **Purpose**: This script is used to set up the MySQL database and create the `books` table, which will store the scraped data.
   - **How it works**:
     - Connects to MySQL and creates a database named `books_db` if it doesn't already exist.
     - Creates a `books` table with columns for `category`, `title`, `price`, `image_url`, and `stock`.
   - **Usage**:
     - Run this script before scraping data to set up the database:
       ```bash
       python create_db.py
       ```
     - The database and table will be created with the correct structure.

3. **`pipelines.py`** (Database Pipeline)
   - **Purpose**: This file defines the pipeline that saves scraped data into the MySQL database.
   - **How it works**:
     - When the spider processes each book item, the pipeline inserts the item into the `books` table of the `books_db` database.
     - It uses the MySQL `pymysql` library to execute SQL `INSERT` commands.
   - **Usage**:
     - Ensure the pipeline is enabled in Scrapy's settings (`settings.py`):
       ```python
       ITEM_PIPELINES = {
           'myproject.pipelines.MySQLPipeline': 300,
       }
       ```
     - Data will be automatically saved in the MySQL database when the spider runs.

4. **`graph.py`** (Book Price Distribution Visualization)
   - **Purpose**: This script generates a histogram to visualize the distribution of book prices.
   - **How it works**:
     - Reads the scraped data from the `books_data.csv` file.
     - Uses `matplotlib` to plot a histogram showing how book prices are distributed across different price ranges.
   - **Usage**:
     - Ensure that `books_data.csv` exists (created by `book_spider.py`).
     - Run the script to generate and display the histogram:
       ```bash
       python graph.py
       ```
     - The histogram shows the number of books in different price bins.

5. **`category_graph.py`** (Books per Category Visualization)
   - **Purpose**: This script creates a bar chart that shows the number of books in each category.
   - **How it works**:
     - Connects to the MySQL `books_db` database to retrieve the categories of all books.
     - Uses `pandas` and `matplotlib` to generate a bar chart where the x-axis represents the categories and the y-axis represents the number of books in each category.
   - **Usage**:
     - Ensure that the MySQL database has been populated by the spider.
     - Run the script to generate and display the bar chart:
       ```bash
       python category_graph.py
       ```
     - The bar chart will show how many books belong to each category.

---

#### Workflow:

1. **Set Up the Database**:
   - Run `create_db.py` to create the MySQL database and table for storing book data.

2. **Scrape Book Data**:
   - Run `book_spider.py` to scrape book data from [Books to Scrape](http://books.toscrape.com). The spider will store data in both the `books_data.csv` file and the MySQL database.

3. **Visualize the Data**:
   - Use `graph.py` to generate a histogram of book prices.
   - Use `category_graph.py` to create a bar chart showing the number of books in each category.

---

#### System Requirements:

- **Python 3.x**
- **MySQL Server** (with `pymysql` to connect to it)
- Python Libraries:
  - `Scrapy`: For web scraping.
  - `pymysql`: For connecting to the MySQL database.
  - `pandas`: For data manipulation.
  - `matplotlib`: For data visualization.

---

This documentation outlines the functionality of each component in the project. The project provides a complete pipeline from data extraction, storage, and analysis to visualization, making it a comprehensive system for scraping and analyzing book data.
