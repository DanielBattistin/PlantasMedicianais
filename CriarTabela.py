import sqlite3

def criar_tabela():
    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plantas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_popular TEXT,
            sinonimias TEXT,
            origem_habitat TEXT,
            caracteristicas_botanicas TEXT,
            uso_popular TEXT,
            mais_informacoes TEXT,
            fonte TEXT
        )
    ''')

    conn.commit()
    conn.close()