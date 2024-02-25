#Con este no me dan discrepancias pero se demora mucho en ejecutar

def separar_longitudes(longitudes):
    longitudes_separadas = longitudes.split(' ')
    longitudes_separadas = [x for x in longitudes_separadas if x]
    longitudes_separadas = list(map(int, longitudes_separadas))
    longitudes_separadas.sort(reverse=True)
    return longitudes_separadas

def sumar_longitudes(longitudes_separadas):
    suma = 0
    for longitud in longitudes_separadas:
        suma += longitud
    return suma

def encontrar_divisores(suma):
    lista_divisores = []
    for i in range(1, suma + 1):
        if suma % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def encontrar_longitud_mayor(longitudes_separadas):
    mayor = max(longitudes_separadas)
    return mayor

def seleccionar_divisores_validos(lista_divisores, mayor):
    divisores_validos = []
    for divisor in lista_divisores:
        if (divisor >= mayor):
            divisores_validos.append(divisor)
    return divisores_validos

def encontrar_longitud_palito(longitudes_separadas, divisores, suma_total):
    def backtrack(objetivo, longitudes, usados, suma_actual):
        if suma_actual == objetivo:
            if all(usados):
                return True
            else:
                return backtrack(objetivo, longitudes, usados, 0)
        if suma_actual > objetivo:
            return False
        for i in range(len(longitudes)):
            if not usados[i]:
                if suma_actual + longitudes[i] <= objetivo:
                    usados[i] = True
                    if backtrack(objetivo, longitudes, usados, suma_actual + longitudes[i]):
                        return True
                    usados[i] = False
                else:
                    # Poda temprana: si la longitud actual más la suma actual
                    # supera el objetivo, no es necesario explorar las
                    # longitudes restantes.
                    break
        return False

    long_max = max(longitudes_separadas)
    for divisor in sorted(divisores):
        if divisor >= long_max and suma_total % divisor == 0:
            usados = [False] * len(longitudes_separadas)
            if backtrack(divisor, longitudes_separadas, usados, 0):
                return divisor
    return None



def main():
    print('Pegue la serie de datos, incluido el 0 al final, y presione Enter:\n')
    entradas = []
    while True:
        entrada = input()
        if entrada.strip() == '0':
            entradas.append(entrada.strip())
            break
        entradas.extend(entrada.strip().split('\n'))

    for i in range(0, len(entradas), 2):
        palitos_cortados = int(entradas[i])
        if palitos_cortados == 0:
            break
        longitudes = entradas[i + 1]

        longitudes_separadas = separar_longitudes(longitudes)
        suma = sumar_longitudes(longitudes_separadas)
        lista_divisores = encontrar_divisores(suma)
        mayor = encontrar_longitud_mayor(longitudes_separadas)
        divisores_validos = seleccionar_divisores_validos(lista_divisores, mayor)
        longitud_minima = encontrar_longitud_palito(longitudes_separadas, divisores_validos, suma)
        print(longitud_minima)

if __name__ == "__main__":
    main()
