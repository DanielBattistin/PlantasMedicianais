import sqlite3
    
def inserir_planta():
    nome_popular = input("Nome Popular: ")
    sinonimias = input("Sinônimias: ")
    origem_habitat = input("Origem ou Habitat: ")
    caracteristicas_botanicas = input("Características Botânicas: ")
    uso_popular = input("Uso Popular: ")
    mais_informacoes = input("Mais Informações: ")
    fonte = input("Fonte: ")

    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO plantas (nome_popular, sinonimias, origem_habitat, caracteristicas_botanicas, uso_popular, mais_informacoes, fonte)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome_popular, sinonimias, origem_habitat, caracteristicas_botanicas, uso_popular, mais_informacoes, fonte))

    # Restante do código para gerar o QR code

    conn.commit()
    conn.close()
