import twitter as twit
import json
import shutil

def search(twitter, search_type, search_term):
	# only returns a max of 100 tweets, anyways
    return twitter.GetSearch(term=search_term, result_type=search_type, return_json=True, count=1000)

if __name__ == '__main__':
	# API auth
	consumer_key = 'no05DWDZL4xuR2a4WylRsQXQM'
	consumer_secret = 'P2k16EheiyCo4RqDqqN7r5SmSuTIj6dLVkEXY0iukWpNabX1U7'
	token = '198209455-M7eQGuYoaNdLmCx3wIf6WFpg2cpqSNIPdvTOrckt'
	token_secret = 'Y5cWHdCIHV43Qw1joMZOlXJBUFsBZOEdUa1SJqT773apV'

	twitter = twit.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token_key=token, access_token_secret=token_secret)
	# t = twit.Twitter(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token_key=token, access_token_secret=token_secret)

	'''
	print(t.VerifyCredentials())

	print(list(map(lambda x: x['user']['followers_count'], search(t, 'storj')['statuses'])))
	print(list(map(lambda x: x['user']['followers_count'], search(t, 'STORJ')['statuses'])))
	
	print(search(t, 'storj')[90].user.followers_count)
	'''

	terms = ['ETH','XRP','BCH','LTC','EOS','ADA','NEO','XLM','BCD','VEN','IOT','XMR','TRX','DASH','XEM','ETC','QTUM','BNB','LSK','MAID','SC','STORJ']
	types = ['mixed', 'popular', 'recent']
	file_names = ['ETH','XRP','BCH','LTC','EOS','ADA','NEO','XLM','BCD','VEN','IOT','XMR','TRX','DASH','XEM','ETC','QTUM','BNB','LSK','MAID','SC','STORJ']		
	for name in zip(terms, file_names):
		for tp in types:
			data = search(twitter, tp, name[0])
			try:
				shutil.copyfile(name[1] + '_' + tp + '.json', name[1] + '_' + tp + '_BACKUP.json')
				with open(name[1] + '_' + tp +'.json', 'r', newline='') as f:
					f_data = json.load(f)
					# get the list of tweet ids already in the JSON
					id_list = list(map(lambda x: x["id_str"], f_data['statuses']))
					# create a list of tweets whose ids aren't already in the JSON
					new_data = list(filter(lambda x: not x['id_str'] in id_list, data['statuses']))

					f_data['statuses'].extend(new_data)
				
				with open(name[1] + '_' + tp + '.json', 'w') as f:
					json.dump(f_data, f)
					print('Dumped %d lines of data to file'%len(f_data['statuses']))

			except Exception as e:
				print('Did not read from file.  Does it exist?', e)

				with open(name[1] + '_' + tp + '.json', 'w') as f:
					json.dump(data, f)
					print('Dumped %d lines of data to file'%len(data['statuses']))
