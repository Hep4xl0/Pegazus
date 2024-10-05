
lista = []
lista.append(1)#primeiro item
lista.append(2)#segundo item
lista.append(3)#terceiro item
print(f'Lista orginal: {lista}\n')
#FIFO (First in, First Out)
lista_fifo = lista.copy() #Faz uma copia da lista original para ser demosntrado o metodo FIFO
lista_fifo.append(7)
print(f'Adição de um item na metodologia FIFO: {lista_fifo}')
item_removido = lista_fifo.pop(0)
print(f'Remoção de um item na metodologia FIFO: {lista_fifo}, onde o item {item_removido} foi removido\n')

#LIFO (Last in, First Out)
lista_lifo = lista.copy()#Faz uma copia da lista original para ser demosntrado o metodo LIFO
lista_lifo.append(8)
print(f'Adição de um item na metodologia LIFO: {lista_lifo}')
item_removido = lista_lifo.pop()  # Remover o último item (LIFO)
print(f'Lista após remoção na metodologia LIFO: {lista_lifo}, onde o item {item_removido} foi removido')