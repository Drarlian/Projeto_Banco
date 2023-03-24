from models.sistema import Banco, Cliente, Conta
from verifica.verifica_dado import verifica_int
from time import sleep

def menu():
    while True:
        print('Banco Hype')
        print('1 - Criar Conta')
        print('2 - Efetuar Saque')
        print('3 - Efetuar Depósito')
        print('4 - Efetuar Transferência')
        print('5 - Listar Contas')
        print('6 - Sair do Sistema')

        opcao = verifica_int('Digite a opção: ')

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            break
        else:
            print('Opção inválida')
