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

#Función principal para probar las funciones anteriores
def main():
    listas = [
        [1, 2, 3, 4, 5],
        [10, 5, 8, 3],
        [7]
    ]

    for lista in listas:
        print("Lista:", lista)
        print("Double:", double(lista))
        print("Maximum:", maximum(lista))
        print("Average:", average(lista))
        print("-" * 30)


if __name__ == "__main__":
    main()