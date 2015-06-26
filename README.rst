=======================
Machine Learning Primer
=======================

Description
------------

This repository contains files to supplement the presentation I am giving for the Data Science Colorado Meetup group on July 1st, 2015 at Galvanize Platte.

You can find the presentation slides in this repo or with this link `A Primer on Machine Learning <https://docs.google.com/presentation/d/1rFoSPMGrWEwU8U-Ej49B6mqv8ikyAzIfVj0ryqZPVNA/edit?usp=sharing>`_

Package Versions used for Python Scripts
----------------------------------
* Python 2.7.9
* NumPy 1.9.2
* Matplotlib 1.4.3

I haven't checked compatibility with other versions.  I strongly recommend downloading the `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ stack.  It will provide you with everything required to run the scripts in this repo.

Summary of Scripts
------------------

display_linefit_graphic.py
	This is a Python script that displays 4 regression line plots to compare how well a line will fit the data based upon the m and b variables

gradient_descent_button.py
	This is a Python script that shows gradient descent algorithm applied against the plot of f(x) = (x - 5)^2.
		
gradient_descent_movie.py
	This is a Python script that displays a 3D graph of the linear regression cost function with respect to parameters m and b and also a scatter plot graph with regression line.  Both graphs are based upon the data found in movie_data.csv  The script steps through the algorithm and plots new 3D points on the left graph and new regression lines on the right graph.
	
scikit_gradient_descent.py
	This Python script is a scikit-learn implentation of stochastic gradient descent that reads the data from movie_data.csv, fits the data to a S.G.D. regressor, and outputs a scatter plot and regression line.
