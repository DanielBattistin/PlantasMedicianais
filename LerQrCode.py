import sqlite3
import qrcode
import cv2

def ler_qrcode():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        qr_code_reader = cv2.QRCodeDetector()
        data, vertices, qr_code = qr_code_reader.detectAndDecode(frame)

        # print("Data:", data)  # Adicione esta linha para depurar

        if data:
            nome_popular = data.strip()
            if nome_popular:
                exibir_informacoes_planta(nome_popular)
                break

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def exibir_informacoes_planta(nome_popular):
    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM plantas WHERE nome_popular LIKE ?', ('%' + nome_popular + '%',))
    planta = cursor.fetchone()

    if planta:
        print("\nInformações da planta:")
        print("\nNomes populares:", planta[1])
        print("\nSinonímias:", planta[2])
        print("\nOrigem ou Habitat:", planta[3])
        print("\nCaracterísticas botânicas:", planta[4])
        print("\nUso popular:", planta[5])
        print("\nMais informações:", planta[6])
        print("\nFonte:", planta[7])
    else:
        print(f"Planta com o nome popular '{nome_popular}' não encontrada.")

    conn.close()  