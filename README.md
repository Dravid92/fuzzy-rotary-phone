# Project 2 - Simple Linear Regression 
Linear regression is to model the relationship between two continous variable , given that significant correlation exists between the two variables.
## How does it work ?
![1_LEmBCYAttxS6uI6rEyPLMQ](https://user-images.githubusercontent.com/41041795/93014539-849ae300-f5cf-11ea-80e0-517c24edaaf3.png)
- The general idea of Linear Regression is to fit the line that could best fit the data when the data is visualized using scatter plot.
## How to find the Best fit line ?
- The line that best fits the data is found by,  
             		
		y = m*x + c 
- **m** is the slope of the line , **c** is the y intercept (where does the line interacts with the y- axis) 
- **x** is the explanatory variable (independent variable) , **y** is the response variable (dependent variable) 
### Finding m and c :
![Capture](https://user-images.githubusercontent.com/41041795/93015022-6f27b800-f5d3-11ea-8939-d0bc6a0a84b7.PNG) 
	     
		
- Created random values for y using random.rand depending on whether or not we want the data points to be correlated.

- Calculated m and b ,where m is the slope of the line which tells you how the line formed by the co-ordinates (x,y) in the graph [M-POSTIVE -line is increasing from left to right M-NEGATIVE - line is decreasing from right to left] ,X is basically range of y  which is from 0 to 39 ,
b is the y intercept which is the point where the line interesects the Y-axis

- Finding R-squared which requres sum of squares of Regression and Sum of squares of Total
	- Sum of squares of Regression is the difference between the prediction(predicted y value) and the population mean(mean of y)
	- Sum of squares of Total is difference between the dependent value(y given) and its mean

############## FORMULAS ###################
## Linear Reg.- y = mX + b
### m = Slope= Change in x   Mean(X)Mean(y)-Mean(X*y)
	     -----------   -----------------------    
             Change in y   Mean(X)**2 - Mean(X**2)	
### b = y-mX
​	
### Variance - (Sum(X -mean(X))^2)/N 
	- Where N is the total # of data points [here I haven't used variance formula instead created the data points of y based on variance,you can change the value of variance and thus values of y ,which intern changes the value of R-squared(accuracy)] 

### R-squared is 1-(SSR/SST)
- SSR = Sum(ŷ-Mean(y))**2
- SST = Sum(y -Mean(y))**2


