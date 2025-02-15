from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="max_drinks", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total"

model += (2 * lemonade + fruit_juice <= 100, "Water")
model += (1 * lemonade <= 50, "Sugar")
model += (1 * lemonade <= 30, "Lemon_Juice")
model += (2 * fruit_juice <= 40, "Fruit")

model.solve(PULP_CBC_CMD(msg=False))

print(f"Oprimal amount of Lemonade: {lemonade.varValue}")
print(f"Oprimal amount of Fruit Juice: {fruit_juice.varValue}")