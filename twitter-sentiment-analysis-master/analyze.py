from pprint import pprint
import predict
import json
import csv

BASE_DIR = "../twitter_data/"
NAMES = ['ETH','XRP','BCH','LTC','EOS','ADA','NEO','XLM','BCD','VEN','IOT','XMR','TRX','DASH','XEM','ETC','QTUM','BNB','LSK','MAID','SC','STORJ']
TYPES = ['mixed', 'popular', 'recent']

def main():
	pred = predict.predictor()

	for name in NAMES: 
		for tp in TYPES:
			# shutil.copyfile(name + '_' + tp + '.json', name + '_' + tp + '_BACKUP.json')
			with open(BASE_DIR + name + '_' + tp +'.json', 'r', newline='') as f:
				f_data = json.load(f)

				# create a list of the sentiments of each tweet (in order) 
				sentiment_list = pred.infer(tweets = list(map(lambda x: x['text'], f_data['statuses'])))

				# normalizes the sentiment so that -1 is the most negative and 1 is the most positive
				sentiment_list = list(map(lambda x: (2.0 * x[1]) - 1, sentiment_list))
				
				# add a sentiment field to each tweet and set it to be the normalized value of the sentiment
				for (status, sentiment) in zip(f_data['statuses'], sentiment_list):
					status['sentiment'] = sentiment

			
			with open(BASE_DIR + name + '_' + tp + '.json', 'w') as f:
				json.dump(f_data, f)
				print('Dumped %d lines of data to file'%len(f_data['statuses']))


if __name__ == "__main__":
	main()
