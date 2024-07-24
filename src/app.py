import streamlit as st
import pandas as pd
from pages import home, organizacoes, iniciativas
from data import database

conn = database.get_connection()
cursor = conn.cursor()

st.sidebar.title('Menu')
selection = st.sidebar.radio('Ir para', ['Geral', 'Organizações', 'Iniciativas'])

if selection == 'Geral':
    home.show()
elif selection == 'Organizações':
    organizacoes.show()
elif selection == 'Iniciativas':
    iniciativas.show()