# Site de referencia para cadastro das plantas 
# https://hortodidatico.ufsc.br/capim-limao/

from CriarTabela import criar_tabela
from InserirPlanta import inserir_planta
from BuscarPlanta import buscar_planta
from ListarPlanta import listar_plantas
from LerQrCode import ler_qrcode
from GerarQrCode import gerar_qrcode
# from BuscarPlantaAPI import buscar_planta_via_api


if __name__ == '__main__':
    criar_tabela()

    while True:
        print("\nMenu:")
        print("1. Inserir planta")
        print("2. Buscar planta")
        print("3. Listar todas as plantas")
        print("4. Gerar QR code")
        # print("5. Ler QR code (câmera)")
        # print("6. Buscar planta (API)")
        print("s. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            inserir_planta()
        elif escolha == '2':
            buscar_planta()
        elif escolha == '3':
            listar_plantas()
        elif escolha == '4':
            identificador = input("Digite o ID ou o nome da planta para gerar o QR code: ")
            gerar_qrcode(identificador)
        # elif escolha == '5':
        #     ler_qrcode()
        # elif escolha == '6':  #revisar este codódo para uma implementação futura.
        #     nome_planta = input("Digite o nome da planta para buscar na API: ")
        #     buscar_planta_via_api(nome_planta)
        elif escolha == 's':
            print("Saindo do programa, até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
