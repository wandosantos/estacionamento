print('===========Digite a Placa e a Hora==========')
placa = input('Digite sua placa :')
hora =float(input('Digite a hora de entrada :'))

registro = placa
horas = hora * 3600
horaf = horas // 3600
placaSaida = input('Digite sua placa, para liberar, seu automovel! :')
horaSaida = int(input('Digite a hora de saida :'))
#saida = placaSaida

if placaSaida == registro:
    saida = placaSaida
    preco = (horaSaida - horaf ) * 5.60
    print('Seu automovel sera liberado de imediato')
    print('Valor do estacionamento {:.2f} '.format(preco))
    print('hora da sua entrada : ',horaf,':00' , ' hora da sua saida :',horaSaida ,':00')
elif placaSaida != registro:
    print('Sua placa esta incorreta,tente novamente !')    