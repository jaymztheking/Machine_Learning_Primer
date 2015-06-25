import csv
from matplotlib import cm
import matplotlib.pyplot as pp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Imports data from CSV and returns 2 arrays: x array and y array respectively
def readData(data):
	a = [[],[]]
	with open(data, 'rb') as file:
		reader = csv.reader(file)
		for row in reader:
			a[0].append(int(row[0].split(' ')[0]))
			a[1].append(float(row[0].split(' ')[1]))
	return a

#Returns cost of function at point m, b	
def cost(a, m, b):
	cost = 0.0
	for i in range(0,len(a)):
		y = a[1][i]
		x = a[0][i]
		cost += np.square(y - (m*x+b))
	return cost

#Returns gradient of cost function in an array with m first, then b
def gradCost(a, m, b):
	gradM = 0.0
	gradB = 0.0
	N = len(a[0])
	for i in range(0,N):
		y = a[1][i]
		x = a[0][i]
		gradM += -x*(y-(m*x+b))
		gradB += -1*(y-(m*x+b))
	return [2*N*gradM, 2*N*gradB]
	
def main():
	#loop related variables and data initialization
	a = readData('movie_data.csv')
	inp = ' '
	i = 0
	
	#initial variables
	m = -2.5
	b = -15
	g = 0.00001 #cheated and chose a good one for convergence
	
	#drawing the initial 3d cost function chart
	fig = pp.figure()
	mrange = np.arange(-4,4.2,.2)
	brange = np.arange(-20,21)
	mrange, brange = np.meshgrid(mrange, brange)
	z = cost(a,mrange,brange)
	hillChart = fig.add_subplot(121, projection='3d')
	hillChart.cla() #workaround for "gridline transparency issue"
	hillChart.plot_surface(mrange,brange,z,alpha=.5, rstride = 3, cstride = 3, cmap=cm.coolwarm)
	hillChart.axis([-4,4,-20,20])
	hillChart.set_xlabel('m')
	hillChart.set_ylabel('b')
	hillChart.set_zlabel('Cost')
	hillChart.set_title('Cost Function for m, b')
	
	#drawing the initial scatter plot of movie rating data
	xrange = np.arange(0,11)
	yrange = np.add(np.multiply(m,xrange),b)
	scatChart = fig.add_subplot(122)
	scatChart.cla() #workaround for "gridline transparency issue"
	scatChart.axis([0,10,0,10])
	scatChart.set_xlabel('Number of Explosions in Film')
	scatChart.set_ylabel('James\' Rating of Film')
	scatChart.set_title('Rating Based on Number of Explosions')
	scatChart.plot(xrange,yrange)
	scatChart.plot(a[0],a[1],'o')
	fig.show()
	raw_input('')
	while i < 1000:
		z1 = cost(a,m,b)
		yrange = np.add(np.multiply(m,xrange),b)
		hillChart.plot([m],[b],[z1], "s", markeredgecolor = "r", markerfacecolor = "r")
		scatChart.cla()
		scatChart.axis([0,10,0,10])
		scatChart.set_xlabel('Number of Explosions in Film')
		scatChart.set_ylabel('James\' Rating of Film')
		scatChart.set_title('Rating Based on Number of Explosions')
		scatChart.plot(xrange, yrange)
		scatChart.plot(a[0],a[1],'o')
		fig.canvas.draw()
		grad = gradCost(a,m,b)
		newM = m - .2*g*grad[0]
		newB = b - g*grad[1]
		m = newM
		b = newB
		if (i % 50 == 49): #used for 'pauses' to examine charts and to prevent too many points from being plotted
			inp = raw_input('')
			hillChart.cla()
			hillChart.plot_surface(mrange,brange,z,alpha=.5, rstride = 3, cstride = 3, cmap=cm.coolwarm)
			hillChart.axis([-4,4,-20,20])
			hillChart.set_xlabel('m')
			hillChart.set_ylabel('b')
			hillChart.set_zlabel('Cost')
			hillChart.set_title('Cost Function for m, b')
		i += 1	
		print m, b
		

if __name__ == '__main__':
	main()