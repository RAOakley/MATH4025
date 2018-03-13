import cryptocompare as cc
import requests
import datetime as dt
import csv
from itertools import compress
import tqdm

# pulls the last 5.5 days (by default) of minute-by-minute price data in terms of BTC (by default)
# the final data-point will be time-stamped to the closest minute of the request-time
# each data point is 1 minute, and request rate is capped to:
#	8000/hour, 300/minute, 15/second
def min_pull(coin_name, curr='BTC', data_len=8000):
	url_hist_price_min = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}'.format(coin_name, curr, data_len)
	# hist_data = cc.query_cryptocompare(url_hist_price_min)
	# copied pasted from the cryptocompare GIT; the wrapper above doesn't work for some reason
	try:
		hist_data = requests.get(url_hist_price_min).json()
	except Exception as e:
		print('Error getting coin information. %s' % str(e))
		return 
	if (hist_data.get('Response') == 'Error'):
		print('[ERROR] %s' % hist_data.get('Message'))
		return 

	formatted = [list(map(lambda x: x['time'], hist_data['Data'])), list(map(lambda x: x['open'], hist_data['Data'])),
				 list(map(lambda x: x['volumefrom'], hist_data['Data'])), list(map(lambda x: x['volumeto'], hist_data['Data']))]
	
	return formatted 

#BTC: MAY 2013 - PRESENT
#SIA: OCT 2015 - PRESENT
#STORJ: JUL 2 2017 - PRESENT
#MAIDSAFE: MAY 2014 - PRESENT

# date should be the start date for data collection
# start_index is where the time-stamp t should 
# coin_name should be the 3 letter coin name in the crypto database
#	   e.g. bitcoin is BTC
def pull(date, coin_name, start_index):
	data = [[],[]]
	t = 0
	day_list = [date]
	while(start_index < date):
		data[0].append(t)
		data[1].append(0)
		t += 1
		start_index += dt.timedelta(days=1)

	while(date < dt.datetime.today()):
		day_list.append(date)
		date += dt.timedelta(days=1)

	# made a little for loop to replace the original while loop b/c I like progress bars
	for day in tqdm.tqdm(day_list):
		crypto = cc.get_historical_price(coin_name, 'USD', timestamp=day)
		data[0].append(t)
		data[1].append(crypto[coin_name]['USD'])
		t += 1

	return zip(data[0],data[1])


if __name__ == '__main__':
	'''
	btc_date = dt.datetime(2013, 5, 30)
	sia_date = dt.datetime(2015, 10, 31)
	storj_date = dt.datetime(2017, 7, 2)
	ms_date = dt.datetime(2014, 5, 30)

	#dates = [btc_date, sia_date, storj_date, ms_date]
	dates = [sia_date, storj_date, ms_date]
	#names = ['BTC', 'SC', 'STORJ', 'MAID']
	names = ['SC', 'STORJ', 'MAID']
	start_index = btc_date

	[btc_date <= i for i in dates]

	# Change above iterables to change which coins' data are pulled down
	# column 1 of the csv file is the time (where the first date is normalized to 0)
	# column 2 is the price that corresponds with the date/time in the first column 
	for (date, name) in zip(dates, names):
		f = open(name + '.csv', 'w', newline='')
		csv.writer(f).writerows(pull(date, name, start_index))
		f.close()
	'''


	names = ['SC', 'STORJ', 'MAID']
	for name in names:
		data = min_pull(name)
		try:
			with open(name + '.csv', 'r', newline='') as f:
				i = 0
				reader = csv.reader(f)
				last_time = []
				for row in reader:
					if i == 0:
						truth_list = list(map(lambda x: not str(x) in list(row), data[0]))
					data[i] = list(compress(data[i], truth_list))
					data[i].extend(row)
					i += 1
					
		except Exception as e:
			print('Did not read from file.  Does it exist?', e)

		with open(name + '.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(data)
			print('Wrote ' + str(len(data[0])) + ' lines of data to file \'' + name + '.csv\' \n')
