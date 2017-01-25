import random
f = open('data.txt', 'r')
Information = []
for line in f:
    Information.append([str((line.strip())).split('\t')])


def ReturnAll():
	return Data
def ReturnRandom():
	return random.choice(Data)
def ReturnRandomPass():
	return random.choice(Data)[1]
def ReturnRandomUser():
	return random.choice(Data)[0]
def ReturnLine(number):
	return Datas[0:0 + int(number)]
