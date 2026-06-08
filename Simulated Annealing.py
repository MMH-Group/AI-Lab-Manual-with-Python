# Part 1: Objective function plot
from numpy import arange
from matplotlib import pyplot

def objective(x):
    return x[0]**2.0  # Simple parabola function

r_min, r_max = -5.0, 5.0
inputs = arange(r_min, r_max, 0.1)
results = [objective([x]) for x in inputs]

pyplot.plot(inputs, results)
pyplot.axvline(x=0.0, ls='--', color='red')  # Optimal point
pyplot.show()
