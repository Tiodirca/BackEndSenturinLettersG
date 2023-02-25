from waitress import serve
from chamar_requisicoes_gerar_arquivos import gerarArquivo
from obter_ip_maquina import obter_ip

# pip install Flask
# pip install python-pptx
# pip install waitress
# pyinstaller --windowed main.py

if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    # gerarArquivo.run(host='0.0.0.0', port=port, debug=True)
    print("Necessario está tela estar aberta para "
          "\ngerar e baixar o arquivo criado no programa"
          "\nSenturion Letters G.")

    serve(gerarArquivo, host=obter_ip(), port=5000)
    #gerarArquivo.run(host=obter_ip(), port=5000, debug=True),
