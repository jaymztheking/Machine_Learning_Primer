import csv
import sklearn.linear_model as sk
import numpy as np

def readData(data):
	a = [[],[]]
	with open(data, 'rb') as file:
		reader = csv.reader(file)
		for row in reader:
			a[0].append(int(row[0].split(' ')[0]))
			a[1].append(float(row[0].split(' ')[1]))
	return a

def matrixify(a):
	matrix = []
	for i in a:
		matrix.append([i])
	return matrix
	
def main():
	a = readData('movie_data.csv')
	#Each x value needs to be in an array/matrix
	x = matrixify(a[0])
	y = np.array()
	reg = sk.SGDRegressor(loss="squared_loss", penalty="none")
	print x
	reg.fit(x,y)
	print reg.predict([10])
	print reg.predict([0])
	# scaX = []
	# scatX = matrixify(np.arange(0,11))
	# for i in scatX:
		# scaX.append([i])
	# scatY = reg.predict(scatX)
	# print x
	# print y
	# print scatX
	# print scatY

if __name__ == '__main__':
	main()