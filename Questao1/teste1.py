import json

preco_max = 30.00

with open('lojas.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


for produto in data:
    for i in range(len(produto["produtos"]) - 1, -1, -1):
        if produto['produtos'][i]['preço'] > preco_max:
            del produto['produtos'][i]



with open('lojas.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

