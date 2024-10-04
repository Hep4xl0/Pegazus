
lista = []
lista.append(1)#primeiro item
lista.append(2)#segundo item
lista.append(3)#terceiro item
print(f'Lista orginal: {lista}\n')
#FIFO
lista_fifo = lista.copy()
lista_fifo.append(7)
print(f'Adição de um item na metodologia FIFO: {lista_fifo}')
item_removido = lista_fifo.pop(0)
print(f'Remoção de um item na metodologia FIFO: {lista_fifo}, onde o item {item_removido} foi removido\n')

#LIFO
lista_lifo = lista.copy()
lista_lifo.append(8)
print(f'Adição de um item na metodologia LIFO: {lista_lifo}')
item_removido = lista_lifo.pop()  # Remover o último item (LIFO)
print(f'Lista após remoção na metodologia LIFO: {lista_lifo}, onde o item {item_removido} foi removido')