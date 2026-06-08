from numpy import asarray, exp, sqrt, cos, e, pi
from numpy.random import randn, rand, seed

def objective(v):
    x, y = v
    return (-20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) 
            - exp(0.5 * (cos(2*pi*x) + cos(2*pi*y))) + e + 20)

def in_bounds(point, bounds):
    for d in range(len(bounds)):
        if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
            return False
    return True

def hillclimbing(objective, bounds, n_iterations, step_size):
    solution = None
    while solution is None or not in_bounds(solution, bounds):
        solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    
    solution_eval = objective(solution)
    
    for i in range(n_iterations):
        candidate = None
        while candidate is None or not in_bounds(candidate, bounds):
            candidate = solution + randn(len(bounds)) * step_size
        
        candidate_eval = objective(candidate)
        if candidate_eval <= solution_eval:
            solution, solution_eval = candidate, candidate_eval
            print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
    
    return [solution, solution_eval]

seed(1)
bounds = asarray([[-5.0, 5.0], [-5.0, 5.0]])
best, score = hillclimbing(objective, bounds, 1000, 0.05)
print('f(%s) = %f' % (best, score))
