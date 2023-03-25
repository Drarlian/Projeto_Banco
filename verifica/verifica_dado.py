def verifica_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
        except (ValueError, TypeError):
            print('Informe um valor válido!')
        except KeyboardInterrupt:
            print('O usuário escolheu não continuar.')
            exit()
        else:
            return valor
