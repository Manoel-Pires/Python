nome = str(input('digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer')
div = nome.split()
print('Seu primeiro nomeé {}' .format(div[0]))
print('Seu ultimo nome é {}' .format(div[len(div) - 1]))

