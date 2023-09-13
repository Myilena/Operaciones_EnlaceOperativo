lista = ["lucas daltgo", "soy dalto", True, 1.85]   # Esto es una lista, similar a una matriz
print(lista[0])  # Accedemos al primer elemento de la lista usando corchetes []


tupla = ("lucas daltgo", "soy dalto", True, 1.85)  # Las tuplas son similares a las listas
print(tupla[0])  # Accedemos al primer elemento de la tupla usando corchetes []

# ESTE CONJUNTO TIENE DOS ERRORES NO PUEDE MOSTRAR LOS INDICES Y NO SE PUEDE REPETIR LOS VALORES
conjunto = {"soy dalto", "lucas daltgo", 1.85, True, "soy dalto "} 
#print(conjunto [0])


#ESTO ES UN JSON EN JAVASCRIP Y PYTHON, ADEMAS TIENE LA ESTRUCTURA DE KEY Y VALUE
diccionario = {
        'nombre ' : "soy dalto",
        'apellido ' : "loreto loreto", 
        'les gusta trabajar' : True,
        'altura' : 1.65,  
        'dato duplicado ' : "soy dalto"    
    }
print (diccionario["les gusta trabajar"])
