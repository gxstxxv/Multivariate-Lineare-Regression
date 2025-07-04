import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from linear_regression import (
    linear_hypothesis,
    mse_cost_function,
    gradient_descent,
)
from plotting_functions import (
    plot_progress,
)


data = load_diabetes()

X = data.data
y = data.target.reshape(-1, 1)

scaler = StandardScaler()
X = scaler.fit_transform(X)

m = X.shape[1]
theta = np.zeros((m + 1, 1))

alpha = 0.01
iterations = 500

costs, thetas = gradient_descent(
    learning_rate=alpha,
    theta=theta,
    iterations=iterations,
    x=X,
    y=y,
    cost_function=mse_cost_function,
    verbose=True,
)

theta = thetas[-1]
h = linear_hypothesis(theta)
Y = h(X)

mse = mean_squared_error(y, Y)
r2 = r2_score(y, Y)

print(f"MSE: {mse:.4f}")
print(f"R²: {r2:.4f}")

plot_progress(costs)
