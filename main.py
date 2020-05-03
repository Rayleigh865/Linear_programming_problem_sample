import pulp

problem = pulp.LpProblem('test', pulp.LpMaximize)

x1 = pulp.LpVariable('x1', 0, 100)
x2 = pulp.LpVariable('x2', 0, 100)

problem += 3*x1 + 5*x2

problem += x1+7*x2<=140
problem += 2*x1+4*x2<=100
problem += 3*x1+2*x2<=120
problem += x1>=0
problem += x2>=0

status = problem.solve()

print("Status", pulp.LpStatus[status])
print(problem)
print("Result")
print("x1", x1.value()) 
print("x2", x2.value()) 
