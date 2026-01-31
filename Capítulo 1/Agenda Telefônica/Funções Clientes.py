import sqlite3
import os

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_do_script, 'agenda.db')


def conectar():
    return sqlite3.connect(caminho_completo)

def inserir_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cliente (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()
    print("Contato salvo com sucesso!")

def listar_contatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Tel: {linha[2]}")
    conn.close()

while True:
    print("\n1. Adicionar Contato | 2. Listar | 0. Sair")
    opcao = input("Escolha: ")
    if opcao == "1": inserir_contato()
    elif opcao == "2": listar_contatos()
    elif opcao == "0": break