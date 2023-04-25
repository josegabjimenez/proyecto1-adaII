def accionesVoraz(num_acciones, precio_minimo, num_compradores, compradores):
  restante = num_acciones
  valor=0
  ventaCompradores=[]
  for i in range(num_compradores):
#Este primer if se puede quitar pero no se como quitarle un grado a la identacion
    if restante >= 0:
      if restante >= compradores[i][2]:
        restaMax = restante - compradores[i][1]
#haciendo el condicional de restaMax > 0 hago que la resta en el ultimo caso que es el gobierno comprando todo nunca caiga en el si, pues siempre va a ser negativo o = 0
        if restaMax > 0:
          if restaMax < compradores[i+1][2]:
            posibleCantidad = compradores[i][1]-(compradores[i+1][2]-restaMax)
            factibilidad1 = valor + (compradores[i][0]*compradores[i][1]) + (restaMax*precio_minimo)
            factibilidad2 = valor + (compradores[i][0]*(posibleCantidad))+(compradores[i+1][0]*compradores[i+1][1])
            if factibilidad1 < factibilidad2 :
              valor += compradores[i][0]*(posibleCantidad)
              ventaCompradores.append(posibleCantidad)
              restante -= posibleCantidad
            else:
              valor += compradores[i][0]*compradores[i][1]
              ventaCompradores.append(compradores[i][1])
              restante = restaMax
          else:
            valor += compradores[i][0]*compradores[i][1]
            ventaCompradores.append(compradores[i][1])
            restante = restaMax
        else:
          valor +=compradores[i][0]*restante
          ventaCompradores.append(restante)
          restante -= restante
      else:
        ventaCompradores.append(0)

  return valor, ventaCompradores