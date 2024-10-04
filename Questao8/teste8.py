import requests

url = 'https://jsonplaceholder.typicode.com/todos'

resp = requests.get(url)
if resp.status_code != 200:
    print(f'Erro: {resp.status_code}')
    exit()
tarefas = resp.json()

tarefas_completadas = 0
tarefas_incompletas = 0

for tarefa in tarefas:
    if tarefa['completed'] == True:
        tarefas_completadas += 1
    elif tarefa['completed'] == False:
        tarefas_incompletas += 1

print(f'{tarefas_incompletas}, {tarefas_completadas}')