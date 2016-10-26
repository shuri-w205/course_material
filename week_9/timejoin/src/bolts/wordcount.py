from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt


class DataCruncher(Bolt):


    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.packets = {}


    def process_data_fragment(self, time, word_or_data):
      # TODO
      # put word and data together by time in packets.
      # if we have a complete data + word set
      # do something with both (I don’t really care what).
      # and remove it from packets
      pass

    def process(self, tup):
        time = tup.values[0]
        word_or_data = tup.values[1]
        self.process_data_fragment(time, word_or_data)
