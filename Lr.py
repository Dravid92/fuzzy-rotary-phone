import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# import data from for training and testing
dtrain = pd.read_csv('train.csv')
dtest = pd.read_csv('test.csv')
# clean the data removing NAN (infinite values)
dtest.dropna(inplace=True)
dtrain.dropna(inplace=True)
# pass the data as an array for testing (prediction data)
Xtest = np.array(dtest[['x']])
ytest = np.array(dtest[['y']])
# pass the data as an array for training
X_train = pd.DataFrame(dtrain[['x']])
y_train = np.array(dtrain[['y']])






# calling the linear function to create the model
linear = LinearRegression()
# using the function and finding the coeff by using the collected data
predictor = linear.fit(X_train,y_train)
# predicting the future values using the linear eqn which has the coeff found by training
predicting = linear.predict(Xtest)
# finding the R-squared [1-sum squared regression / sum squared total(difference between given(y)and mean(y)]
acc = linear.score(Xtest,ytest)
# this will be more accurate than the previous because we use the same data to find the variation and train the mode
acc2 = linear.score(X_train,y_train)
print(predicting)
print(acc)
# plotting the new data
plt.scatter(Xtest,ytest)
# now plotting the fitted line by passing the new data into the trained linear model
plt.plot(Xtest,predicting,linewidth = 3,color ='black')

plt.show()
