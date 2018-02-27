import twitter as twit
import csv
import tqdm

def search(twitter, search_terms):
    # not sure which will work, as it is unclear how the twitter package deals with listed queries
    twitter.search.tweets(q=search_terms.join("%20"))
    twitter.search.tweets(q=search_terms)
