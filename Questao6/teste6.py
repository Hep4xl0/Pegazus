lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
lista = ["maria" if nome == "joao" else nome for nome in lista]
print(lista)