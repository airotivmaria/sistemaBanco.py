menu = """

[1] deposito
[2] saque
[3] extrato
[4] sair

==> """

saldo = 0
num_saque = 0
limite = 500
extrato = ''
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor_deposito = float(input('Digite quanto deseja depositar: '))

        if valor_deposito < 0:
            print(f'Não é possível depositar valores negativos!')
            valor_deposito = float(input('Digite um valor positivo que deseja depositar: '))
        saldo += valor_deposito
        extrato += f'\nDepósito = R$ {valor_deposito}'

    elif opcao == '2':
        saque = float(input('Digite o valor que gostaria de sacar: '))
        if saque > 0:
            num_saque += 1
            saldo -= saque
            print(f'Saque realizado com sucesso! Seu saldo agora é de R$ {saldo}')
            extrato += f'\nSaque = R$ {saque}'

        elif saque > saldo:
                print(f'Seu saldo não é suficiente para realizar esse saque. Seu saldo está em R$ {saldo}')

        elif saque > 500:
            print(f'Você não possui limite de saque, seu limite é de 500, você gostaria de sacar {saque} reais. SAQUE RECUSADO.')

        elif num_saque > LIMITE_SAQUE:
            print('Você excedeu seu limite de 3 operação de saque por dia. SAQUE RECUSADO.')

    elif opcao == '3':
        print(f'============= extrato ============')
        print(f'Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo = R$ {saldo:.2f}')
        print('===================================')

    elif opcao == '4':
        break

    else:
        print('Operação inválida, digite novamente uma das alternativas solicitadas.')
        
