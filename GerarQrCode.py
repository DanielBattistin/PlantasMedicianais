import sqlite3
import qrcode
import cv2

def gerar_qrcode(identificador):
    conn = sqlite3.connect('local_database.db')
    cursor = conn.cursor()

    if isinstance(identificador, int):  # Se o identificador for um número, assume-se que é o ID
        cursor.execute('SELECT * FROM plantas WHERE id = ?', (identificador,))
    else:  # Se não for um número, assume-se que é o nome da planta
        cursor.execute('SELECT * FROM plantas WHERE nome_popular LIKE ?', ('%' + identificador + '%',))

    planta = cursor.fetchone()

    if planta:
        qr_code_data = (
            f"Nome Popular: {planta[1]}\n"
            f"Sinonímias: {planta[2]}\n"
            f"Origem ou Habitat: {planta[3]}\n"
            f"Características Botânicas: {planta[4]}\n"
            f"Uso Popular: {planta[5]}\n"
            f"Mais informações: {planta[6]}\n"
            f"Fonte: {planta[7]}"
            )
        nome_arquivo_qr = f"qrcode_planta_{planta[0]}.png"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(qr_code_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nome_arquivo_qr)

        print(f"QR code gerado e salvo como: {nome_arquivo_qr}")
    else:
        print("Planta não encontrada.")

    conn.close()