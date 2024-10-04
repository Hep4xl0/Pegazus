from model import cadastro

contas = []
contas.append(cadastro("Mario Mario", "11187799900"))

def criar_conta():
    nome = str(input('Insira seu nome: '))
    while True:
        cpf = input('Insira seu CPF (somente números): ')
        if cpf.isdigit() and len(cpf) == 11:  
            break
        else:
            print("Você digitou um CPF inválido.")

        
    novo_cadastro = cadastro(nome,cpf)
    contas.append(novo_cadastro)


def visualizar_contas(contas):
    print("Lista de Contas: ")
    for conta in contas:
        print(conta)

def saque_saldo():
    escolher_cpf = input("Digite o CPF da conta que deseja sacar: ")
    for conta in contas:
        if conta.cpf == escolher_cpf:
            if conta.saldo <= 0:
                print("Não é possível fazer saque desta conta.")
                return
            else:
                valor_saque = float(input("Digite o valor a ser sacado: "))
                if 0 < valor_saque <= conta.saldo:
                    conta.sacar(valor_saque)
                    print(f"Saque de R${valor_saque} realizado com sucesso.")
                else:
                    print("Valor de saque inválido.")
                return
    print("Conta não encontrada.")

def deposito():
    escolher_cpf = input("Digite o CPF da conta que deseja sacar: ")
    for conta in contas:
        if conta.cpf == escolher_cpf:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            if valor_deposito > 0:
                conta.depositar(valor_deposito)
                print(f"O deposito de R${valor_deposito} realizado com sucesso.")
            else:
                print('valor invalido')
            return
    print("Conta não encontrada.")
            
