import sqlite3

def listar_plantas():
    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM plantas')
    plantas = cursor.fetchall()

    if plantas:
        print("\nLista de todas as plantas cadastradas:")
        for planta in plantas:
            print("Plantas cadastradas:", planta[1])
            # print("\nNomes populares:", planta[1])
            # print("\nSinonímias:", planta[2])
            # print("\nOrigem ou Habitat:", planta[3])
            # print("\nCaracterísticas botânicas:", planta[4])
            # print("\nUso popular:", planta[5])
            # print("\nMais informações:", planta[6])
            # print("\nFonte:", planta[7])
    else:
        print("Nenhuma planta cadastrada.")

    conn.close()