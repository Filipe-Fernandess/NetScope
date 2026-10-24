import socket

def menu_selection():
    print(f"""
{"=" * 21}
{" " * 3}NetScope V.01
{"=" * 21}

Bem vindo(a) ao NetScope V.01!
Escolha uma opção:""")
    while True:
        print("""
Menu:
    [0] Sair
    [1] Informações do dispositivo (host e Ip)
        """)
        option = input("Digite 0 ou 1: ")

        if option == 1:
            device_info()

        elif option == 0:
            print("Exiting of NetScope...")
            break

        else:
            print("PARÂMETRO INVÁLIDO! Tente novamente.")



def device_info():
    
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    print(f"""
{"-_-" * 9}

INFORMAÇÕES DO DISPOSITIVO:

- Nome do dispositivo: {host}
- IP: {ip}
{"_-_" * 9}

    """)


menu_selection()