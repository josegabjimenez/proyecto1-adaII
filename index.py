import streamlit as st
from FuerzaBruta import accionesFB
from ProgramacionVoraz import accionesVoraz
from ProgramacionDinamica import accionesPD
from ProgramacionDinamicaPaquetes import accionesPDP

loading = False

# ALGORITMOS





# PROGRAMACIÓN VORAZ ---------------------------


def main():
    global loading
    print(loading)
    st.title("Proyecto I. Análisis y Diseño de Algoritmos II")

    # Widget para seleccionar el archivo de entrada
    input_file = st.file_uploader("Seleccionar archivo de entrada")
    if input_file is not None:

        es_psub = False
        file_extension = input_file.name.split(".")[-1]
        lines = input_file.readlines()

        if(file_extension == "psub"):
            es_psub = True
        

        max_acciones = int(lines[0].strip())
        min_precio_acciones = int(lines[1].strip())
        compradores = int(lines[2].strip())
        ofertas = []

        # Verifica que sea una entrada de programación dinámica con paquetes
        if(es_psub):
            acciones_paquete = int(lines[len(lines)-1].strip())
            

        for i in range(3, len(lines) - 1):
            # print("PALABRA:",lines[i], "\n")
            oferta = lines[i].decode('utf-8')
            oferta_arr = oferta.split(',')
            array_numeros = [int(x) for x in oferta_arr]
            ofertas.append(array_numeros)

        print('max_acciones : ', max_acciones)
        print('min_acciones : ', min_precio_acciones)
        print('compradores : ', compradores)
        print("ofertas : ",ofertas)
        # print("acciones por paquete : ", acciones_paquete)
        print('')

        tipo_algoritmo = st.radio("Elige un enfoque para resolver el problema",
                         ('Fuerza Bruta', 'Programación Voraz', 'Programación Dinámica', 'Programación Dinámica con Paquetes'))

        generar_solucion = st.button("Generar solución")
        
        if (generar_solucion):
            if (tipo_algoritmo == "Fuerza Bruta"):
                resultado, acciones_vendidas = accionesFB(max_acciones, min_precio_acciones, compradores, ofertas)

            if (tipo_algoritmo == "Programación Voraz"):
                resultado, acciones_vendidas = accionesVoraz(max_acciones, min_precio_acciones, compradores, ofertas)

            if (tipo_algoritmo == "Programación Dinámica"):
                resultado, acciones_vendidas = accionesPD(max_acciones, min_precio_acciones, compradores, ofertas)
            
            if (tipo_algoritmo == "Programación Dinámica con Paquetes"):
                if(not es_psub):
                    st.write("Este archivo no indica el número de acciones por paquete")
                else:
                    resultado, acciones_vendidas = accionesPDP(max_acciones, min_precio_acciones, compradores, ofertas, acciones_paquete)
            
            # Mostrar los resultados
            st.write(f"La máxima ganancia posible es: {resultado}")
            st.write(f"Acciones por comprador: {acciones_vendidas}")


        # Llamar a la función 
        

        if(loading):
            st.write("Cargando...")

  
        # for i, a in enumerate(acciones_vendidas):
        #     st.write(f"El comprador {i+1} compró {a} acciones")

if __name__ == "__main__":
    main()
