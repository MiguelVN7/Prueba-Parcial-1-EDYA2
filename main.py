# Este resuelve todos los casos...
def separar_longitudes(longitudes):
    longitudes_separadas = longitudes.split(' ')
    longitudes_separadas = [x for x in longitudes_separadas if x]
    longitudes_separadas = list(map(int, longitudes_separadas))
    longitudes_separadas.sort(reverse=True)
    return longitudes_separadas

def sumar_longitudes(longitudes_separadas):
    return sum(longitudes_separadas)

def encontrar_divisores(suma, mayor):
    return [i for i in range(mayor, suma + 1) if suma % i == 0]

def encontrar_longitud_mayor(longitudes_separadas):
    return max(longitudes_separadas)


def encontrar_longitud_palito(longitudes_separadas, divisores):
    longitudes_separadas.sort(reverse=True)  # Ordena las longitudes de mayor a menor
    n = len(longitudes_separadas)  # Número de palitos
    total_longitud = sum(longitudes_separadas)  # Suma de las longitudes de los palitos

    def backtrack(objetivo, longitudes, usados, suma_actual, indice_actual, varillas_completadas):
        if varillas_completadas == total_longitud // objetivo:  # Se han formado todas las varillas requeridas (que son total_longitud // objetivo)
            return True
        if suma_actual == objetivo:  # Si la suma actual es igual al objetivo, se forma una varilla completa y se continúa con la siguiente
            return backtrack(objetivo, longitudes, usados, 0, 0, varillas_completadas + 1)

        for i in range(indice_actual, n):  # Este ciclo itera sobre las longitudes de los palitos que no han sido usados para formar la siguiente varilla
            if not usados[i] and suma_actual + longitudes[i] <= objetivo:  # Si la longitud no ha sido usada y al sumarla a la suma actual no excede el objetivo, se intenta usar
                if i > 0 and longitudes[i] == longitudes[i - 1] and not usados[i - 1]:  # Si la longitud es igual a la anterior y la anterior no ha sido usada, se salta para evitar duplicados
                    continue
                usados[i] = True  # Marca la longitud como usada
                if backtrack(objetivo, longitudes, usados, suma_actual + longitudes[i], i + 1, varillas_completadas):  # Se llama recursivamente con la longitud actual sumada a la suma actual y el índice actual incrementado en 1
                    return True
                usados[i] = False  # Desmarca la longitud como usada si no se logra formar una varilla con ella
                if suma_actual == 0 or suma_actual + longitudes[i] == objetivo:  # Si la suma actual es 0 o la suma actual más la longitud actual es igual al objetivo, no se podrán formar varillas con la longitud actual
                    break
        return False

    for divisor in divisores:  # Itera sobre los divisores de la suma de las longitudes
        if total_longitud % divisor == 0:  # Solo considera divisores que permitan formar varillas completas
            usados = [False] * n  # Arreglo que indica si una longitud ha sido usada
            if backtrack(divisor, longitudes_separadas, usados, 0, 0, 0):  # Llama a la función backtrack con el divisor actual como objetivo y las longitudes de los palitos como argumentos
                return divisor  # Si se logra formar todas las varillas completas, se retorna el divisor actual
    return total_longitud  # Si no se logra formar todas las varillas completas, se retorna la suma de las longitudes de los palitos


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
        mayor = encontrar_longitud_mayor(longitudes_separadas)
        lista_divisores = encontrar_divisores(suma, mayor)
        longitud_minima = encontrar_longitud_palito(longitudes_separadas, lista_divisores)
        print(longitud_minima)

if __name__ == "__main__":
    main()