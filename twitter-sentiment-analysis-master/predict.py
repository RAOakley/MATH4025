from __future__ import print_function
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from pprint import pprint
import csv
import sys
import os

MAX_SEQUENCE_LENGTH = 1000
MAX_NB_WORDS = 20000
BASE_DIR = "../twitter-sentiment-analysis-master/"
TRAIN_DATA_FILE = BASE_DIR + "Sentiment Analysis Dataset.csv"

def main():
	inpts = []
	argvs = sys.argv.copy()
	argvs.pop(0)

	for arg in argvs:
		inpts.append(arg)

	pred = predictor()
	
	return predictor.infer(tweets=inpts)


class predictor(object):
	def __init__(self):
		self.tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
		self.load_tokenizer_data()

		self.model = load_model(BASE_DIR + 'model.h5')
		self.model.load_weights(BASE_DIR + 'weights.h5')


	def infer(self, tweets=[]):
		os.environ['CUDA_VISIBLE_DEVICES'] = '1'  # str(random.randint(0, 15))

		'''
		X_raw = []
		for line in sys.stdin:
			X_raw.append(line)
		'''

		X_raw = tweets

		X, word_index = self.tokenize_data(X_raw)

		# Note that each tweet is a 2-tuple: [%-chance negative, %-chance positive]
		predictions = self.model.predict(x=X, batch_size=128, verbose=1)

		'''	
		for index, txt in enumerate(X_raw):
			is_positive = predictions[index][1] >= 0.5
			status_txt = "Positive" if is_positive else "Negative"
			print("[",status_txt,"] ", txt)
		'''

		return predictions


	def load_tokenizer_data(self):
		X = []
		
		with open(TRAIN_DATA_FILE, "r", newline='', encoding='utf8') as f:
			reader = csv.reader(f)
			for line in reader:
				text = line[3]
				X.append(text)

		self.tokenizer.fit_on_texts(X)

		return


	def tokenize_data(self, X_raw):
		sequences = self.tokenizer.texts_to_sequences(X_raw)
		word_index = self.tokenizer.word_index
		X_processed = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

		return X_processed, word_index


if __name__ == "__main__":
	main()
	# sys.stdout.write(main())
