def verifica_int(mensagem: str) -> int:
    while True:
        try:
            valor: int = int(input(mensagem))
        except (ValueError, TypeError):
            print('Informe um valor válido!')
        except KeyboardInterrupt:
            print('O usuário escolheu não continuar.')
            exit()
        else:
            return valor


def verifica_float(mensagem: str) -> float:
    while True:
        try:
            valor: float = float(input(mensagem))
        except (ValueError, TypeError):
            print('Informe um valor válido!')
        except KeyboardInterrupt:
            print('O usuário escolheu não continuar.')
            exit()
        else:
            return valor

