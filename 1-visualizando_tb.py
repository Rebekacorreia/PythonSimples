import streamlit as st
import pandas as pd

st.title("Visualização da Tabela de Compras")

caminho_compras = "datasets/compras.csv"

# Tenta carregar o CSV
try:
    df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",")
    st.dataframe(df_compras)
except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {caminho_compras}")
except Exception as e:
    st.error(f"Ocorreu um erro: {e}")
