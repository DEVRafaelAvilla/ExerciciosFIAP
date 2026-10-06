print('Escolha o tipo de investimento:')
print('1. CDB')
print('2. LCI')
print('3. LCA')

investimento = int(input('Digite o tipo de investimento (1, 2 ou 3): '))

if investimento < 1 or investimento > 3:
    print('Tipo de investimento inválido.')

else:
    valor = float(input('Digite o valor a ser resgatado: '))
    dias = int(input('Digite o número de dias que o valor permaneceu investido: '))

    if investimento == 1:

        if dias <= 180:
            aliquota = 0.225
        elif dias <= 360:
            aliquota = 0.20
        elif dias <= 720:
            aliquota = 0.175
        else:
            aliquota = 0.15

        imposto = valor * aliquota

        print(f'O valor do imposto de renda a ser pago é: R$ {imposto:.2f}')

    else:
        print('O investimento é isento de imposto de renda.')