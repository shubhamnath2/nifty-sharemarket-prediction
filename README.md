# nifty-sharemarket-prediction
Using regression (polynomial), find expected market value on some input date.

Description of data:
Data consists of 5 columns i.e. date, open, high, low, close for 10 years(2007-2017). With respect to date, the share value of Nifty is provided. 

Model Working:
Data is read and 2 columns were taken as Y=f(x) where Y is 'close' and x is 'date', means on this date nifty market value is closed and the scatter plot graph is also made. Using polynomial regression, the model is trained and accuracy score is also provided. Trend line is also plotted in the scatter graph, giving overall closing value for 10 years.

Script:
The script 'nifty_data.py' is the main model. Data is read using pandas and converted into array using numpy as polynomial regression inputs takes 2d array (for e.g.- [[5,10,15],[10,20,30]]->[[10],[20]]). 3 degree polynomial is taken. Then 'x' is transformed into polymorised x (say x_poly) & fitted in the regression w.r.t Y. Linear regression with x_poly and Y is fitted. Fron x_poly, predicted Y is also calculated. Then accuracy is scored followed by trend plotting. The model is now trained, and date is provided as an user input. With input date, expected closing value shows.

The script 'remain.py' is used as reference with information of other columns and their respective plotting code.

Warning:
The accuracy score is not perfect, therefore predicted closing value may come false. But the objective of implementing this model is to understand the implementation of Machine Learning Model in real life, with good algorithm to apply with reduced error. Happy Learning!!

Configuration:
You need virtualenv, PyCharm or any other Python IDE to run this model, as this model requires virtualenv to use. PyCharm is prefered with Python3.6 with all the required modules/libraries in venv folder.

References:
https://towardsdatascience.com/introduction-to-linear-regression-and-polynomial-regression-f8adc96f31cb
https://towardsdatascience.com/polynomial-regression-bbe8b9d97491


