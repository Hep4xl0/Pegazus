#VERSÃO BASE DO PROGRAMA PARA O DESAFIO
from helpers import *

def menu():
    while True:
        print("\nMenu:")
        print("1 Criar Conta")
        print("2 Visualizar Contas")
        print("3 Sacar")
        print("4 Depositar")
        print("5 sair")
        
        opcao = int(input("Escolha uma opção: "))
        match opcao:
        
            case 1:
                criar_conta()
            case 2:
                visualizar_contas(contas)
            case 3:
                saque_saldo()
            case 4:
                deposito()
            case 5:
                print("saindo")
                break

menu()
#VERSÃO BASE DO PROGRAMA PARA O DESAFIO