import requests

url = 'https://jsonplaceholder.typicode.com/todos' #define a url da api

#Requisição e verificação da url
resp = requests.get(url)
if resp.status_code != 200:
    print(f'Erro: {resp.status_code}')
    exit()
#Converte a resposta json em um dicionario
tarefas = resp.json()
#Inicializa contador das tarefas
tarefas_completadas = 0
tarefas_incompletas = 0
#verifica se cada tarefa esta completa ou incompleta e baseado nisso soma a uma das variaveis
for tarefa in tarefas:
    if tarefa['completed'] == True:
        tarefas_completadas += 1
    elif tarefa['completed'] == False:
        tarefas_incompletas += 1

print(f'{tarefas_incompletas}, {tarefas_completadas}')