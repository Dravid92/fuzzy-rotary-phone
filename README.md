# Project 2 - Simple Linear Regression 
Linear regression is to model the relationship between two continous variable , given that significant correlation exists between the two variables.
## How does it work ?

![1_LEmBCYAttxS6uI6rEyPLMQ](https://user-images.githubusercontent.com/41041795/93014539-849ae300-f5cf-11ea-80e0-517c24edaaf3.png)

- The general idea of Linear Regression is to fit the line that could best fit the data when the data is visualized using scatter plot.
## How to find the Best fit line ?
- The line that best fits the data is found by,  
             		
		y = a*x + b 
- **a** is the slope of the line , **b** is the y intercept (where does the line interacts with the y- axis) 
- **x** is the explanatory variable (independent variable) , **y** is the response variable (dependent variable) 
- Generally a and b are considered as co-efficients , more like weights for particular variable 
- If the coefficent is zero then there is no effect of that particular variable over the dependent variable (y)
## Math Behind Linear Regression

### Finding a and b :

![Capture](https://user-images.githubusercontent.com/41041795/93015022-6f27b800-f5d3-11ea-8939-d0bc6a0a84b7.PNG) 

Σ -  is called **sigma** which interpreted as sum 
- therefore Σxy mean **sum of all the x * y values **

-  In our case we use m and c as co-efficent and they are calculated using the below formula 

![1_f_VhshEGxwhT4tZLDzwtgA](https://user-images.githubusercontent.com/41041795/93995367-8c683d80-fdae-11ea-8745-1b448ce6dfa4.png)

 - This is how co-efficents are found using python 
 
 ![Capture](https://user-images.githubusercontent.com/41041795/93996185-90e12600-fdaf-11ea-8af3-3eeb07913c25.PNG)
 
## R- Squared 
- R- squared states how much does the Independent variable explains the dependent variable(y) 
- For example a R- squared of 100 % tells us that all the changes in the dependent variable are 100 percent explained by using the changes in the Independent variable 
- Formula for R- Squared 

![capture2](https://user-images.githubusercontent.com/41041795/93997377-f7b30f00-fdb0-11ea-9baf-484c760ad6c5.PNG)

### Using python the above notations are found using :

![capture3](https://user-images.githubusercontent.com/41041795/93997661-4496e580-fdb1-11ea-8990-fd6f8fbc2526.PNG)


## visualizing using math and python 

- Inorder to visualize the data , scatter plot is used 
- for visualizing the **best fit line** , the value of the equation for each x value is used. 

Below is the code to visualize the data and the best fit line using matlplotlib library 

![capture4](https://user-images.githubusercontent.com/41041795/93998317-fdf5bb00-fdb1-11ea-9c1e-6b2116e83560.PNG)

**p_x** - are the x observation   

**p_y** - is the value from the equation **a*x+b**

## Linear Regression using SKlearn

- Split the data into train and test datasets

![capture5](https://user-images.githubusercontent.com/41041795/93998879-c9363380-fdb2-11ea-927c-93a5d42bc7c7.PNG)

- Create a Linear Regression model using the LinearRegression function from the SKlearn module

- Fit the data to the model 

![captur6](https://user-images.githubusercontent.com/41041795/93999031-f682e180-fdb2-11ea-9a33-b44407390ad1.PNG)




