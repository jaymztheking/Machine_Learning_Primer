import matplotlib.pyplot as pp
import numpy as np

#Function I chose to graph, (x-5)^2
def f(a):
	return np.square(a-5)

#First derivative of above function for finding slope of gradient line
def slope(a):
	return (2*a)-10
	
#Used to find y-intercept in creating gradient line	
def intercept(a, m):
	return m*a - f(a)

def main():	
	x = np.arange(0,11) #numbers 1- 10
	g = 0.1 #learning rate
	a = 8 #initial position

	#Initialize Graph
	fig = pp.figure()
	chrt = fig.gca()
	chrt.axis([0,10,0,30])
	fig.show()

	#Plot our function
	chrt.plot(x,f(x))
	fig.canvas.draw()
	i = raw_input(' ')
	while i != 'q':
		#Plot point A
		chrt.plot(a,f(a),'o')
		fig.canvas.draw()
		i = raw_input(' ')
		
		#Display gradient line at point A
		m = slope(a)
		b = intercept(a, m)
		chrt.plot(x, (m*x)-b)
		fig.canvas.draw()
		i = raw_input(' ')
		
		#Use gradient descent algorithm to get new point
		newA = a - (g*m)
		print 'A is now: ', newA
		
		#Display new point A on Equation Line
		chrt.plot(newA, f(newA), '^')
		fig.canvas.draw()
		i = raw_input(' ')
		
		#Set A to New A and reset
		chrt.cla()
		a = newA
		chrt.axis([0,10,0,30])
		chrt.plot(x,f(x))
	
if __name__ == '__main__':
	main()
