lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
lista = ["maria" if nome == "joao" else nome for nome in lista] #verifica todos os nomes da lista e caso ele seja joao ele se tornara maria
print(lista)