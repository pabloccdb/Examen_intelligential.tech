
#Se piden la cantidad de Columnas y Filas para generar una matriz
N=int(input('introduce la cantidad de Columnas: '))
M=int(input('introduce la cantidad de Filas: '))
matrix = [[0 for x in range(N)] for y in range(M)] 

#Llenamos la matriz o el arreglo bidimensional 
contador=1
for a in range(M):
    for b in range(N):
           matrix[a][b]=contador
           contador+=1
print("Asi se muestra la matriz de entrada: ")
print(matrix)
        
#Variable para podernos mover hacia los lados
direccion=0 
#Un punto de inicio, de donde voy a empezar a recorrer
inicio=0
#Valor incremental
valor=1 
#Variable para posicionarme 
siguiente=0 
#Filas para reducir las paredes
y=len(matrix) 
 #Columnas para reducir las paredes
x=len(matrix[y-1])
#Multiplicacion
n=y*x 

#Arreglo Final donde se guardara el resultado
Caracol = [0 for x in range(n)]
ContCaracol=0

while valor<=n:
    #En Caso que vaya para la derecha
    if direccion==0 and valor<=n:
        Caracol[ContCaracol]=matrix[inicio][siguiente]
        matrix[inicio][siguiente]=valor
        valor+=1
        siguiente+=1
        ContCaracol+=1
        if siguiente==x:
            direccion=1
            siguiente=inicio+1
    #En caso que vaya hacia abajo
    if direccion==1 and valor<=n:
        Caracol[ContCaracol]=matrix[siguiente][x-1]
        matrix[siguiente][x-1]=valor
        valor+=1
        siguiente+=1
        ContCaracol+=1
        if siguiente == y:
            direccion=2
            siguiente=x-2  
    #En caso que vaya hacia atras
    if direccion==2 and valor<=n:
       Caracol[ContCaracol]=matrix[y-1][siguiente]
       matrix[y-1][siguiente]=valor
       valor+=1
       siguiente-=1
       ContCaracol+=1
       if siguiente==inicio-1:
            direccion=3
            siguiente=y-2
    #En caso que vaya hacia arriba
    if direccion==3 and valor<=n:
        Caracol[ContCaracol]=matrix[siguiente][inicio]
        matrix[siguiente][inicio]=valor
        valor+=1
        siguiente-=1
        ContCaracol+=1
        if siguiente==inicio:
            direccion=0
            x-=1
            y-=1
            inicio+=1
            siguiente=inicio
print("Arreglo Final :")
print(Caracol)
input("Press any key to continue")