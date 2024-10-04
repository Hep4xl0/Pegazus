import json
responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}


with open('lojas2.json', 'w', encoding='utf-8') as f:
    json.dump(responsejson, f, ensure_ascii=False, indent=4)
