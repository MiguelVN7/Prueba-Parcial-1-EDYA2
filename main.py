def solicitar_datos():
    num_palitos = int(input())  # El usuario ingresa el número de palitos.
    if num_palitos == 0:  # Si se ingresan 0 palitos, termina el programa.
        return None, None
    longitudes_palitos = list(map(int, input().split()))  # El usuario ingresa las longitudes de los palitos y se convierten a enteros y almacenan en una lista.
    return num_palitos, longitudes_palitos

def sumar_longitudes(longitudes_palitos):
    return sum(longitudes_palitos)  # Se suman las longitudes de la lista y se retorna el resultado.

def ordenar_longitudes(longitudes_palitos):
    return sorted(longitudes_palitos, reverse=True)  # Se ordena la lista de las longitudes de mayor a menor y se retorna ordenada.


# Los parámetros de la función backtracking:
# - indice_actual: el índice del palito que se está considerando.
# - es_nueva_varilla: indica si se está comenzando a construir una nueva varilla.
# - suma_actual: la suma de las longitudes de los palitos que se han seleccionado hasta el momento para la varilla actual.
# - varillas_completadas: el número de varillas que se han completado hasta el momento.
# - longitudes_palitos: la lista con las longitudes de los palitos.
# - longitud_objetivo: la longitud que se está tratando de alcanzar con la varilla actual.
# - total_varillas: el número total de varillas que se deben construir.
# - num_palitos: el número total de palitos.
# - usado: una lista que indica si cada palito ha sido seleccionado o no.

def backtracking(indice_actual, es_nueva_varilla, suma_actual, varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
    # Si la suma actual de los palitos es igual a la longitud objetivo, se verifica si se han completado todas las varillas necesarias.
    # Si es así, se devuelve True, indicando que se ha encontrado una solución.
    # Si no, se inicia la construcción de una nueva varilla llamando recursivamente a backtracking con los parámetros actualizados.
    if suma_actual == longitud_objetivo:
        if varillas_completadas + 1 == total_varillas:
            return True
        return backtracking(0, 1, 0, varillas_completadas + 1, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado)


    # Si se está empezando una nueva varilla, se busca el primer palito no utilizado y se marca como usado, continuando la construcción con ese palito.
    # Luego se llama recursivamente a backtracking para continuar construyendo la varilla con ese palito.
    # Si la llamada recursiva devuelve True, se devuelve True para indicar que se ha encontrado una solución.
    # Si no, se desmarca el palito como no utilizado y se continúa con el siguiente palito.
    if es_nueva_varilla:
        i = 0
        while usado[i]:
            i += 1
        usado[i] = True
        if backtracking(i + 1, 0, longitudes_palitos[i], varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
            return True
        usado[i] = False

    # Si no se está empezando una nueva varilla, se intenta agregar palitos a la varilla actual.
    # Se verifica que el palito no haya sido utilizado y que al agregarlo no se exceda la longitud objetivo.
    # Se evitan duplicados consecutivos para reducir el número de combinaciones a probar.
    # Si se logra completar la varilla, se devuelve True. Si no, se desmarca el palito como no utilizado y se prueba con el siguiente.
    else:
        for i in range(indice_actual, num_palitos):
            if not usado[i] and suma_actual + longitudes_palitos[i] <= longitud_objetivo:
                if i > 0 and longitudes_palitos[i] == longitudes_palitos[i - 1] and not usado[i - 1]:
                    continue
                usado[i] = True
                if backtracking(i + 1, 0, suma_actual + longitudes_palitos[i], varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
                    return True
                usado[i] = False
                if suma_actual + longitudes_palitos[i] == longitud_objetivo:
                    break
    return False  # Si no se encuentra una solución, se devuelve False.

def main():
    print('Pegue la serie de datos, incluido el 0 al final, y presione Enter:\n')
    primera_entrada = True

    # Se solicitan los datos y se siguen aceptando hasta que se ingrese 0, caso en el que la función retorna dos None.
    while True:
        num_palitos, longitudes_palitos = solicitar_datos()
        if num_palitos is None:
            print('\n')
            break

        if primera_entrada:
            print('\n')
            primera_entrada = False


        longitud_total = sumar_longitudes(longitudes_palitos)  # Se suman las longitudes de los palitos.
        longitudes_palitos = ordenar_longitudes(longitudes_palitos)  # Se ordenan las longitudes de los palitos de mayor a menor.

        solucion_encontrada = False

        # Se itera sobre todas las longitudes de varillas posibles, desde la del palito más largo hasta la mitad de la longitud total.
        # Se itera hasta ahí porque no es posible construir una varilla más larga que la mitad de la longitud total, ya que se necesitarían menos varillas para completar la longitud total y no se podrían utilizar todos los palitos.
        for longitud_posible in range(longitudes_palitos[0], longitud_total // 2 + 1):
            if longitud_total % longitud_posible != 0:  # Si la longitud total no es divisible por la longitud posible, se continúa con la siguiente longitud posible.
                continue
            longitud_objetivo = longitud_posible  # Se establece la longitud objetivo como la longitud posible, si la longitud total es divisible por la longitud posible.
            total_varillas = longitud_total // longitud_posible  # Se calcula el número total de varillas que se deben construir para alcanzar la longitud total con la longitud posible.
            usado = [False] * num_palitos  # Se inicializa la lista de palitos utilizados como False para todos los palitos, indica que no se ha utilizado ningún palito.

            # Se llama a la función de backtracking con los parámetros adecuados para intentar formar todas las varillas con la longitud objetivo.
            # Si la función devuelve True, significa que se ha encontrado una solución, y se establece solucion_encontrada a True
            solucion_encontrada = backtracking(0, 1, 0, 0, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado)
            if solucion_encontrada:  # Si se encuentra una solución, se rompe el ciclo.
                break

        # Si no se encuentra una solución, la longitud objetivo se establece como la longitud total de todos los palitos, ya que no se pudieron construir varillas con los otros divisores.
        if not solucion_encontrada:
            longitud_objetivo = longitud_total
        print(longitud_objetivo)

if __name__ == "__main__":
    main()

