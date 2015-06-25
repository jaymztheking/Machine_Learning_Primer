import random
import matplotlib.pyplot as pp
from matplotlib.lines import Line2D
import numpy as np

#Creates 10 randomish data points
def genBoringScat():
	x = []
	y = []
	for i in range(0,10):
		x.append(random.uniform(1,10))
		y.append(x[-1]+random.normalvariate(0,1))
		#if I had to do it over I might instead use scikit-learn's sklearn.datasets.make_regression function
	return [x, y]
	
#Formats individual charts and returns error (sum of squares)
def makeRegChart(ax, a, m, b):
	error = 0
	ax.axis([0,10,0,10])
	ax.set_title('M = '+str(m)+', B = '+str(b))
	ax.plot(a[0],a[1],'o')
	ax.plot(a[0],np.add(np.multiply(m,a[0]),b))
	for n in range(0,len(a[0])):
		line = Line2D([a[0][n],a[0][n]],[a[1][n],np.add(np.multiply(m,a[0][n]),b)])
		ax.add_line(line)
		error += np.square(a[1][n]- np.add(np.multiply(m,a[0][n]),b))
	return 'M = '+str(m)+' and B = '+str(b)+' has a Sum of Squares of '+str(error)

#Creates 4 different regression lines to fit data	
def showRegLines(a):
	error = []
	fig, axarr = pp.subplots(2, 2)
	error.append(makeRegChart(axarr[0,0], a, 0, 5)) 
	error.append(makeRegChart(axarr[0,1], a, .5, 2))
	error.append(makeRegChart(axarr[1,0], a, 2, -5))
	error.append(makeRegChart(axarr[1,1], a, 1, 0))
	fig.canvas.draw()
	fig.show()
	for e in error:
		print e
	raw_input('')

def main():
	a = genBoringScat()
	showRegLines(a)
	
if __name__ == "__main__":
	main()
