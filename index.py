import os
import streamlit as st
from FuerzaBruta import accionesFB
from ProgramacionVoraz import accionesV
from ProgramacionDinamica import accionesPD1
from ProgramacionDinamicaPaquetes import accionesPD2

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

        st.write(f"Número de acciones: {max_acciones}")
        st.write(f"Precio mínimo por accion: {min_precio_acciones}")
        st.write(f"Número de compradores: {compradores}")
        st.write(f"Ofertas de cada comprador: {ofertas}")

        if(es_psub):
            st.write(f"Acciones por paquete: {acciones_paquete}")

        tipo_algoritmo = st.radio("Elige un enfoque para resolver el problema",
                         ('Fuerza Bruta', 'Programación Voraz', 'Programación Dinámica', 'Programación Dinámica con Paquetes'))

        generar_solucion = st.button("Generar solución")
        
        if (generar_solucion):
            if (tipo_algoritmo == "Fuerza Bruta"):
                resultado, acciones_vendidas = accionesFB(max_acciones, min_precio_acciones, compradores, ofertas)

            if (tipo_algoritmo == "Programación Voraz"):
                resultado, acciones_vendidas = accionesV(max_acciones, min_precio_acciones, compradores, ofertas)

            if (tipo_algoritmo == "Programación Dinámica"):
                resultado, acciones_vendidas = accionesPD1(max_acciones, min_precio_acciones, compradores, ofertas)
            
            if (tipo_algoritmo == "Programación Dinámica con Paquetes"):
                if(not es_psub):
                    st.write("Este archivo no indica el número de acciones por paquete")
                else:
                    resultado, acciones_vendidas = accionesPD2(max_acciones, min_precio_acciones, compradores, ofertas, acciones_paquete)
            
            # Mostrar los resultados
            st.write(f"La máxima ganancia posible es: {resultado}")
            st.write(f"Acciones por comprador: {acciones_vendidas}")

            # Lógica para crear archivo de salida
            path = "./salidas/"
            filename = "resultado.txt"
            contador = 1

            # Verifica que no exista un archivo de salida con el mismo nombre
            while os.path.exists(path + filename):
                filename = "resultado_" + str(contador) + ".txt"
                contador += 1

            # Crea el archivo de salida con los resultados
            with open(path + filename, "w") as f:
                f.write(f"{resultado}\n")
                for accion in acciones_vendidas:
                    f.write(f"{accion}\n")

            with open(filename, 'rb') as f:
                file_contents = f.read()

            # # Crear un botón de descarga
            # download_button = st.download_button(
            #     label="Descargar solución",
            #     data=file_contents,
            #     file_name=filename
            # )
        

        # if(loading):
        #     st.write("Cargando...")

if __name__ == "__main__":
    main()
