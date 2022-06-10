# Crypto Scraping

In this project, we are going to scrape [crypto.com](https://crypto.com) site to get top 500 performing cryptocurrency and store all data into CSV file with time stamp as file name.
- Site: https://crypto.com/price

## Package Required
### [Requests](https://requests.readthedocs.io/en/latest/)
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.
### [Pandas](https://pandas.pydata.org/)
In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license.
### [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.
### [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the Python Database API Specification v2.0 (PEP 249).

## [CSV Files](https://github.com/arabind-meher/Crypto-Scraping/tree/master/Crypto%20Data)

## Code Blocks

### Web Scraping
```python
import requests
from bs4 import BeautifulSoup

url = 'https://crypto.com/price'
response = requests.get(url)
text = response.text
soup = BeautifulSoup(text, 'html.parser')
```

### MySQL Connection
```python
import mysql.connector

database = mysql.connector.connect(
    host='<host>',
    user='<user>',
    password='<password>',
    database='<database>'
)
```

### SQL Commands
```sql
CREATE TABLE `crypto_scraper`.`{table_name}` (
    `Rank` INT NOT NULL,
    `Name` VARCHAR(50) NOT NULL,
    `Price` VARCHAR(20) NOT NULL,
    `24H_Change` VARCHAR(20) NOT NULL,
    `24H_Volume` VARCHAR(20) NOT NULL,
    `Market_Cap` VARCHAR(20) NOT NULL,
    PRIMARY KEY (`Name`)
);'''
```
