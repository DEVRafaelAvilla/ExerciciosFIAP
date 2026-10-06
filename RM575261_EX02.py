preco = int(input('Insira o valor do veículo:'))
print('FORMAS DE PAGAMENTO')
print('1. A vista')
print('2. Parcelamento')
forma_pagamento = int(input('Insira o número correspondente a forma de pagamento: '))
if forma_pagamento == 1:
    preco_final = preco - preco * 0.20
    print(f'O preço final a vista com desconto de 20% é: R${preco_final:.2f}')
elif forma_pagamento == 2:
    for i in range(6, 61, 6):
        preco_juros = preco + preco * (0.03 * (i // 6))
        parcela = preco_juros / i
        print(f'O preço final parcelado em {i}X é de R${preco_juros:.2f} com parcelas de R${parcela:.2f}')