import json
#Define um preço máximo 
preco_max = 30.00
#Abre o arquivo JSON e carrega os dados
with open('lojas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


for produto in data:
    #verifica a lista de trás pra frente para garantir a verificação de todos os produtos
    for i in range(len(produto["produtos"]) - 1, -1, -1):
        #verifica se o preço do produto é maior que o preço maximo
        if produto['produtos'][i]['preço'] > preco_max:
            del produto['produtos'][i]#remove o produto da lista caso seja maior que o preço maximo estabelecido


#salvar as alterações no arquivo json
with open('lojas.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

