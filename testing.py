import numpy as np
from scipy.optimize import linprog

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    b = np.array(list(map(int, f.readline().split())))
    c = np.array(list(map(int, f.readline().split())))
    A = []
    for i in range(m):
        row = np.array(list(map(int, f.readline().split())))
        A.append(row)
    A = np.array(A)


# Bounds on variables
bounds = [(0, None)] * n   # Set lower bound as 0 for all variables

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if res.success:
    # print("Optimal solution found:")
    print("Objective value =", res.fun)
    # print("Solution =", res.x)
else:
    print("Optimization failed. Check input constraints.")
