#Función para multiplicar cada elemento por 2
def double(arr):
    return [x * 2 for x in arr]

#Función que devuelve el elemento máximo de un arreglo
def maximum(arr):
    if len(arr) == 0:
        return None
    return max(arr)

#Función que devuelve el promedio de los elementos del arreglo
def average(arr):
    if len(arr) == 0:
        return None
    return sum(arr) / len(arr)
