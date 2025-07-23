import streamlit as st
import pandas as pd

caminho_compras = "datasets/compras.csv"

df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",")

st.dataframe(df_compras)