import cryptocompare as cc
import datetime as dt
import pickle
import csv
import tqdm

#BTC: MAY 2013 - PRESENT
#SIA: OCT 2015 - PRESENT
#STORJ: JUL 2 2017 - PRESENT
#MAIDSAFE: MAY 2014 - PRESENT

#date should be the start date for data collection
#start_index is where the time-stamp t should 
#coin_name should be the 3 letter coin name in the crypto database
#   e.g. bitcoin is BTC
def pull(date, coin_name, start_index):
    data = [[],[]]
    t = 0
    day_list = [date]
    while(start_index < date):
        data[0].append(t)
        data[1].append(0)
        t += 1
        date += dt.timedelta(days=1)

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
    btc_date = dt.datetime(2013, 5, 30)
    sia_date = dt.datetime(2015, 10, 31)
    storj_date = dt.datetime(2017, 7, 2)
    ms_date = dt.datetime(2014, 5, 30)

    dates = [btc_date, sia_date, storj_date, ms_date]
    names = ['BTC', 'SC', 'STORJ', 'MAID']
    start_index = btc_date

    print([btc_date <= i for i in dates])

    # Change above iterables to change which coins' data are pulled down
    # column 1 of the csv file is the time (where the first date is normalized to 0)
    # column 2 is the price that corresponds with the date/time in the first column 
    for (date, name) in zip(dates, names):
        f = open(name + '.csv', 'w', newline='')
        csv.writer(f).writerows(pull(date, name, start_index))
        f.close()
