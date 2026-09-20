import streamlit as st
import pandas as pd

st.set_page_config(page_title="Presupuesto Logística", layout="wide")
st.title("Calculadora de Presupuesto Logístico")

# Datos base
inventario = [
    {"Categoría": "Ferretería", "Artículo": "Alicate universal aislado", "Cantidad": 2, "Precio Unitario": 15.0},
    {"Categoría": "Ferretería", "Artículo": "Serrucho de carpintero", "Cantidad": 2, "Precio Unitario": 17.5},
    {"Categoría": "Ferretería", "Artículo": "Pico con mango de fibra", "Cantidad": 1, "Precio Unitario": 35.0},
    {"Categoría": "Ferretería", "Artículo": "Azada forjada con mango", "Cantidad": 2, "Precio Unitario": 22.5},
    {"Categoría": "Ferretería", "Artículo": "Hacha de campamento", "Cantidad": 1, "Precio Unitario": 30.0},
    {"Categoría": "Ferretería", "Artículo": "Bobina cuerda sintética", "Cantidad": 2, "Precio Unitario": 25.0},
    {"Categoría": "Ferretería", "Artículo": "Caja tornillería y clavos", "Cantidad": 3, "Precio Unitario": 11.66},
    {"Categoría": "Fontanería", "Artículo": "Abrazaderas sinfín", "Cantidad": 1, "Precio Unitario": 15.0},
    {"Categoría": "Fontanería", "Artículo": "Racores y tes (1/2\")", "Cantidad": 8, "Precio Unitario": 3.12},
    {"Categoría": "Fontanería", "Artículo": "Grifo esfera macho 1/2\"", "Cantidad": 5, "Precio Unitario": 4.0},
    {"Categoría": "Fontanería", "Artículo": "Teflón / Tangit", "Cantidad": 2, "Precio Unitario": 4.0},
    {"Categoría": "Fontanería", "Artículo": "Calentador gas portátil", "Cantidad": 1, "Precio Unitario": 180.0},
    {"Categoría": "Fontanería", "Artículo": "Alcachofa ducha", "Cantidad": 2, "Precio Unitario": 10.0},
    {"Categoría": "Electricidad", "Artículo": "Enrollacable RV-K", "Cantidad": 2, "Precio Unitario": 80.0},
    {"Categoría": "Electricidad", "Artículo": "Base protectora SAI", "Cantidad": 1, "Precio Unitario": 25.0},
    {"Categoría": "Electricidad", "Artículo": "Tira LED IP65", "Cantidad": 1, "Precio Unitario": 40.0},
    {"Categoría": "Electricidad", "Artículo": "Marquesina generador", "Cantidad": 1, "Precio Unitario": 60.0}
]

df = pd.DataFrame(inventario)

st.sidebar.header("Ajuste de Precios Unitarios")
for index, row in df.iterrows():
    nuevo_precio = st.sidebar.number_input(
        f'{row["Artículo"]} (Cant: {row["Cantidad"]})',
        min_value=0.0,
        value=float(row["Precio Unitario"]),
        step=1.0,
        key=index
    )
    df.at[index, "Precio Unitario"] = nuevo_precio

# Recalcular totales en tiempo real
df["Coste Total"] = df["Cantidad"] * df["Precio Unitario"]
coste_total = df["Coste Total"].sum()

st.dataframe(df.style.format({"Precio Unitario": "{:.2f} €", "Coste Total": "{:.2f} €"}), use_container_width=True)
st.subheader(f"Total Presupuesto Estimado: {coste_total:.2f} €")