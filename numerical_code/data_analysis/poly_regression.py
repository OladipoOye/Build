# example working with polynomial regression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# example of implementing linear regression
# Generate some array data
X = np.array([[1, 2], [2, 4], [3, 5], [4, 2], [5, 8]])
y = np.array([1, 2, 3, 40, 32])

#fit the model
model = LinearRegression().fit(X, y)

#extract the intercept and coefficients for the data
r_sq = model.score(X, y)
intercept, coefficients = model.intercept_, model.coef_
print(f"Coeff of determination: {r_sq}")
print(f"Intercept: {intercept}")
print(f"Coefficients: {coefficients}")

#fucntion for polynomial fit 
def polyfit(x, y, new_data=[])
    #x is the input array
    #y is the output array
    
    x, y = np.array(x), np.array(y)
    
    #create the x^2 array, and concatenate it to x
    x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
    
    #fit the model
    model = LinearRegression().fit(x_, y)
    
    #get the coefficient of determination and the correlation coefficients
    r_sq = model.score(x_, y)
    intercept, coefficients = model.intercept_, model.coef_
    print(f"Coeff of determination: {r_sq}")
    print(f"Intercept: {intercept}")
    print(f"Coefficients: {coefficients}")
    
    #predict the new outputs based on the pred array, if an array is passed
    if len(new_data) > 0:
        new_data=np.array(new_data)
        new_y = model.predict(new_data)
        print(f"The new y values are: {new_y}")
        return new_y

