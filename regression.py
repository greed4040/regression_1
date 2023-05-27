import numpy as np

# Example time series data
x = np.array([1, 2, 3, 4, 5])  # Independent variable
y = np.array([2, 4, 6, 8, 10])  # Dependent variable

# Initialize coefficient
c = 1  # Coefficient for x

# Define the objective function to minimize
def objective(c):
    y_pred = [c * xi for xi in x]  # Calculate the predicted values
    squared_diffs = [(yi - y_pred[i])**2 for i, yi in enumerate(y)]  # Calculate the squared differences
    return sum(squared_diffs)  # Calculate the sum of squared differences

# Perform optimization using brute-force search
min_error = float('inf')  # Initialize the minimum error
best_c = None  # Best coefficient

for c in [i / 10 for i in range(0, 101)]:  # Try different values for c
    error = objective(c)  # Calculate the error for the current coefficient
    if error < min_error:  # If the error is lower than the minimum error
        min_error = error  # Update the minimum error
        best_c = c  # Update the best coefficient

# Print the best coefficient and minimum error
print("Best Coefficient:", best_c)
print("Minimum Error:", min_error)