from models.sistema import Banco, Cliente, Conta, verificar_conta_existe, pegar_dados_cliente
from verifica.verifica_dado import verifica_int, verifica_float
from time import sleep

def menu_base():
    while True:
        cabecalho('Banco Hype')
        print('1 - Criar Conta')
        print('2 - Entrar em uma Conta')
        print('3 - Listar Contas')
        print('4 - Sair do Sistema')

        opcao = verifica_int('Digite a opção: ')

        if opcao == 1:
            cabecalho('Criação de Conta')
            print('Informe seus dados:')
            cpf = verifica_int('CPF: ')
            if not verificar_conta_existe(cpf):
                nome = str(input('Nome: ')).strip().capitalize()
                sobrenome = str(input('Sobrenome: ')).strip().capitalize()
                idade = verifica_int('Idade: ')
                cliente = Cliente(nome, sobrenome, idade, cpf)
                conta = Conta(cliente)
                print('Criando conta...')
                sleep(2)
                menu_cliente(conta)
            else:
                print('O CPF informado já está em uso.')
            sleep(2)
        elif opcao == 2:
            banco = Banco()
            if len(banco.contas) > 0:
                cabecalho('Login')
                cpf = verifica_int('Informe o CPF: ')
                if verificar_conta_existe(cpf):
                    cliente = pegar_dados_cliente(cpf)
                    conta = Conta(cliente)
                    print('Logando...')
                    sleep(2)
                    menu_cliente(conta)
                else:
                    print('O CPF informado não está registrado.')
            else:
                print('Não existem contas registradas.')
            sleep(2)
        elif opcao == 3:
            banco = Banco()
            if len(banco.contas) > 0:
                cabecalho('Contas Existentes')
                for conta in banco.contas:
                    print(conta)
                    print('-' * 60)
            else:
                print('Não existem contas registradas.')
            sleep(2)
        elif opcao == 4:
            print('Volte Sempre :)')
            sleep(2)
            exit()
        else:
            print('Opção inválida!')


def menu_cliente(conta: Conta):
    while True:
        cabecalho('Banco Hype')
        print('1 - Checar Saldo')
        print('2 - Efetuar Saque')
        print('3 - Efetuar Depósito')
        print('4 - Efetuar Transferência')
        print('5 - Voltar')
        print('6 - Sair do Sistema')

        opcao = verifica_int('Digite a opção: ')

        if opcao == 1:
            print(f'Saldo Atual: R${conta.saldo:.2f}')
            sleep(2)
        elif opcao == 2:
            cabecalho('Saque')
            valor = verifica_float('Informe o valor: R$')
            conta.sacar(valor)
            sleep(2)
        elif opcao == 3:
            cabecalho('Depósito')
            valor = verifica_float('Informe o valor: R$')
            conta.depositar(valor)
            sleep(2)
        elif opcao == 4:
            cabecalho('Transferência')
            cpf: int = verifica_int('Informe o CPF da conta destino: ')
            valor: float = verifica_float('Informe o valor: R$')
            conta.transferir(cpf, valor)
            sleep(2)
        elif opcao == 5:
            print('Voltando...')
            sleep(2)
            menu_base()
        elif opcao == 6:
            print('Volte Sempre :)')
            sleep(2)
            exit()
        else:
            print('Opção inválida!')


def cabecalho(mensagem: str) -> None:
    print('-' * 60)
    print(mensagem.center(60))
    print('-' * 60)
