##Se tienen los datos de un grupo de 5 transacciones referentes a las matrículas de un grupo de estudiantes (código, apellidos, nombres, créditos), almacenadas como txt, crear un arreglo con estas transacciones y a partir del mismo, calcular cuántos estudiantes y su número de créditos matriculados, tienen un mayor número de créditos matriculados que el promedio de todos los estudiantes; generando esta respuesta en una tupla.

#importar diccionario
matriculas={}
with open("matriculas.txt", "r") as f:
    x = f.readlines()
    for i in x:
        lista1=i.split(":")
        lista1[1]=lista1[1].replace("\n","")
        lista2=lista1[1].split(",")
        matriculas.setdefault(lista1[0],lista2)

f.close()

##calcular promedio de creditos
promedio=0
suma=0
for key in matriculas:
    creditos=int(matriculas[key][2])
    suma=suma+creditos

promedio=suma/len(matriculas)

##compara los credito por encima del promedio
tupla=()
contador=0
for key in matriculas:
    creditos=int(matriculas[key][2])
    if creditos>promedio:
        contador=contador+1

        
#generar tuplaa
tupla=(str(contador))

for key in matriculas:
    creditos=int(matriculas[key][2])
    if creditos>promedio:
        tupla=tupla+","+str(creditos)
        
print(tupla)