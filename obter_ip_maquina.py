import socket


def obter_ip():
    # metodo para obter ip da maquina para testes
    try:
        # obtendo ip
        ip = socket.gethostbyname(socket.gethostname())
        print(f"Ip(protocolo de rede) da Maquina : {ip} Teste")
        # retornando o arquivo
        return ip
    except Exception as e:
        print(e)
        return f"<p>Erro '{e}'</p>"
