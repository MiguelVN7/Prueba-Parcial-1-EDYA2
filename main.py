def solicitar_datos():
    num_palitos = int(input())
    if num_palitos == 0:
        return None, None
    longitudes_palitos = list(map(int, input().split()))
    return num_palitos, longitudes_palitos

def sumar_longitudes(longitudes_palitos):
    return sum(longitudes_palitos)

def ordenar_longitudes(longitudes_palitos):
    return sorted(longitudes_palitos, reverse=True)

def backtracking(indice_actual, es_nueva_varilla, suma_actual, varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
    if suma_actual == longitud_objetivo:
        if varillas_completadas + 1 == total_varillas:
            return True
        return backtracking(0, 1, 0, varillas_completadas + 1, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado)

    if es_nueva_varilla:
        for i in range(num_palitos):
            if not usado[i]:
                usado[i] = True
                if backtracking(i + 1, 0, longitudes_palitos[i], varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
                    return True
                usado[i] = False
                break
    else:
        for i in range(indice_actual, num_palitos):
            if not usado[i] and suma_actual + longitudes_palitos[i] <= longitud_objetivo:
                if i > 0 and longitudes_palitos[i] == longitudes_palitos[i - 1] and not usado[i - 1]: # Evitar duplicados consecutivos, que disminuye mucho el número de combinaciones a probar y el tiempo de ejecución.
                    continue
                usado[i] = True
                if backtracking(i + 1, 0, suma_actual + longitudes_palitos[i], varillas_completadas, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado):
                    return True
                usado[i] = False
                if suma_actual + longitudes_palitos[i] == longitud_objetivo:
                    break
    return False

def main():
    print('Pegue la serie de datos, incluido el 0 al final, y presione Enter:\n')
    primera_entrada = True

    while True:
        num_palitos, longitudes_palitos = solicitar_datos()
        if num_palitos is None:
            print('\n')
            break

        if primera_entrada:
            print('\n')
            primera_entrada = False

        longitud_total = sumar_longitudes(longitudes_palitos)
        longitudes_palitos = ordenar_longitudes(longitudes_palitos)

        solucion_encontrada = False

        for longitud_posible in range(longitudes_palitos[0], longitud_total // 2 + 1):
            if longitud_total % longitud_posible != 0:
                continue
            longitud_objetivo = longitud_posible
            total_varillas = longitud_total // longitud_posible
            usado = [False] * num_palitos

            solucion_encontrada = backtracking(0, 1, 0, 0, longitudes_palitos, longitud_objetivo, total_varillas, num_palitos, usado)
            if solucion_encontrada:
                break

        if not solucion_encontrada:
            longitud_objetivo = longitud_total
        print(longitud_objetivo)

if __name__ == "__main__":
    main()
