import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import datetime as dt

df=pd.read_excel('/home/shubham/Desktop/Nifty/Nifty_updated_June_19.xls')
df['Date_Id'] = pd.to_datetime(df['Date']).apply(lambda date: date.toordinal())
print(df)

x=df['Date']
x_new=df['Date_Id']
y4=df['Close']

#scatter plot
plt.figure(figsize=(60, 30), dpi=20)
plt.scatter(x,y4,s=17,color='black')
plt.suptitle('Closing Figure- Date v/s close figure',fontsize=72)
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
plt.xlabel('Date',fontsize=72)
plt.ylabel('Close',fontsize=72)
plt.savefig('/home/shubham/Desktop/Nifty/Date_vs_close.png')

#data reshaping
x_new=x_new.values.reshape(-1,1)
y4=y4.values.reshape(-1,1)

#polynomial regression
poly=PolynomialFeatures(degree=3)
x_poly=poly.fit_transform(x_new)
poly.fit(x_poly,y4)

clf=linear_model.LinearRegression()
clf.fit(x_poly,y4)

y_pred=clf.predict(x_poly)

#comparing with linear model
lin=linear_model.LinearRegression()
lin.fit(x_new,y4)

#accuracy score
print('Mean Absoulute Error %s' % metrics.mean_absolute_error(y4, y_pred))
print('Root Mean Squared Error %s' % np.sqrt(metrics.mean_squared_error(y4, y_pred)))
print("Differences in variability: %s "%round(metrics.r2_score(y4,y_pred)*100,3))

#plotting
plt.figure(figsize=(60, 30), dpi=20)
plt.scatter(x,y4,s=17,color='black')
plt.plot(x_new,lin.predict(x_new),'-r', color='red', linewidth=7, markersize=3)
plt.plot(x,y_pred,'-r', color='green', linewidth=7, markersize=3)
plt.suptitle('Closing Figure- Date v/s close figure',fontsize=72)
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
plt.xlabel('Date',fontsize=72)
plt.ylabel('Close',fontsize=72)
plt.savefig('/home/shubham/Desktop/Nifty/Date_vs_close_after_regression.png')

while True:
    try:
        date_value=input("Enter the Date in dd-mm-yyyy format:")
        date_value=dt.datetime.strptime(date_value,'%d-%m-%Y')
        ordinal_date_value=date_value.toordinal()
        inp=poly.fit_transform([[ordinal_date_value]])

    except:
        print("Wrong date format must be dd-mm-yyyy Format.")
        continue
    else:
        pass

    opt=clf.predict(inp)
    print("Expected Closing Value on %s is %s"%(date_value,opt[0][0]))
    print("\n")