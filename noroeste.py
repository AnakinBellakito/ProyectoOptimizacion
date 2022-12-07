import random
import ast
import time

def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    count = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
            count += 1
            """
            COMENTADO: Considera la restricción de 5 proyectos por persona
            if count == 5:
                i += 1
                count = 0
            """
    return bfs, count

def calcular_costo(bfs, costos):
    res = 0
    cant_vars = 0
    for tuple in bfs:
        row = tuple[0][0]
        col = tuple[0][1]
        amt = tuple[1]
        res += amt * costos[row][col]
        if amt != 0: 
            print("Fila " + str(row) + ", columna " + str(col) + ", cantidad: " + str(amt))
            cant_vars += 1
    print("Costo total basal: " + str(res))
    print("Cantidad de variables usadas: " + str(cant_vars))

fileC = open('noroeste_costo.txt', 'r')
fileD = open('noroeste_demanda.txt', 'r')
fileO = open('noroeste_oferta.txt', 'r')
n = int(fileC.readline())
m = int(fileC.readline())
filas = n
columnas = m
oferta = []
demanda = []
costos = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = fileO.readline()
    o = int(line)
    oferta.append(o)

for i in range(m):
    line = fileD.readline()
    d = int(line)
    demanda.append(d)

for i in range(n):
    line = fileC.readline()
    stringlist = line.split("/")
    costos[i] = [int(e) for e in stringlist]

fileC.close()
fileD.close()
fileD.close()
supply = [30, 70, 50]
demand = [40, 30, 40, 40]
bfs, iter = north_west_corner(oferta, demanda)
t0 = time.process_time()
calcular_costo(bfs, costos)
t1 = time.process_time()
print("Cantidad de iteraciones: " + str(iter))
print("Tiempo de ejecución: " + str(t1 - t0) + " segundos")