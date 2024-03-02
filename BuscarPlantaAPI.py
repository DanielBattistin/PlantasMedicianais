
#revisar este codódo para uma implementação futura.


import sqlite3
import qrcode
import cv2
import requests

def buscar_planta_via_api(nome_planta):
    api_url = 'http://localhost:5000/buscar_planta'
    params = {'nome_planta': nome_planta}

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            planta_info = response.json()
            exibir_informacoes_planta_api(planta_info)
        elif response.status_code == 404:
            print("Planta não encontrada na API.")
        else:
            print(f"Erro na API: {response.status_code}")
    except Exception as e:
        print(f"Erro na comunicação com a API: {str(e)}")

def exibir_informacoes_planta_api(planta_info):
    print("\nInformações da planta (via API):")
    print("\nNomes populares:", planta_info.get('nome_popular'))
    print("\nSinonímias:", planta_info.get('sinonimias'))
    print("\nOrigem ou Habitat:", planta_info.get('origem_habitat'))
    print("\nCaracterísticas botânicas:", planta_info.get('caracteristicas_botanicas'))
    print("\nUso popular:", planta_info.get('uso_popular'))
    print("\nMais Informações:", planta_info.get('mais_informacoes'))
    print("Fonte:", planta_info.get('fonte'))