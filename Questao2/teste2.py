import json
#Abre o arquivo JSON e carrega os dados
with open('Questao2/lojas2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

#Versão mais "compacta" do codigo com o objetivo de torna-lo mais eficiente, ultilizando a função next para encontrar o preço do Produto B de forma direta

preco_produtoB = next((produto['preço'] for produto in data['produtos'] if produto['nome'] == 'Produto B'), None)
print(preco_produtoB)

#Caso tenha preferecia pela maior legitbilidade e facilitar compreensão do codigo é possivel fazer o mesmo tambem do seguinte metodo:

for produto in data['produtos']:
    if produto['nome'] == 'Produto B':
        preco_produtoB = produto['preço']

print(preco_produtoB)

