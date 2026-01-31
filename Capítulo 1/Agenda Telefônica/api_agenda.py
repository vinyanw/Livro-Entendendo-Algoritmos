from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()
DB_PATH = os.path.join(os.path.dirname(__file__), "agenda.db")

@app.get("/contatos")
def lista_contatos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    contatos = cursor.fetchall()
    conn.close()

    return [{"id": c[0], "nome": c[1], "telefone": c[2]} for c in contatos]

@app.post("/adicionar")
def adicionar_contato(nome: str, telefone: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cliente (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()
    return {"status": "sucesso", "mensagem": f"Contato {nome} adicionado"}

@app.get("/")
def home():
    return {"mensagem": "API da Agenda está online! Vá para /docs para testar."}
    