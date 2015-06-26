import csv
import sklearn.linear_model as sk
import numpy as np
import matplotlib.pyplot as pp

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
		matrix.append([i, 1]) #i is x1, 1 is x0
	return matrix
	
def dematrixify(a):
	array = []
	for i in a:
		array.append(i[0])
	return array
	
def main():
	a = readData('movie_data.csv')
	x = matrixify(a[0]) #SGDRegressor needs independent variables in an individual array/matrix
	y = a[1] #Output doesn't have to be in individual arrays
	reg = sk.SGDRegressor(loss='squared_loss', penalty='none', n_iter=1000, fit_intercept=False)
	reg.fit(x,y)
	
	#Make Scatter Plot with scikit's "answers"
	xaxis = matrixify(np.arange(0,11))
	yaxis = reg.predict(xaxis)
	xaxis = dematrixify(xaxis)

	fig = pp.figure()
	ax = fig.gca()
	ax.axis([0,10,0,10])
	ax.set_xlabel('Number of Explosions in Film')
	ax.set_ylabel('James\' Rating of Film')
	ax.set_title('Scikit Found M = '+str(reg.coef_[0])+'and B = '+str(reg.coef_[1]))
	ax.plot(a[0],a[1],'o')
	ax.plot(xaxis, yaxis)
	fig.show()
	raw_input(' ')
	
	

if __name__ == '__main__':
	main()