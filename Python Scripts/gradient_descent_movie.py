import csv
from matplotlib import cm
import matplotlib.pyplot as pp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def readData(data):
	a = [[],[]]
	with open(data, 'rb') as file:
		reader = csv.reader(file)
		for row in reader:
			a[0].append(int(row[0].split(' ')[0]))
			a[1].append(float(row[0].split(' ')[1]))
	return a

def cost(a, m, b):
	cost = 0.0
	for i in range(0,len(a)):
		y = a[1][i]
		x = a[0][i]
		cost += np.square(y - (m*x+b))
	return cost
	
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
	
def drawPoint(ax, m, b):
	ax.plot(m, b, cost(a, m, b), 'o')	
		
def main():
	a = readData('movie_data.csv')
	inp = ' '
	i = 0
	
	m = -2.5
	b = -15
	g = 0.00001
	
	fig = pp.figure()
	mrange = np.arange(-4,4.2,.2)
	brange = np.arange(-20,21)
	mrange, brange = np.meshgrid(mrange, brange)
	z = cost(a,mrange,brange)
	hillChart = fig.add_subplot(121, projection='3d')
	hillChart.cla()
	hillChart.plot_surface(mrange,brange,z,alpha=.5, rstride = 3, cstride = 3, cmap=cm.coolwarm)
	hillChart.axis([-4,4,-20,20])
	
	xrange = np.arange(0,11)
	yrange = np.add(np.multiply(m,xrange),b)
	scatChart = fig.add_subplot(122)
	scatChart.cla()
	scatChart.axis([0,10,0,10])
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
		scatChart.plot(xrange, yrange)
		scatChart.plot(a[0],a[1],'o')
		fig.canvas.draw()
		grad = gradCost(a,m,b)
		newM = m - .2*g*grad[0]
		newB = b - g*grad[1]
		m = newM
		b = newB
		if (i % 30 == 29):
			inp = raw_input('')
			hillChart.cla()
			hillChart.plot_surface(mrange,brange,z,alpha=.5, rstride = 3, cstride = 3, cmap=cm.coolwarm)
			hillChart.axis([-4,4,-20,20])
		i += 1	
		print m, b
		

if __name__ == '__main__':
	main()