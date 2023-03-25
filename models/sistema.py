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
    def nome(self) -> None:
        return self.__nome

    @property
    def sobrenome(self) -> None:
        return self.__sobrenome

    @property
    def idade(self) -> None:
        return self.__idade

    @property
    def cpf(self) -> None:
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
        self.__numero_conta: int = self.__gerar_numero_conta()
        self.__saldo: float = 0.0
        self.__registrar_conta()

    @property
    def cliente(self) -> None:
        return self.__cliente

    @property
    def numero_conta(self) -> None:
        return self.__numero_conta

    @property
    def saldo(self) -> None:
        return self.__saldo

    def __str__(self) -> None:
        return f'Cliente -> {self.cliente} | Conta-> Número da conta: {self.numero_conta} | Saldo: {self.saldo}'

    def sacar(self):
        pass

    def depositar(self):
        pass

    def transferir(self):
        pass

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
                ret: list = decode(conteudo)
            return ret
        else:
            return None

    def __buscar_contas(self) -> list:
        caminho = 'dados\\contas.json'
        if path.exists(caminho):
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                conteudo = arquivo.read()
                ret: dict = decode(conteudo)
            return ret
        else:
            return None
