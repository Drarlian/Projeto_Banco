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
        caminho = 'dados\\clientes.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
            with open(caminho, 'w', encoding='UTF-8') as arquivo:
                if conteudo != '':
                    ret: list = decode(conteudo)
                    ret.append(self)
                    ret = encode(ret)
                    arquivo.write(ret)
                else:
                    ret = encode([self])
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

    @numero_conta.setter
    def numero_conta(self, numero_conta: int) -> None:
        self.__numero_conta = numero_conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self.__saldo = saldo

    def __str__(self) -> str:
        return f'Cliente -> {self.cliente} | Conta-> Número da conta: {self.numero_conta} | Saldo: {self.saldo}'

    def sacar(self):
        pass

    def depositar(self):
        pass

    def transferir(self):
        pass

    def pegar_dados_conta(self, cpf: int):
        banco = Banco()
        for conta in banco.contas:
            if conta.cliente.cpf == cpf:
                self.numero_conta = conta.numero_conta
                self.saldo = conta.saldo

    def __gerar_numero_conta(self) -> int:
        caminho = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo != '':
                    ret: list = decode(conteudo)
                    codigo = ret[-1].numero_conta
                    return codigo + 1
                else:
                    return 1
        else:
            return 1

    def __registrar_conta(self) -> None:
        caminho = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
            with open(caminho, 'w', encoding='UTF-8') as arquivo:
                if conteudo != '':
                    ret: list = decode(conteudo)
                    ret.append(self)
                    ret = encode(ret)
                    arquivo.write(ret)
                else:
                    ret = encode([self])
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
        caminho = 'dados\\clientes.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo != '':
                    ret: list = decode(conteudo)
                else:
                    ret = []
            return ret
        else:
            return []

    def __buscar_contas(self) -> list:
        caminho = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo != '':
                    ret: dict = decode(conteudo)
                else:
                    ret = []
            return ret
        else:
            return []


def verificar_conta_existe(cpf: int) -> bool:
    banco = Banco()
    for conta in banco.contas:
        if conta.cliente.cpf == cpf:
            return True
    return False


def pegar_dados_cliente(cpf: int) -> Cliente:
    banco = Banco()
    for cliente in banco.clientes:
        if cliente.cpf == cpf:
            return cliente
    return None
