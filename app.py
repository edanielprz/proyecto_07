import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="Vehicles EDA", layout="wide")
st.header("Anuncios de venta de autos — EDA rápida con Streamlit")
@st.cache_data
def load_data(path="vehicles_us.csv"):
    return pd.read_csv(path)
df = load_data()
num_cols = df.select_dtypes(include="number").columns.tolist()
st.subheader("Opciones")
col1, col2 = st.columns(2)
with col1:
    build_hist = st.checkbox("Construir histograma")
    hist_col = st.selectbox("Columna (histograma)", options=num_cols)
with col2:
    build_scatter = st.checkbox("Construir dispersión")
    x_col = st.selectbox("Eje X", options=num_cols)
    y_col = st.selectbox("Eje Y", options=num_cols)
if build_hist:
    st.write(f"### Histograma — {hist_col}")
    fig = px.histogram(df, x=hist_col, nbins=30)
    st.plotly_chart(fig, use_container_width=True)
if build_scatter:
    st.write(f"### Dispersión — {x_col} vs {y_col}")
    fig2 = px.scatter(df, x=x_col, y=y_col, opacity=0.6)
    st.plotly_chart(fig2, use_container_width=True)