from pulp import *

# Read input from file
with open("input.txt", "r") as file:
    # Read dimensions of c and b
    n, m = map(int, file.readline().split())

    # Read b
    b = list(map(int, file.readline().split()))

    # Read c
    c = list(map(int, file.readline().split()))

    # Read A
    A = []
    for _ in range(m):
        A.append(list(map(int, file.readline().split())))

# Define the problem
problem = LpProblem("Integer Linear Programming Problem", LpMinimize)

# Define the decision variables
x = [LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(1, n + 1)]  # Integer variables x1, x2, ..., xn

# Define the constraints
for i in range(m):
    constraint = LpConstraint(
        e=LpAffineExpression([(x[j], A[i][j]) for j in range(n)]),
        sense=LpConstraintLE,
        rhs=b[i],
    )
    problem += constraint

# Define the objective function
problem += lpSum([c[j] * x[j] for j in range(n)])  # Minimize c1*x1 + c2*x2 + ... + cn*xn

# Solve the problem
problem.solve()

# Print the results
print("Status:", LpStatus[problem.status])
print("Optimal solution:")
for i in range(n):
    print(f"x{i+1} =", value(x[i]))
print("Objective value =", value(problem.objective))