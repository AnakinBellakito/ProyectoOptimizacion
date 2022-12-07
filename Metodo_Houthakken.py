from copy import deepcopy
import ast
import time

#Encuentra flujos mutuamente preferibles
def FindFmp(matriz):
    k = 0
    fme = []
    matrizS = deepcopy(matriz)
    while k < filas:
        menor = 100
        i = 0
        j = 0
        y = 0
        posfme = True
        for j in range(0,columnas):
            if(matrizS[k][j][0] < menor and (matriz[k][columnas] != 0 and matriz[filas][j] != 0) ):
                menor = matrizS[k][j][0]
                y = j
        if(menor == 100):
            posfme = False

        
        for i in range(0,filas):
            #SE ENCUENTRA QUE NO ES FME
            if(matrizS[i][y][0] < menor and posfme and (matriz[i][columnas] != 0 and matriz[filas][y] != 0)):
                matrizS[k][y][0] = 100
                break
            
        #IF NOT BREAK
        else:
            if(i+1 == filas):
                if(menor != 100):
                    fme.append([k,y])
                    k +=1
                    i = 0
                    for i in range(0,filas):
                        matrizS[i][y][0] = 100
                else:
                    k+=1
    
    return fme
        

#Realiza operaciones a matriz en función de flujos mutuamente preferibles
def SearchFlujos(matriz,lista):
    for x in lista:
        if matriz[x[0]][columnas] < matriz[filas][x[1]]:
            matriz[x[0]][x[1]][1] = matriz[x[0]][columnas]
            matriz[filas][x[1]] = matriz[filas][x[1]] - matriz[x[0]][columnas]
            matriz[x[0]][columnas] = matriz[x[0]][columnas] - matriz[x[0]][columnas]
            
        else:
            matriz[x[0]][x[1]][1] = matriz[filas][x[1]]
            matriz[x[0]][columnas] = matriz[x[0]][columnas] - matriz[filas][x[1]]
            matriz[filas][x[1]] = matriz[filas][x[1]] - matriz[filas][x[1]]
        
    
            
#Programa--------------------------------------------------------     
'''   
filas = 3
columnas = 4

matriz = [
          [[3,0],[2,0],[7,0],[6,0],5000]
         ,[[7,0],[5,0],[2,0],[3,0],6000]
         ,[[2,0],[5,0],[4,0],[5,0],2500]
         ,[6000,4000,2000,1500]
          ]
'''

#################################################
matriz = []
archivo = open("matriz-hotaken.txt", "r")
t0 = time.process_time()

n = int(archivo.readline())
m = int(archivo.readline())
filas = n
columnas = m

x = 0
i = 0
tmp = []
for i in range((n*m+n)):
    line = archivo.readline()
    lista = ast.literal_eval(line)
    #print(lista)
    if x == m:
        tmp.append(int(lista))
        matriz.append(tmp)
        tmp = []
        x = -1
    else:
        lista[0] = int(lista[0])
        lista[1] = int(lista[1])
        tmp.append(lista)
    x += 1

i = 0
tmp = []
for i in range(m):
    line = archivo.readline()
    tmp.append(int(line))
matriz.append(tmp)
###########################################

archivo.close()    

lista = [1]
cont = 1
while len(lista) != 0:
    #print("---------------ITERACIÓN",cont,"------------------")
    lista = FindFmp(matriz)

    SearchFlujos(matriz,lista)
    cont+=1
    #print("---------------------------------------------\n\n")
variables = 0
resultado = 0
for i in range(0,filas):
    for j in range (0,columnas):
        if(matriz[i][j][1] != 0):
            variables += 1
            resultado += (matriz[i][j][0]) * (matriz[i][j][1])
            #print("+" + str(matriz[i][j][0])+ "*" +str(matriz[i][j][1]),end = " ")
print("=", resultado)

t1 = time.process_time()
print("Tiempo de ejecucion: " + str(t1 - t0))
print("Cantidad de iteraciones: " + str(cont))
print("Variables usadas: " + str(variables))



