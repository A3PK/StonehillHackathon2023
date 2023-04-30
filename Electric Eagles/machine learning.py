# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv('building_energy.csv')

# Preprocess the data
# Feature engineering
data['total_occupancy'] = data['num_occupants'] * data['sq_ft_per_occupant']
data['cooling_load'] = data['window_area'] * data['outdoor_temp'] * data['cooling_degree_days']
data['heating_load'] = data['window_area'] * data['outdoor_temp'] * data['heating_degree_days']
# Data cleaning
data.dropna(inplace=True)

# Split the data into training and test sets
X = data.drop('energy_consumption', axis=1)
y = data['energy_consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean squared error: %.2f' % mse)
print('R2 score: %.2f' % r2)

# Use the model to make predictions and identify opportunities for energy reduction
new_data = pd.read_csv('new_building_data.csv')
new_data['total_occupancy'] = new_data['num_occupants'] * new_data['sq_ft_per_occupant']
new_data['cooling_load'] = new_data['window_area'] * new_data['outdoor_temp'] * new_data['cooling_degree_days']
new_data['heating_load'] = new_data['window_area'] * new_data['outdoor_temp'] * new_data['heating_degree_days']
new_data.dropna(inplace=True)

new_data['predicted_energy_consumption'] = model.predict(new_data.drop('energy_consumption', axis=1))
new_data['energy_reduction_potential'] = new_data['energy_consumption'] - new_data['predicted_energy_consumption']

print(new_data[['building_id', 'energy_consumption', 'predicted_energy_consumption', 'energy_reduction_potential']])