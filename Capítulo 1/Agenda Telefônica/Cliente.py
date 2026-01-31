import sqlite3
import streamlit as st
import os

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, 'agenda.db')

# --- INTERFACE DO SITE ---
st.title("Agenda Telefônica - Cap 1 Entendendo Algoritmos")

# Campos de entrada no site
nome = st.text_input("Nome do Contato")
telefone = st.text_input("Telefone")

if st.button("Salvar Contato"):
    if nome and telefone:
        # Conecta e insere
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cliente (nome, telefone) VALUES (?, ?)", (nome, telefone))
        conn.commit()
        conn.close()
        st.success(f"Contato {nome} salvo com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")

# --- MOSTRAR DADOS ---
if st.checkbox("Mostrar todos os contatos"):
    conn = sqlite3.connect(caminho_db)

    import pandas as pd
    df = pd.read_sql_query("SELECT * FROM Cliente", conn)
    st.dataframe(df)
    conn.close()