conta_normal = True
saldo = 2000
saque = 5000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com cheque especial')
    else:
        print('Conta sem saldo suficiente')

