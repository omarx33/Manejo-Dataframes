import streamlit as st
import pandas as pd


st.title("Manejo de Dataframes")
st.sidebar.title("Parámetro")

modulo = st.sidebar.selectbox("Seleccione un Modulo", ["Filtros","Consultas","Agrupaciones","Muestras"])
df = pd.read_csv("Datos/ds_salaries.csv")
if modulo == "Filtros":

   
    st.write(df) #mostrar los datos 1

    st.write("Columnas del Dataframe", df.columns) #mostrar los datos 2

    lista_columnas = list(df.columns)

    seleccion_columnas = st.multiselect("Seleccione columnas", lista_columnas)

    st.write(seleccion_columnas)

    ingreso_indice = st.number_input("Ingrese el valor de indice")

    df_filtro_1 = df.loc[int(ingreso_indice),seleccion_columnas]
    st.write(df_filtro_1)

    indice_columna=st.number_input("Ingrese indice")

    indice_fila= st.number_input("Ingrese el indice de la fila")

    df_filtro_2 = df.iloc[int(indice_fila),int(indice_columna)]

    st.write(df_filtro_2)
elif modulo == "Consultas":

    consultas= st.text_input("Ingrese query")



    try:
        
      df_query = df.query(consulta)
      st.write(df_query)
    except:  
      st.write("Ingrese el query y presione ENTER") 

       
    consulta_coincidencia = st.text_input("Ingrese el query y ponga enter")
    seleccion_columnas=st.selectbox("Escoja una columna", list(df.columns))

    try:
       df_coincidencia=df[df[seleccion_columnas].str.contains(consulta_coincidencia)]
       st.write(df_coincidencia)
    except:
        st.write("Ingrese la coincidencia")    

elif modulo == "Agrupaciones":       

        lista_columnas = list(df.columns)
        seleccion_columnas = st.multiselect("Seleccione columnas", lista_columnas)
        columna_cuantitativa = st.selectbox("Seleccione una columna cuantitativa", lista_columnas)

        df_agrupacion_promedio = df.groupby(seleccion_columnas)[columna_cuantitativa].mean()
        st.write(df_agrupacion_promedio)

elif modulo == "Muestras":
    muestra_aleatoria = df.sample(n=int(st.number_input("Ingrese un valor")), random_state=42)
    st.write(muestra_aleatoria)

    muestra_aleatoria_2 = df.sample(frac=float(st.number_input("Ingrese una fracción")), random_state=42)
    st.write(muestra_aleatoria_2)