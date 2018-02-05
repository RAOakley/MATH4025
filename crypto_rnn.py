import tensorflow as tf
import tqdm
import numpy as np


class trainer:
    def __init__(self):
        self.graph = tf.graph()
        self.graph.as_default()

    def train(rate=.0001, batch_size=100, features=1):
        self.input = tf.placeholder(shape=[batch_size, features])
        self.optimizer = tf.train.AdamOptimizer(training_rate=rate)
        
        lstm = tf.contrib.rnn.BasicLSTMCell(1)

