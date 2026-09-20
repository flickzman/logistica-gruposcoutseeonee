import streamlit as st
import pandas as pd

st.set_page_config(page_title="Presupuesto Logística", layout="wide")
st.title("Calculadora de Presupuesto Logístico")

# Datos base con enlaces a Amazon.es para referencia de precios
inventario = [
    {"Categoría": "Ferretería", "Artículo": "Alicate universal aislado", "Cantidad": 2, "Precio Unitario": 15.0, "URL": "https://www.amazon.es/Alicate-universal-aislado-1000V-180mm/dp/B01ALKP4IQ"},
    {"Categoría": "Ferretería", "Artículo": "Serrucho de carpintero", "Cantidad": 2, "Precio Unitario": 17.5, "URL": "https://www.amazon.es/Bellota-4551-14-Serrucho-carpintero-dentado/dp/B00F2NO1GY"},
    {"Categoría": "Ferretería", "Artículo": "Pico con mango de fibra", "Cantidad": 1, "Precio Unitario": 35.0, "URL": "https://www.amazon.es/DARMAN-Pico-5kg-Mango-Fibra/dp/B07LG8ZJ5S"},
    {"Categoría": "Ferretería", "Artículo": "Azada forjada con mango", "Cantidad": 2, "Precio Unitario": 22.5, "URL": "https://www.amazon.es/Azada-lane-forjada-mango-N-º/dp/B00UY1TBQ4"},
    {"Categoría": "Ferretería", "Artículo": "Hacha de campamento", "Cantidad": 1, "Precio Unitario": 30.0, "URL": "https://www.amazon.es/hacha-camping/s?k=hacha+camping"},
    {"Categoría": "Ferretería", "Artículo": "Bobina cuerda sintética", "Cantidad": 2, "Precio Unitario": 25.0, "URL": "https://www.amazon.es/bobina-cuerda/s?k=bobina+de+cuerda"},
    {"Categoría": "Ferretería", "Artículo": "Caja tornillería y clavos", "Cantidad": 3, "Precio Unitario": 11.66, "URL": "https://www.amazon.es/cajas-tornillos/s?k=cajas+para+tornillos"},
    {"Categoría": "Fontanería", "Artículo": "Abrazaderas sinfín", "Cantidad": 1, "Precio Unitario": 15.0, "URL": "https://www.amazon.es/ABRAZADERA-SINFÍN-25-100-120-mm/dp/B079DT8HQ4"},
    {"Categoría": "Fontanería", "Artículo": "Racores y tes (1/2\")", "Cantidad": 8, "Precio Unitario": 3.12, "URL": "https://www.amazon.es/racor-1-2/s?k=racor+1/2"},
    {"Categoría": "Fontanería", "Artículo": "Grifo esfera macho 1/2\"", "Cantidad": 5, "Precio Unitario": 4.0, "URL": "https://www.amazon.es/Genebre-Valvula-Esfera-2´-305904/dp/B014WL6OVG"},
    {"Categoría": "Fontanería", "Artículo": "Teflón / Tangit", "Cantidad": 2, "Precio Unitario": 4.0, "URL": "https://www.amazon.es/Tangit-2055959-Sellador-Uni-Lock-Blanco/dp/B00VKYY9MU"},
    {"Categoría": "Fontanería", "Artículo": "Calentador gas portátil", "Cantidad": 1, "Precio Unitario": 180.0, "URL": "https://www.amazon.es/Calentador-Camplux-exteriores-propano-regulador/dp/B01CJPU6JI"},
    {"Categoría": "Fontanería", "Artículo": "Alcachofa ducha", "Cantidad": 2, "Precio Unitario": 10.0, "URL": "https://www.amazon.es/alcachofa-ducha/s?k=alcachofa+ducha"},
    {"Categoría": "Electricidad", "Artículo": "Enrollacable RV-K", "Cantidad": 2, "Precio Unitario": 80.0, "URL": "https://www.amazon.es/enrollacable/s?k=enrollacable"},
    {"Categoría": "Electricidad", "Artículo": "Base protectora SAI", "Cantidad": 1, "Precio Unitario": 25.0, "URL": "https://www.amazon.es/sai/s?k=sai"},
    {"Categoría": "Electricidad", "Artículo": "Tira LED IP65", "Cantidad": 1, "Precio Unitario": 40.0, "URL": "https://www.amazon.es/tira-led-ip65/s?k=tira+led+ip65"},
    {"Categoría": "Electricidad", "Artículo": "Marquesina generador", "Cantidad": 1, "Precio Unitario": 60.0, "URL": "https://www.amazon.es/s?k=marquesina+generador"}
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

# Mostrar dataframe con URLs como texto
display_df = df.copy()
# Formatear columnas numéricas
display_df["Precio Unitario"] = display_df["Precio Unitario"].apply(lambda x: f"{x:.2f} €")
display_df["Coste Total"] = display_df["Coste Total"].apply(lambda x: f"{x:.2f} €")
# Mostrar tabla
st.dataframe(display_df[["Categoría", "Artículo", "Cantidad", "Precio Unitario", "Coste Total", "URL"]], use_container_width=True)
st.subheader(f"Total Presupuesto Estimado: {coste_total:.2f} €")
st.caption("Los enlaces URL son referencias de productos en Amazon.es para comparar precios")