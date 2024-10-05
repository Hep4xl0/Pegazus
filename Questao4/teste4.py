lista = ["   joao   ","   maria   ","  joana  "]
lista_sem_espaco = [nome.strip() for nome in lista] #metodo strip faz com que seja removido algo no inicio e final de uma string, neste caso esta sendo removido o espaço em branco
print(lista_sem_espaco)