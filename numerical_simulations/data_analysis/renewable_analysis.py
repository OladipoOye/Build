# model for analysis of solar energy data
# This code is for analyzing solar energy data using linear regression

#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('owid-energy-data.csv')

# get 2023 data
df_latest = df[df['year'] == 2023]

# Filter for necessary columns
columns_needed = [
    'gdp_per_capita',
    'population',
    'urban_population_percent',
    'solar_consumption'  # or 'solar_share_energy'
]

df_solar = df_latest.dropna(subset=columns_needed)

# Define features and target
X = df_solar[['gdp_per_capita', 'population', 'urban_population_percent']]
y = df_solar['solar_consumption']  # or 'solar_share_energy'

# Optional: log-transform if very skewed
y = np.log1p(y)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate R-squared and RMSE
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("Coefficients:")
for feature, coef in zip(['gdp_per_capita', 'population', 'urban_population_percent'], model.coef_):
    print(f"{feature}: {coef:.4f}")

#plot the input variables separately
sns.regplot(x='gdp_per_capita', y='solar_consumption', data=df_solar)
plt.title("GDP per Capita vs Solar Consumption")
plt.show()