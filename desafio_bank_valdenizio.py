menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 1000
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do  deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito:  R$ {valor:6.2f}\n'

        else:
            print('Operação falhou! O valor informado e  invalido')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite')

        elif excedeu_saques:
            print('Operação falhou! Numero  maximo de saques excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque:     R$ {valor:6.2f}\n'
            numero_saques += 1
            print('valor sacado')
            print('retire seu dinheiro na boca do caixa')

        else:
            print('Operação falhou! O valor informado inválido')


    elif opcao == 'e':
        print('\n****************** EXTRATO *******************')
        print('Não foram  realizadas movimentações' if not extrato else extrato)
        print(f"\nSaldo:     R$ {saldo:6.2f}")
        print('************************************************')

    elif opcao == 'q':
        print('obrigado por ser nosso cliente, volte sempre!!!')
        break


    else:
        print('Operação invalida, por  favor selecione  novamente a  operação desejada')