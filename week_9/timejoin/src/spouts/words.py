from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout

class WordSpout(Spout):

    animals = ['dog', 'cat', 'zebra', 'elephant']

    def initialize(self, stormconf, context):
        self.words = itertools.cycle(self.animals)
        self.time = 0

    def classify(self, word):
        return self.animals.index(word)

    def next_tuple(self):
        word = next(self.words)
        self.time = self.time + 1
        self.emit([self.time, word])



class DataSpout(Spout):

    signal_feed = [{"score":3}, {"score":5}, {"score":7}, {"score":11}]

    def initialize(self, stormconf, context):
        self.signals = itertools.cycle(self.signal_feed)
        self.time = 0

    def next_tuple(self):
        signal = next(self.signals)
        self.time = self.time + 1
        # Update index (there should be a nicer way).
        self.emit([self.time, signal["score"]])
