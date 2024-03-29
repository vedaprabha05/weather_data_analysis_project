# -*- coding: utf-8 -*-
"""weather_data_analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ghtXHoMYRzbyUWDyIsgffzL6esVtEPD1

#Weather Data Analysis

**Importing libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"""**Load the dataset**"""

weather_data = pd.read_csv("/content/weather[1].csv")
weather_data

"""**Data Exploration**"""

#Headings
weather_data.head()

#Last rows
weather_data.tail()

#display
display(weather_data)

#Describe
weather_data.describe()

#information
weather_data.info()

#Shaping
weather_data.shape

"""**Data Visualization**"""

#Pair Plot

sns.pairplot(weather_data[['MinTemp', 'MaxTemp', 'Rainfall']])
plt.title('Pairplot of MinTemp, MaxTemp, and Rainfall')
plt.show()

"""**Feature Engineering**"""

weather_data['HotDay'] = weather_data['MaxTemp'] > 30
weather_data['HotDay']

"""**Data Analysis**"""

#Analyse MinTemp

average_MinTemp = weather_data['MinTemp'].mean()
MinTemp_std_dev = weather_data['MinTemp'].std()

print("MinTemp Analysis:")
print("Average MinTemp:", average_MinTemp)
print("MinTemp Standard Deviation:", MinTemp_std_dev)

#Analyse MaxTemp

average_MaxTemp = weather_data['MaxTemp'].mean()
MaxTemp_std_dev = weather_data['MaxTemp'].std()

print("MaxTemp Analysis:")
print("Average MaxTemp:", average_MaxTemp)
print("MaxTemp Standard Deviation:", MaxTemp_std_dev)

#Analyse Humidity9am

average_humidity9am = weather_data['Humidity9am'].mean()
max_humidity9am = weather_data['Humidity9am'].max()
min_humidity9am = weather_data['Humidity9am'].min()
humidity9am_std_dev = weather_data['Humidity9am'].std()

print("\nHumidity9am Analysis:")
print("Average Humidity9am:", average_humidity9am)
print("Max Humidity9am:", max_humidity9am)
print("Min Humidity9am:", min_humidity9am)
print("Humidity9am Standard Deviation:", humidity9am_std_dev)

#Analyse Rainfall

average_rainfall = weather_data['Rainfall'].mean()
max_rainfall = weather_data['Rainfall'].max()
min_rainfall = weather_data['Rainfall'].min()
rainfall_std_dev = weather_data['Rainfall'].std()

print("\nRainfall Analysis:")
print("Average Rainfall:", average_rainfall)
print("Max Rainfall:", max_rainfall)
print("Min Rainfall:", min_rainfall)
print("Rainfall Standard Deviation:", rainfall_std_dev)

#Analyze WindSpeed3pm

average_windspeed3pm = weather_data['WindSpeed3pm'].mean()
max_windspeed3pm = weather_data['WindSpeed3pm'].max()
min_windspeed3pm = weather_data['WindSpeed3pm'].min()
windspeed3pm_std_dev = weather_data['WindSpeed3pm'].std()

print("\nWindSpeed3pm Analysis:")
print("Average WindSpeed3pm:", average_windspeed3pm)
print("Max WindSpeed3pm:", max_windspeed3pm)
print("Min WindSpeed3pm:", min_windspeed3pm)
print("WindSpeed3pm Standard Deviation:", windspeed3pm_std_dev)

"""**Data Vizualization**"""

#Scatter plot

plt.figure(figsize=(8, 6))
plt.scatter(weather_data['MaxTemp'], weather_data['Sunshine'], color='green', alpha=0.5)
plt.title('Scatter Plot of MaxTemp vs Sunshine')
plt.xlabel('MaxTemp')
plt.ylabel('Sunshine')
plt.grid(True)
plt.show()

#Bar plot

plt.figure(figsize=(10, 6))
count = weather_data['WindGustDir'].value_counts()
count.plot(kind='bar')
plt.title('Count of WindGustDir')
plt.xlabel('WindGustDir')
plt.ylabel('Count')
plt.show()

#Line plot

plt.figure(figsize=(9, 6))
plt.plot(weather_data['MinTemp'], marker='o', linestyle='-', label='MinTemp', alpha=0.5)
plt.plot(weather_data['MaxTemp'], marker='o', linestyle='-', label='MaxTemp', alpha=0.5)
plt.title('Temperature Over Time')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()

#Histogram

plt.figure(figsize=(8, 6))
plt.hist(weather_data['Rainfall'],bins= 30, color='hotpink', alpha=0.5)
plt.title('Histogram of Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#Distribution plot of MaxTemp

sns.histplot(weather_data['MaxTemp'], kde=True)

"""**Advanced Analysis**"""

# Prepare the data for prediction

X = weather_data[['MinTemp', 'MaxTemp']]
y = weather_data['Rainfall']

# Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model

model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and calculate the Mean Squared Error

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error for Rainfall Prediction: {mse}')

"""**Conclusions and Insights**

1. Mean Squared Error for Rainfall Prediction: 37.0768456005826
2. Average MinTemp: 7.265573770491804
3. Average MaxTemp: 20.550273224043714
4. Mean of Evaporation: 4.521858
5. Max Sunshine: 13.600000
"""