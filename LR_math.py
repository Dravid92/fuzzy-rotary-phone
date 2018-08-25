from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#x = np.array([1,2,3,4,5,6], dtype=np.float64)
#y = np.array([9,7,5,4,2,4],dtype=np.float64)

def dataset(hv,variance , step = 2, correlation = 'neg'):
    v = 1
    y =[]
    for i in range(hv):
        r = v + random.randrange(-variance , variance)
        y.append(r)
        if correlation and correlation == 'pos':
            v+=step
        elif correlation and correlation == 'neg':
            v-=step
    x = [i for i in range(len(y))]
    #print(y)
    return np.array(x,dtype=np.float64) ,np.array(y,dtype=np.float64)

# dataset function contains random values -'hv' , variance -
[x,y]=dataset(40,20,step=2,correlation='pos')



def slope_and_intercept(x,y):

    m = (((mean(x)*mean(y)) - (mean(x*y)))/
         ((mean(x)*mean(x))- mean(x*x)))
    b = mean(y) - m * mean(x)
    return m , b

m,b = slope_and_intercept(x,y)

p_x = 14
p_y = m*p_x + b

regression = [(m*i) + b for i in x]

# print(regression)
mean_line = [mean(y) for i in y]
# print(mean_line)
SEy_cap = sum((regression - y)**2)
# Sum of squared Regression
SEy_mean = sum((mean_line - y)**2)
# Sum of squared Total
r_squared = 1- (SEy_cap/SEy_mean)
# computing R-squared
print(r_squared)





plt.scatter(x,y)
plt.scatter(p_x,p_y,s=50,color='r')
plt.plot(x,regression)
plt.show()


