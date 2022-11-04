# import necessary packages
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.optimize import minimize
from scipy.optimize import curve_fit

plt.style.use('fivethirtyeight')


# %matplotlib inline


def squared_loss(y_obs, theta):
    return (y_obs - theta) ** 2


y_obs = 10
theta_values = np.linspace(0, 20, 100)  # some arbitrary values of theta
# type your code here
s = lambda x: (y_obs - x) ** 2
s_loss = s(theta_values)
# plt.plot(theta_values,s_loss)
# plt.xlabel(r'$\theta$')
# plt.ylabel('L2 loss')
# plt.title(r'L2 Loss for different values of $\theta$'); # Do not want to show an additional line of Text, use ";"
# plt.show()

# Run this cell, do not change anything
df = sns.load_dataset("tips")
tips = np.array(df['tip'])  # array of observed tips


def mean_squared_error(theta, data):
    r_sum = np.square(np.subtract(theta, data)).sum()
    return r_sum / len(data)


print(mean_squared_error(5.3, tips))

theta_values = np.linspace(0, 6, 100)
mse = [mean_squared_error(theta, tips) for theta in theta_values]
# plt.plot(theta_values, mse)
# plt.xlabel(r'$\theta$')
# plt.ylabel('L2 loss')
# plt.title(r'L2 Loss for different values of $\theta$');
# plt.show()

# mse_observed_theta = np.rint(np.min(mse))

mse_observed_theta = np.rint(theta_values[np.where(mse == np.min(mse))])
print(mse_observed_theta)

x_values = np.linspace(-4, 2.5, 100)


def fx(x):
    return 0.1 * x ** 4 + 0.2 * x ** 3 + 0.2 * x ** 2 + 1 * x + 10


# plt.plot(x_values, fx(x_values));
# plt.show()


print(minimize(fx, x0=1.1))

def func(x):
    return mean_squared_error(x, tips)



min_scipy = minimize(func, x0=0.0)['x'][0]
print(min_scipy)

min_computed = np.mean(tips)
print(min_computed)


def abs_loss(theta, y_obs):
    return np.abs(theta - y_obs)


def mean_absolute_error(theta, data):
    r_sum = np.abs(np.subtract(theta, data)).sum()
    return r_sum / len(data)


theta_values = np.linspace(2.7, 3.02, 100)
mae = [mean_absolute_error(theta, tips) for theta in theta_values]
plt.plot(theta_values, mae)
plt.xlabel(r'$\theta$')
plt.ylabel('L1 Loss')
plt.title(r'L1 Loss for different values of $\theta$');
plt.show()

mae_observed_theta = np.around(np.min(mae),1)
print(mae_observed_theta)

