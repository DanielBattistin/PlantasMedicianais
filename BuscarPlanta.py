import sqlite3

def buscar_planta():
    termo_busca = input("Digite o termo de busca: ")
    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM plantas
        WHERE nome_popular LIKE ? OR sinonimias LIKE ? OR origem_habitat LIKE ? 
        OR caracteristicas_botanicas LIKE ? OR uso_popular LIKE ? OR mais_informacoes LIKE ? OR fonte LIKE ?
    ''', ('%' + termo_busca + '%', '%' + termo_busca + '%', '%' + termo_busca + '%', '%' + termo_busca + '%', 
          '%' + termo_busca + '%', '%' + termo_busca + '%', '%' + termo_busca + '%'))

    resultados = cursor.fetchall()

    if resultados:
        print("\nResultados da busca:")
        for resultado in resultados:
            print("\nNomes populares:", resultado[1])
            print("\nSinonímias:", resultado[2])
            print("\nOrigem ou Habitat:", resultado[3])
            print("\nCaracterísticas botânicas:", resultado[4])
            print("\nUso popular:", resultado[5])
            print("\nMais informações:", resultado[6])
            print("\nFonte:", resultado[7])            
    else:
        print("Nenhum resultado encontrado.")

    conn.close()
