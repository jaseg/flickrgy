#!/usr/bin/env python

import json, os, sys
from collections import defaultdict

data = defaultdict(lambda: [])

for line in sys.stdin:
	*words, rating = line.split()
	data[int(rating)].append(' '.join(words))

print(json.dumps(data))

