"""
El siguiente script responde al siguiente problema:


Una máquina arranca su tarea imprimiendo los números 2023, 2024 y 2025. 
Luego, sin interrupción, sigue imprimiendo la suma de los últimos tres 
números que ha impreso: 6072, 10121, 18218, y así sucesivamente. 
¿Serías capaz de determinar cuáles son los cuatro dígitos finales del
número impreso en la posición 2.023.202.320.232.023? 

Como referencia, en la posición 50, el número impreso es 8188013234823360, 
que finaliza en 3360.
"""


##  Importamos las librerías necesarias
from collections import deque
from itertools import count
import sys, time, pickle


# Increase the limit for integer string conversion
sys.set_int_max_str_digits(1000000)




##  Funciones
def last_4_digits(q):
    return str(sum(q))[-4:]


##  =================== MAIN ===================  ##
if __name__ == '__main__':

    ##  Parámetros de configuración
    maxsize = 3
    startvalue = 2023
    start_position = count(1)
    end_position = 2023
    # end_position = 50
    start_time = time.time()

    ##  Variables operativas
    q = deque(maxlen=maxsize)
    counter = count(startvalue)

    ##  Bucle de procesamiento
    for i in range(maxsize):
        q.append(next(counter))
        position = next(start_position)
    
    next(start_position)
    while position < end_position:
        position = next(start_position)
        q.append(sum(q))

    ##  Tiempo de ejecución
    end_time = time.time()
    execution_time = end_time - start_time
    
    ##  Guardamos los resultados del procesamiento
    results = {
        'position': position,
        'final_deque': q,
        'excetion_time': execution_time
    }

    with open('results.pickle', 'wb') as f:
        pickle.dump(results, f)


    ##  Resultados del problema
    results.update({'last_4_digits': last_4_digits(q)})

    with open('results.txt', 'w') as f:
        print(results, file=f)

    print(f"Número de posición actual: {position}")
    # print(f"Últimos tres dígitos: {list(q)}")
    # print(f"Suma de los últimos tres dígitos: {sum_last_3_digits(q)}")
    print(f"Últimos cuatro dígitos: {last_4_digits(q)}")
    print()

        

        