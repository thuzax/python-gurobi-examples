from gurobipy import *

tipos_avioes = [0, 1, 2]
tamanho_avioes = [1, 1/3, 5/3]
max_galpao = 40

verba = 220
custos = [5.1, 3.6, 6.8]

receitas = [330, 300, 420]
pilotos = [30, 20, 10]

model = Model("empresa_aviacao")

quantidades = model.addVars(len(tipos_avioes), vtype=GRB.INTEGER, name="quantidades", lb=0)

model.setObjective(quicksum(quantidades[i] * (receitas[i] - custos[i]) for i in tipos_avioes), GRB.MAXIMIZE)

limite_galpao = model.addConstr(
    (
        quicksum(tamanho_avioes[i] * quantidades[i] for i in tipos_avioes) 
        <= max_galpao 
    ),
    name="limite_galpao"
)

limite_custo = model.addConstr(
    (
        quicksum(quantidades[i] * custos[i] for i in tipos_avioes) 
        <= verba
    ),
    name="limite_custo"
)

limite_pilotos_md11 = model.addConstr(
    (
        2 * quantidades[2] 
        <= pilotos[2]
    ),
    name="limites_pilotos_md11"
)

limite_pilotos_b717 = model.addConstr(
    (
        2 * quantidades[0] + 2 * quantidades[2] <= pilotos[0] + pilotos[2]
    ),
    name="limite_pilotos_b717"
)

limite_pilotos_b737 = model.addConstr(
    (
        2 * quantidades[1] + 2 * quantidades[2] <= pilotos[1] + pilotos[2]
    ),
    name="limite_pilotos_b737"
)

limite_pilotos = model.addConstr(
    (
        2 * quicksum(quantidades[i] for i in tipos_avioes)
        <= quicksum(pilotos[i] for i in tipos_avioes)
    ),
    name="limite_pilotos"
)

model.optimize()

for var in model.getVars():
    print(var.varName, var.x)

model.write("arquivo_exemplos.mps")

