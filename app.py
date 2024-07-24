import streamlit as st
import mysql.connector
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

conn = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()


st.title('Minha Aplicação com Streamlit')
st.write('Bem-vindo à minha aplicação!')