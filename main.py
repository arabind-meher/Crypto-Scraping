from os.path import join

from pandas import DataFrame
from mysql.connector import Error

from crypto_scraper import CryptoScraper
from mysql_db import connect_db
from util import check_directory, get_datetime


def save_as_csv(data, file_name, table_heading):
    check_directory('Crypto Data (csv)')

    DataFrame(data, columns=table_heading).to_csv(
        join('Crypto Data (csv)', file_name + '.csv'), index=False)
    print(f'--> CSV created! (Name): {file_name}')


def store_in_mysql(data, table_name):
    database = connect_db()
    cursor = database.cursor()
    # print(cursor)

    CREATE_COMMAND = f'''
    CREATE TABLE `crypto_scraper`.`{table_name}` (
        `Rank` INT NOT NULL,
        `Name` VARCHAR(50) NOT NULL,
        `Price` VARCHAR(20) NOT NULL,
        `24H_Change` VARCHAR(20) NOT NULL,
        `24H_Volume` VARCHAR(20) NOT NULL,
        `Market_Cap` VARCHAR(20) NOT NULL,
        PRIMARY KEY (`Name`)
    );'''

    INSERT_COMMAND = 'INSERT INTO {table} VALUES(%s, %s, %s, %s, %s, %s);'.format(
        table=table_name)

    try:
        cursor.execute(CREATE_COMMAND)
        database.commit()
        print(f'--> Table Created! (Name): {table_name}')

        cursor.executemany(INSERT_COMMAND, data)
        database.commit()
        print(f'--> Table Filled! (Name): {table_name}')
    except Error as e:
        print(e)


if __name__ == '__main__':
    date_time = get_datetime()

    crypto_scraper = CryptoScraper()
    crypto_data, heading = crypto_scraper.get_crypto_data()

    save_as_csv(crypto_data, date_time, heading)

    store_in_mysql(crypto_data, 'crypto' + '_' + date_time)
