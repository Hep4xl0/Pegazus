import requests

url = 'https://jsonplaceholder.typicode.com/users' #define a url da api

#Requisição e verificação da url
resp = requests.get(url)
if resp.status_code != 200:
    print(f'Erro: {resp.status_code}')
    exit()
#Converte a resposta JSON em um dicionário Python
dados = resp.json()

dados_extrair = []

for dado in dados:
    nome = dado['name']#Extrai o nome do usuário
    username = dado['username']#Extrai o nome de usuário
    email = dado['email']#Extrai o e-mail do usuário
    rua = dado['address']['street']#Extrai a rua do endereço
    numero = dado['address']['suite']#Extrai o número (suite) do endereço

    dados_extrair.append({
            'nome': nome,
            'username': username,
            'email': email,
            'rua': rua,
            'numero': numero
        })
for dado in dados_extrair:
    print(dado)