import streamlit as st
import pandas as pd
import spacy
import sqlite3
import pyodbc


st.title('PLATAFORMA DE VALIDACION👈')

st.write("______________________________________")


st.header(" DEVOLUCIONES🤑")
read= pd.read_excel(r'C:/Users/manitas/Desktop/DEVOLUCION.xlsx')
st.dataframe(read)




st.write("______________________________________")


st.header(" LACTASALES🥛")

read= pd.read_excel(r'C:/Users/manitas/Desktop/LACTASALES.xlsx')
st.dataframe(read)
