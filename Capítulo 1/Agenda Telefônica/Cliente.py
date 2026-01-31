import sqlite3
import os

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_do_script, 'agenda.db')

conexao = sqlite3.connect(caminho_completo)
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cliente (
        cd_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
''')

print("Banco de dados e tabela criados com sucesso!")
conexao.commit()
conexao.close()

