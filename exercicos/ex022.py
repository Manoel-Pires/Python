nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('o seu nome em maiúsculas é  ', nome.upper())
print('Seu nome em minusculas  é ' , nome.lower())
print('Seu nome tem ao todo ', len(nome) - nome.count(' '),' letras')
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))







