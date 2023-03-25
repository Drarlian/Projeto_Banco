from models.sistema import Banco, Cliente, Conta, verificar_conta_existe, pegar_dados_cliente
from verifica.verifica_dado import verifica_int
from time import sleep

def menu_base():
    while True:
        print('Banco Hype')
        print('1 - Criar Conta')
        print('2 - Entrar em uma Conta')
        print('3 - Listar Contas')
        print('4 - Sair do Sistema')

        opcao = verifica_int('Digite a opção: ')

        if opcao == 1:
            print('Informe seus dados:')
            cpf = verifica_int('CPF: ')
            if not verificar_conta_existe(cpf):
                nome = str(input('Nome: ')).strip().capitalize()
                sobrenome = str(input('Sobrenome: ')).strip().capitalize()
                idade = verifica_int('Idade: ')
                cliente = Cliente(nome, sobrenome, idade, cpf)
                conta = Conta(cliente)
                menu_cliente(conta)
            else:
                print('O CPF informado já está em uso.')
            sleep(2)
        elif opcao == 2:
            cpf = verifica_int('Informe o CPF: ')
            if verificar_conta_existe(cpf):
                cliente = pegar_dados_cliente(cpf)
                conta = Conta(cliente)
                menu_cliente(conta)
            else:
                print('O CPF informado não está registrado.')
        elif opcao == 3:
            banco = Banco()
            for conta in banco:
                print(conta)
                print('-' * 20)
            sleep(2)
        elif opcao == 4:
            print('Volte Sempre :)')
            sleep(2)
            exit()
        else:
            print('Opção inválida!')


def menu_cliente(conta: Conta):
    while True:
        print('Banco Hype')
        print('1 - Efetuar Saque')
        print('2 - Efetuar Depósito')
        print('3 - Efetuar Transferência')
        print('4 - Voltar')
        print('5 - Sair do Sistema')

        opcao = verifica_int('Digite a opção: ')

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            print('Voltando...')
            sleep(2)
            menu_base()
        elif opcao == 5:
            print('Volte Sempre :)')
            sleep(2)
            exit()
        else:
            print('Opção inválida!')
