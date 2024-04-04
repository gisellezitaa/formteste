import requests

def enviar_respostas(formulario_url, respostas, quantidade):
    for i in range(quantidade):
        dados_resposta = {}
        for campo, resposta in respostas.items():
            dados_resposta[campo] = resposta
        
        resposta = requests.post(formulario_url, data=dados_resposta)
        
        if resposta.status_code == 200:
            print(f"Resposta {i+1} enviada com sucesso!")
        else:
            print(f"Falha ao enviar resposta {i+1}. Status code: {resposta.status_code}")

# URL do formulário do Google
formulario_url = "https://docs.google.com/forms/d/e/1FAIpQLSf8tqddLZ6J99n3pD8070bPlYJ_GOswOOH7iqgBC9xbwLJxlg/viewform"

# Respostas que você quer enviar
respostas = {
    "entry.1823296986": "leo",
    # Adicione mais campos e respostas conforme necessário
}

# Quantidade de respostas a enviar
quantidade = 10

enviar_respostas(formulario_url, respostas, quantidade)
