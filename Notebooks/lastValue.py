import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the training and test data
train_data = pd.read_csv('data/train.csv', index_col='Date', parse_dates=True)
test_data = pd.read_csv('data/test.csv', index_col='Date', parse_dates=True)

# Ensure the index is in the correct datetime format
train_data.index = pd.to_datetime(train_data.index)
test_data.index = pd.to_datetime(test_data.index)

# Create a function to calculate the last value model predictions
def last_value_model(train, test):
    last_values = train.iloc[-1]
    predictions = pd.DataFrame(np.tile(last_values.values, (len(test), 1)), index=test.index, columns=test.columns)
    return predictions

# Generate predictions
predictions = last_value_model(train_data, test_data)

# Calculate metrics
metrics = {}
for symbol in train_data.columns:
    y_true = test_data[symbol]
    y_pred = predictions[symbol]
    metrics[symbol] = {
        'Mean Absolute Error': mean_absolute_error(y_true, y_pred),
        'Root Mean Squared Error': np.sqrt(mean_squared_error(y_true, y_pred)),
        'Mean Absolute Percentage Error': np.mean(np.abs((y_true - y_pred) / y_true)) * 100,
        'R^2 Score': 1 - (np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2))
    }

# Convert metrics to a DataFrame for display
metrics_df = pd.DataFrame(metrics).T

# Display the metrics
print("Stock Prediction Metrics:")
print(metrics_df)

# Plot the results
plt.figure(figsize=(15, 10))
for i, symbol in enumerate(train_data.columns, 1):
    plt.subplot(2, 3, i)
    plt.plot(train_data[symbol], label='Train Data')
    plt.plot(test_data[symbol], label='Test Data')
    plt.plot(predictions[symbol], label='Predictions')
    plt.title(symbol)
    plt.legend()

plt.tight_layout()
plt.show()

