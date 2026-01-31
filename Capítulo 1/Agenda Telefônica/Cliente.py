import sqlite3

conexao = sqlite3.connect('agenda.db')
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

