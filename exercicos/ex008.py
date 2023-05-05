d = float(input('Quantos dias vc ficou com o carro? '))
km = float(input('Quantos km rodados? '))
diária = d*60
tkm = km*0.15
deb = diária + tkm
print('Valor das diárias = {} \n Valor por Km total = {} \n Total a pagar = {}' .format(diária, tkm, deb))
