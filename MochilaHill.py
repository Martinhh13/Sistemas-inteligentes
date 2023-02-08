#generador de variables random
import random

# Función evaluar calcula el valor total de los objetos seleccionados y compara si el peso total de estos no supera el peso total máximo
def evaluate(items, knapsack_weight, solution):
    total_value = 0 #inicializamo el valor
    total_weight = 0 #inicializamos peso
    for i in range(len(items)): #seleccion de los objetos
        if solution[i] == 1: # itera sobre la lista "solution" y, para cada elemento de la lista, se comprueba si la solución correspondiente para ese objeto es 1.
            total_value += items[i][0] 
            total_weight += items[i][1]
    if total_weight > knapsack_weight: # si el peso total es mayor que el de la mochila se devuelve una lista con dos valores: 0 y el peso total. 
        return [0, total_weight] 
    else:
        return (total_value, total_weight)
        

# Función vecino: genera una solución vecina a la sol actual,
def generate_neighbor(solution):
    neighbor = solution[:] #  primero crea una copia de la solución dada y la almacena en una nueva lista llamada "neighbor"
    i = random.randint(0, len(solution)-1) # se selecciona un índice al azar en la lista "solution" utilizando la función "random.randint" de la biblioteca "random".
    neighbor[i] = 1 - neighbor[i] # el valor en la posición seleccionada se invierte, cambiando de 0 a 1 o de 1 a 0, y se devuelve la lista "neighbor".
    return neighbor

# Inicializar la solución: inicializa la solucion al azar
def initialize_solution(n):
    return [random.randint(0,1) for i in range(n)]

#Algoritmo de Hill climbing: genera soluciones vecinas, evaluza las puntuaciones y act la sol actual si encuentra una sol vecina mejor.
def hill_climbing(items, knapsack_weight, n_iter):
    current_solution = initialize_solution(len(items))
    current_value, total_weight = evaluate(items, knapsack_weight, current_solution) #obtener la knapsack_weight con cada iteración y la mejor solución presente
    print("El valor actual es: " + str(current_value) +" con peso un peso de: "+str(total_weight))
    for i in range (n_iter):  #  La función "range (n_iter)" genera una secuencia de números enteros desde 0 hasta n_iter-1, y el bucle "for" itera sobre esta secuencia.
        neighbor = generate_neighbor(current_solution) # genera vecino mas cercano a la solucion.
        neighbor_value, total_weight = evaluate(items, knapsack_weight, neighbor) # el valor del vecino y el peso de la mochila seran evaluados a partir de los que ya tenemos.
        if neighbor_value > current_value: # si el calor del vecino es mayor al valor actual
            current_value = neighbor_value # se actualiza el valor actual a la solucion vecina.
            current_solution = neighbor # y empareja la solucion actual con el valor del vecino.
            print("En la iteracion: " + str(i) + " se escogio: "+ str(current_solution) +" con el valor de: "+ str(current_value)+" con un peso de: "+str(total_weight))
    return current_solution, current_value # regresa la solucion actual y el valor actual


# uso con items definidos y peso definido
items = [[4,12],[2,1],[2,2],[1,1],[10,4]]
knapsack_weight = 10
solution, value = hill_climbing(items, knapsack_weight,10)
print("Items seleccionados:", [items[i] for i in range(len(items)) if solution[i] == 1])
print("Valor total:", value) #solucion peso y valor