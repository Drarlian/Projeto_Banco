from typing import List
from jsonpickle import encode, decode
from os import path

class Cliente:
    def __init__(self, nome: str, sobrenome: str, idade: int, cpf: int) -> None:
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__idade: int = idade
        self.__cpf: int = cpf
        self.__registrar_cliente()

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @property
    def idade(self) -> int:
        return self.__idade

    @property
    def cpf(self) -> int:
        return self.__cpf

    def __str__(self) -> str:
        return f'Nome: {self.nome} | Sobrenome: {self.sobrenome} | Idade: {self.idade} | CPF: {self.cpf}'

    def __registrar_cliente(self) -> None:
        caminho: str = 'dados\\clientes.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo: str = arquivo.read()
            with open(caminho, 'w', encoding='UTF-8') as arquivo:
                if conteudo != '':
                    ret: list = decode(conteudo)
                    ret.append(self)
                    ret = encode(ret)
                    arquivo.write(ret)
                else:
                    ret: str = encode([self])
                    arquivo.write(ret)


class Conta:
    def __init__(self, cliente: Cliente) -> None:
        self.__cliente: Cliente = cliente

        if verificar_conta_existe(cliente.cpf):
            self.pegar_dados_conta(cliente.cpf)
        else:
            self.__numero_conta: int = self.__gerar_numero_conta()
            self.__saldo: float = 0.0
            self.__registrar_conta()

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def numero_conta(self) -> int:
        return self.__numero_conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self.__saldo = saldo

    def __str__(self) -> str:
        return f'Cliente -> {self.cliente} | Conta-> Número da conta: {self.numero_conta} | Saldo: R${self.saldo:.2f}'

    def sacar(self, valor: float) -> None:
        if self.saldo >= valor > 0:
            self.saldo -= valor
            self.__atualizar_saldo_conta_atual()
            print('Saque realizado com sucesso.')
        else:
            print('Saque inválido.')

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.__atualizar_saldo_conta_atual()
            print('Deposito realizado com sucesso.')
        else:
            print('Deposito inválido.')

    def transferir(self, cpf_destino: int, valor: float) -> None:
        if cpf_destino != self.cliente.cpf:
            if verificar_conta_existe(cpf_destino):
                if self.saldo >= valor > 0:
                    self.__atualizar_saldo_transferencia(cpf_destino, valor)
                    print('Transferência realizada com sucesso.')
                else:
                    print('Transferência inválida.')
            else:
                print('A conta informada não existe.')
        else:
            print('O CPF informado é da conta atual.')

    def __atualizar_saldo_conta_atual(self) -> None:
        banco: Banco = Banco()
        caminho: str = 'dados\\contas.json'

        ret: list = banco.contas
        for conta in ret:
            if conta.numero_conta == self.numero_conta:
                conta.saldo = self.saldo

        with open(caminho, 'w', encoding='UTF-8') as arquivo:
            ret: str = encode(ret)
            arquivo.write(ret)

    def __atualizar_saldo_transferencia(self, cpf_destino: int, valor: float) -> None:
        banco: Banco = Banco()
        caminho: str = 'dados\\contas.json'

        ret: list = banco.contas
        for conta in ret:
            if conta.numero_conta == self.numero_conta:
                self.saldo -= valor
                conta.saldo = self.saldo
            if conta.cliente.cpf == cpf_destino:
                conta.saldo += valor

        with open(caminho, 'w', encoding='UTF-8') as arquivo:
            ret: str = encode(ret)
            arquivo.write(ret)

    def pegar_dados_conta(self, cpf: int):
        banco: Banco = Banco()
        for conta in banco.contas:
            if conta.cliente.cpf == cpf:
                self.__numero_conta = conta.numero_conta
                self.__saldo = conta.saldo

    def __gerar_numero_conta(self) -> int:
        caminho: str = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo: str = arquivo.read()
                if conteudo != '':
                    ret: list = decode(conteudo)
                    codigo: int = ret[-1].numero_conta
                    return codigo + 1
                else:
                    return 1
        else:
            return 1

    def __registrar_conta(self) -> None:
        caminho: str = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo: str = arquivo.read()
            with open(caminho, 'w', encoding='UTF-8') as arquivo:
                if conteudo != '':
                    ret: list = decode(conteudo)
                    ret.append(self)
                    ret = encode(ret)
                    arquivo.write(ret)
                else:
                    ret: str = encode([self])
                    arquivo.write(ret)


class Banco:
    def __init__(self) -> None:
        self.__clientes: List[Cliente] = self.__buscar_clientes()
        self.__contas: List[Conta] = self.__buscar_contas()

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def contas(self) -> list:
        return self.__contas

    def imprimir_clientes(self) -> None:
        for cliente in self.__clientes:
            print(cliente)

    def imprimir_contas(self) -> None:
        for conta in self.__contas:
            print(conta)

    def __buscar_clientes(self) -> list:
        caminho: str = 'dados\\clientes.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo: str = arquivo.read()
                if conteudo != '':
                    ret: list = decode(conteudo)
                else:
                    ret: list = []
            return ret
        else:
            return []

    def __buscar_contas(self) -> list:
        caminho: str = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo: str = arquivo.read()
                if conteudo != '':
                    ret: list = decode(conteudo)
                else:
                    ret: list = []
            return ret
        else:
            return []


def verificar_conta_existe(cpf: int) -> bool:
    banco: Banco = Banco()
    for conta in banco.contas:
        if conta.cliente.cpf == cpf:
            return True
    return False


def pegar_dados_cliente(cpf: int) -> Cliente:
    banco: Banco = Banco()
    for cliente in banco.clientes:
        if cliente.cpf == cpf:
            return cliente
    return None
