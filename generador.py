import random

file1 = open('output.txt', 'w')
file2 = open('matriz-hotaken.txt', 'w')
nw_ofertaF = open('noroeste_oferta.txt', 'w')
nw_demandaF = open('noroeste_demanda.txt', 'w')
nw_costoF = open('noroeste_costo.txt', 'w')
#cij: horas mensuales asignadaas para el trabajo j al trabajador i
#xij: Trabajador i asignado a trabajo j
in1 = input()
print()
n = int(in1)
in1 = input()
print()
m = int(in1)

matriz = []
nw_oferta = []
nw_demanda = []
nw_costos = [[0 for _ in range(m)] for _ in range(n)]

costos = [[0 for _ in range(m)] for _ in range(n)]
horas_minimas = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = []
    for j in range(m):
        costos[i][j] = random.randint(25, 50)
        nw_costos[i][j] = costos[i][j]
        horas_minimas[i][j] = random.randint(20, 50)
        temp.append([costos[i][j],0])
    matriz.append(temp)

horas_trabajadores = [0 for _ in range(n)]
costos_proyectos = [0 for _ in range(m)]
horas_proyectos = [0 for _ in range(m)]

for i in range(n):
    horas_trabajadores[i] = random.randint(50, 100)
    nw_oferta.append(horas_trabajadores[i])
    matriz[i].append(horas_trabajadores[i])

for i in range(m):
    horas_proyectos[i] = random.randint(10, 50)
    nw_demanda.append(horas_proyectos[i])
matriz.append(horas_proyectos)

for i in range(m):
    costos_proyectos[i] = random.randint(6250, 250000)

nw_costoF.write(str(n) + "\n")
nw_costoF.write(str(m) + "\n")
for i in range(n):
    for j in range(m):
        nw_costoF.write(str(nw_costos[i][j]))
        if j == m - 1: nw_costoF.write("\n")
        else: nw_costoF.write("/")


for i in range(m):
    nw_demandaF.writelines(str(nw_demanda[i]) + "\n")

for i in range(n):
    nw_ofertaF.writelines(str(nw_oferta[i]) + "\n")

nw_costoF.close()
nw_demandaF.close()
nw_ofertaF.close()    


file2.write(str(n))
file2.write("\n")
file2.write(str(m))
file2.write("\n")

for fila in matriz:
    #print(fila)
    for x in fila:
        file2.write(str(x))
        file2.write("\n")
        #print(x)
file2.close()

fo = "min: "

file1.write("min:")
for i in range(n):
    for j in range(m):
        cost = costos[i][j]
        currx = str(cost) + " c" + str(i + 1) + "_" +  str(j + 1)
        #fo = fo + " +" + currx
        file1.write(" +" + currx)
file1.write(";\n")
file1.write("\n")
#fo = fo + ";"

#print(fo)

st = ""
#Horas mensuales máximas por trabajador
for i in range(n):
    cost = horas_trabajadores[i]
    for j in range(m):
        currx = " c" + str(i + 1) + "_" + str(j + 1)
        if(j == 0): file1.write("+" + currx)
        else: file1.write(" +" + currx)
        
    file1.write(" <= " + str(cost) + ";\n")
    #print(st)
    st = ""
file1.write("\n")
#Horas mensuales mínimas por proyecto
for i in range(m):
    cost = horas_proyectos[i]
    for j in range(n):
        currx = " c" + str(j + 1) + "_" + str(i + 1)
        if(j == 0): file1.write("+" + currx)
        else: file1.write(" +" + currx)
    file1.write(" >= " + str(cost) + ";\n")
    #print(st)
    st = ""
file1.write("\n")
#Cantidad máxima de trabajadores asignados a un proyecto
for i in range(m):

    for j in range(n):
        currx = " x" + str(j + 1) + "_" + str(i + 1)
        if(j == 0): file1.write("+" + currx)
        else: file1.write(" +" + currx)
    
    file1.write(" <= 5;\n") 
    #print(st)
    st = ""
file1.write("\n");

#Cantidad máxima de proyectos asignados a un trabajador
for i in range(n):

    for j in range(m):
        currx = " x" + str(i + 1) + "_" + str(j + 1)
        if(j == 0): file1.write("+" + currx)
        else: file1.write(" +" + currx)
    
    file1.write(" <= 5;\n") 
    #print(st)
    st = ""
file1.write("\n")

#Límite de presupuesto por proyecto
for i in range(m):
    cost = costos_proyectos[i]
    for j in range(n):
        costo_t = costos[j][i]
        currx = str(costo_t) + " c" + str(j + 1) + "_" + str(i + 1)
        if(j == 0): file1.write("+" + currx)
        else: file1.write(" +" + currx)
    
    file1.write(" <= " + str(cost) + "; \n")
    #print(st)
    st = ""
file1.write("\n")


st = ""
#restricción de variables binarias
for i in range(n):
    for j in range(m):
        st = ""
        currx = "c" + str(i + 1) + "_" + str(j + 1)
        minim = horas_minimas[i][j]
        file1.write(currx + "<= 10000000 x" + str(i + 1) + "_" + str(j + 1) + ";\n")
        st = ""
        file1.write(currx + " >= " + str(minim) + " x" + str(i + 1) + "_" + str(j + 1) + ";\n")
        
st = ""

#Naturaleza de las variables
file1.write("bin")
for i in range(n):
    for j in range(m):
        currx = " x" + str(i + 1) + "_" + str(j + 1)
        if( i == n - 1 and j == m - 1): file1.write(currx + ";\n")
        else: file1.write(currx + ",")
 
st = ""

file1.write("int")
for i in range(n):
    for j in range(m):
        currx = " c" + str(i + 1) + "_" + str(j + 1)
        if( i == n - 1 and j == m - 1): file1.write(currx + ";\n")
        else: file1.write(currx + ",")
file1.close()