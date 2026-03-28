import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Mi Mini Proyecto Python", page_icon="🚀")

st.title("📊 Analizador de Texto Express")
st.write("Introduce un texto abajo para analizar sus estadísticas en tiempo real.")

# Área de entrada de texto
user_input = st.text_area("Escribe algo interesante aquí:", "Hola mundo, esto es una prueba con Python y Streamlit.")

if user_input:
    # Lógica de procesamiento
    words = user_input.split()
    word_count = len(words)
    char_count = len(user_input)
    distinct_words = len(set(words))

    # Métricas en columnas
    col1, col2, col3 = st.columns(3)
    col1.metric("Palabras totales", word_count)
    col2.metric("Caracteres", char_count)
    col3.metric("Palabras únicas", distinct_words)

    # Crear un pequeño DataFrame para visualizar la frecuencia (Top 5 palabras)
    if word_count > 0:
        word_freq = pd.Series(words).value_count_counts().head(5)
        st.subheader("Frecuencia de palabras (Top 5)")
        st.bar_chart(word_freq)
else:
    st.warning("¡Escribe algo para ver la magia!")

st.sidebar.info("Hecho con ❤️ usando Streamlit y Python.")
