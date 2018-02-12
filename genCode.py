import random

def genCode():
	codes = []
	s = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for i in range(4):
		seg = []
		for j in range(4):
			seg.append(s[random.randint(0, len(s) - 1)])
		codes.append(''.join(seg))
	return '-'.join(codes)

for i in range(2):
	print (genCode())
