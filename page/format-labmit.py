#!/usr/bin/env python

import json, os, sys, re
from collections import defaultdict

data = []

for line in sys.stdin:
	if not re.match('^[ ]*(#.*)?$', line):
		word, rank, avg, stdev, twitter_rank, google_rank, nyt_rank, lyrics_rank = line.split()
		#luckily, the words are already sorted by avg
		data.append(word)

print(json.dumps(data))

