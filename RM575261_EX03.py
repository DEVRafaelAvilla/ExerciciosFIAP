divida = float(input('Insira o valor da dívida: '))

if divida <= 0:
    print('Valor da dívida inválido. Por favor, insira um valor maior que zero.')
    
else:
    for i in [1, 3, 6, 9, 12]:
        if i == 1:
            juros = divida * 0
        elif i == 3:
            juros = divida * 0.10
        elif i == 6:
            juros = divida * 0.15
        elif i == 9:
            juros = divida * 0.20
        elif i == 12:
            juros = divida * 0.25

        divida_juros = divida + juros
        valor_parcela = divida_juros / i

        print(f'Total: R${divida_juros:.2f} | Juros: R${juros:.2f} | Número de parcelas: {i} | Valor da parcela: R${valor_parcela:.2f}')
