import twitter as twit
import json

def search(twitter, search_term):
    return twitter.GetSearch(term=search_term,result_type="mixed", return_json=True, count=1000)

if __name__ == '__main__':
	consumer_key = 'no05DWDZL4xuR2a4WylRsQXQM'
	consumer_secret = 'P2k16EheiyCo4RqDqqN7r5SmSuTIj6dLVkEXY0iukWpNabX1U7'
	token = '198209455-M7eQGuYoaNdLmCx3wIf6WFpg2cpqSNIPdvTOrckt'
	token_secret = 'Y5cWHdCIHV43Qw1joMZOlXJBUFsBZOEdUa1SJqT773apV'
	t = twit.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token_key=token, access_token_secret=token_secret)
	# t = twit.Twitter(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token_key=token, access_token_secret=token_secret)

	'''
	print(t.VerifyCredentials())

	print(list(map(lambda x: x['user']['followers_count'], search(t, 'storj')['statuses'])))
	print(list(map(lambda x: x['user']['followers_count'], search(t, 'STORJ')['statuses'])))
	
	print(search(t, 'storj')[90].user.followers_count)
	'''

	names = ['storj', 'maidsafe']
	for name in names:
		with open(name + '.json', 'w') as f:
			json.dump(search(t, name), f)

