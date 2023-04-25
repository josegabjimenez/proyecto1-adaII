# FUERZA BRUTA ---------------------------
def obtener_combinaciones(ofertas, acciones_disponibles):
    
    """
    Función que genera todas las posibles combinaciones de compras que satisfacen las restricciones de cada comprador,
    donde cada comprador solo puede llevar un número fijo de acciones.
    """
    resultados = []
    n = len(ofertas)
    
    # Caso base: si ya se han considerado todos los compradores, se devuelve una lista vacía
    if n == 0:
        return [[]]

    if n == 1:
        return [[acciones_disponibles]]
    
    # Se generan todas las posibles compras que puede hacer el comprador actual
    posibles_acciones = [0, ofertas[0][1]]
    
    # Se itera sobre todas las posibles compras del comprador actual
    for i in range(len(posibles_acciones)):
        if posibles_acciones[i] <= acciones_disponibles:
            # Se llama a la función recursivamente para los demás compradores y se actualiza la cantidad de acciones disponibles
            acciones_restantes = acciones_disponibles - posibles_acciones[i]
            compradores_restantes = obtener_combinaciones(ofertas[1:], acciones_restantes)
            
            # Se combinan todas las posibles compras del comprador actual con todas las posibles compras de los demás compradores
            for j in range(len(compradores_restantes)):
                resultado = [posibles_acciones[i]] + compradores_restantes[j]
                resultados.append(resultado)
    
    return resultados

def accionesFB(num_acciones, min_precio_acciones, num_compradores, compradores):

    #Verificar que la entrada tenga al gobierno al final, sino, se añade
    if(num_compradores != len(compradores)):
        compradores.append([min_precio_acciones, num_acciones, 0])

    # Obtener todas las posibles combinaciones
    combinaciones = obtener_combinaciones(compradores, num_acciones)

    valores = []

    # Se calcula el valor monetario que genera cada combinación
    for i in range(len(combinaciones)):
        acum = 0
        for j in range(len(compradores)):
            acum += combinaciones[i][j] * compradores[j][0]
        valores.append(acum)

    # Se toma la combinación que genera más dinero
    valor_max = max(valores);
    # print("estos son valores",valores)

    # Retornamos la mayor ganancia y las acciones a cada comprador que generan esa mayor ganancia
    return valor_max, combinaciones[valores.index(valor_max)]


