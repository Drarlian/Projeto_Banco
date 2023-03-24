from typing import List

class Cliente:
    def __init__(self, nome: str, sobrenome: str, idade: int, cpf: int) -> None:
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__idade: int = idade
        self.__cpf: int = cpf

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


class Conta:
    def __init__(self, cliente: Cliente) -> None:
        self.__cliente: Cliente = cliente
        self.__numero_conta: int = None  # -> Implementar mais tarde a geração automatica do numero da conta.
        self.__saldo: float = 0.0

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
        return f'Cliente: {self.cliente} | Número da conta: {self.numero_conta} | Saldo: {self.saldo}'

    def sacar(self):
        pass

    def depositar(self):
        pass

    def transferir(self):
        pass


class Banco:
    def __init__(self) -> None:
        self.__clientes: List[Cliente] = self.__verifica_clientes()
        self.__contas: List[Conta] = self.__verifica_contas()

    def __verifica_clientes(self):
        pass

    def __verifica_contas(self):
        pass
