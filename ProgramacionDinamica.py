def accionesPD1(num_acciones, precio_minimo, num_compradores, compradores):

    #Verificar que la entrada tenga al gobierno al final, sino, se añade
    if(num_compradores != len(compradores)):
        compradores.append([precio_minimo, num_acciones, 0])

    # Inicializar una matriz para almacenar la máxima ganancia para cada comprador y número de acciones vendidas
    matriz_ganancias = [[0] * (num_acciones + 1) for _ in range(num_compradores + 1)]
    print("DINAMICA COMPRADORES:" ,len(compradores))
    # Rellenar la primera columna de la matriz con la ganancia que se puede obtener vendiendo 0 acciones
    for i in range(num_compradores + 1):
        matriz_ganancias[i][0] = 0

    # Rellenar la primera fila de la matriz con la ganancia que se puede obtener vendiendo 1 a num_acciones acciones
    for j in range(1, num_acciones + 1):
        matriz_ganancias[0][j] = precio_minimo * j

    # Rellenar el resto de la matriz utilizando programación dinámica
    for i in range(1, num_compradores + 1):
        for j in range(1, num_acciones + 1):
            max_ganancia = matriz_ganancias[i - 1][j]  # Empezar con la máxima ganancia de no venderle al comprador actual
            for k in range(max(1, compradores[i - 1][2]), min(compradores[i - 1][1], j) + 1):
                # Calcular la ganancia de venderle k acciones al comprador actual
                ganancia = compradores[i - 1][0] * k + matriz_ganancias[i - 1][j - k]
                # Actualizar la máxima ganancia para venderle j acciones al comprador actual y a todos los compradores anteriores
                max_ganancia = max(max_ganancia, ganancia)
            matriz_ganancias[i][j] = max_ganancia

    # Determinar qué acciones se vendieron a cada comprador para lograr la máxima ganancia
    acciones_vendidas = [0] * num_compradores
    num_acciones_vendidas = num_acciones
    for i in range(num_compradores, 0, -1):
        for j in range(max(1, compradores[i - 1][2]), min(compradores[i - 1][1], num_acciones_vendidas) + 1):
            # Calcular la ganancia de venderle j acciones al comprador actual
            ganancia = compradores[i - 1][0] * j + matriz_ganancias[i - 1][num_acciones_vendidas - j]
            if matriz_ganancias[i][num_acciones_vendidas] == ganancia:
                acciones_vendidas[i - 1] = j
                num_acciones_vendidas -= j
                break

    # Si hay acciones sobrantes, se le asignan al gobierno
    if (num_acciones_vendidas > 0):
      acciones_vendidas[num_compradores - 1] = num_acciones_vendidas + 1 

    # Devolver la máxima ganancia y las acciones vendidas a cada comprador
    return matriz_ganancias[num_compradores][num_acciones], acciones_vendidas