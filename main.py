from os import mkdir
from os.path import isdir, join
from datetime import datetime

import requests
from pandas import DataFrame
from bs4 import BeautifulSoup


class Crypto:
	def __init__(self):		
		self.crypto_data = list()

		for i in range(1, 11):
			url = f'https://crypto.com/price?page={i}'
			print('Extracting:', url)
			self.get_table_data(url)

		if not isdir('Crypto Data'):
			mkdir('Crypto Data')

		DataFrame(self.crypto_data, columns=self.get_table_heading()).to_csv(
			join('Crypto Data', str(datetime.now())+'.csv'), index=False)

	def get_table_heading(self, url='https://crypto.com/price'):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		table = soup.find('table')

		heading = list()
		thead = table.find('thead').find('tr').find_all('th')[1:7]
		for th in thead:
			heading.append(th.text)

		return heading

	def get_table_data(self, url):
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		table = soup.find('table')

		tbody = table.find('tbody').find_all('tr')
		for tr in tbody:
			tds = tr.find_all('td')[1:7]

			self.crypto_data.append((
				tds[0].text,
				tds[1].find('span').text,
				tds[2].find('div').text,
				tds[3].text,
				tds[4].text,
				tds[5].text,))


if __name__ == '__main__':
	Crypto()
