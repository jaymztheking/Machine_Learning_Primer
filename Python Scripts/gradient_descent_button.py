import matplotlib.pyplot as plt
import numpy as np

def f(a):
	return (a-5)*(a-5)

def slope(a):
	return (2*a)-10
	
def intercept(a, m):
	return m*a - f(a)
	
x = np.arange(0,11)
g = .1
a = 7


fig = plt.figure()
chrt = fig.gca()
chrt.axis([0,10,0,30])
fig.show()
chrt.plot(x,f(x))
fig.canvas.draw()
i = raw_input(' ')
while i != 'q':
	#Plot point
	chrt.plot(a,f(a),'o')
	fig.canvas.draw()
	i = raw_input(' ')
	
	#Display gradient line
	m = slope(a)
	b = intercept(a, m)
	chrt.plot(x, (m*x)-b)
	fig.canvas.draw()
	i = raw_input(' ')
	
	newA = a - (g*m)
	print 'A is now: ', newA
	#Display new A on Equation Line
	chrt.plot(newA, f(newA), '^')
	fig.canvas.draw()
	i = raw_input(' ')
	
	#Set A to New A and reset
	chrt.cla()
	a = newA
	chrt.axis([0,10,0,30])
	chrt.plot(x,f(x))
	
