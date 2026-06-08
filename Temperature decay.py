# Part 2: Temperature decay
from matplotlib import pyplot

iterations = 100
initial_temp = 10
iterations_list = [i for i in range(100)]
temperatures = [initial_temp / float(i + 1) for i in iterations_list]

pyplot.plot(iterations_list, temperatures)
pyplot.xlabel('Iteration')
pyplot.ylabel('Temperature')
pyplot.show()
