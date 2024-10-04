import requests

url = 'https://jsonplaceholder.typicode.com/users'

resp = requests.get(url)
if resp.status_code != 200:
    print(f'Erro: {resp.status_code}')
    exit()

dados = resp.json()

dados_extrair = []

for dado in dados:
    nome = dado['name']
    username = dado['username']
    email = dado['email']
    rua = dado['address']['street']
    numero = dado['address']['suite']

    dados_extrair.append({
            'nome': nome,
            'username': username,
            'email': email,
            'rua': rua,
            'numero': numero
        })
for dado in dados_extrair:
    print(dado)