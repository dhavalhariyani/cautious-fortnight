import random
with open('file.txt','r') as source:
	data = [ (random.random(), line) for line in source ]
data.sort()
with open('file.txt','w') as target:
	for _, line in data:
		target.write(line)