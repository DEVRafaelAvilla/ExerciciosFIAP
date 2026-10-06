colaboradres = int(input('Quantos colaboradores participarão da votação? '))
contador_segunda = 0
contador_terca = 0
contador_quarta = 0
contador_quinta = 0
contador_sexta = 0
if colaboradres <= 0:
    print('Número de colaboradores inválido. Por favor, insira um número maior que zero.')
else:
    for i in range(1,colaboradres + 1):
        dia_escolhido = input('Informe o dia de sua preferência (Segunda-Feira, Terça-Feira, Quarta-Feira, Quinta-Feira, Sexta-Feira): ')
        if dia_escolhido.lower() == 'segunda-feira':
            contador_segunda += 1
        elif dia_escolhido.lower() == 'terça-feira':
            contador_terca += 1
        elif dia_escolhido.lower() == 'quarta-feira':
            contador_quarta += 1
        elif dia_escolhido.lower() == 'quinta-feira':
            contador_quinta += 1
        elif dia_escolhido.lower() == 'sexta-feira':
            contador_sexta += 1
    maior = max(contador_segunda, contador_terca, contador_quarta, contador_quinta, contador_sexta)
    print('O(s) dia(s) escolhido(s) pelos colaboradores foi: ')
    if maior == contador_segunda:
        print('Segunda-Feira - ', contador_segunda, 'voto(s)')
    if maior == contador_terca:
        print('Terça-Feira - ', contador_terca, 'voto(s)')
    if maior == contador_quarta:
        print('Quarta-Feira - ', contador_quarta, 'voto(s)')
    if maior == contador_quinta:
        print('Quinta-Feira - ', contador_quinta, 'voto(s)')
    if maior == contador_sexta:
        print('Sexta-Feira - ', contador_sexta, 'voto(s)')

    print('O número de colaboradores que participaram da votação foi:', colaboradres)