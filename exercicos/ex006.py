n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, a multiplicação é {}, e a divisão é {: .3f}' .format(s,m, d) , end='')
print(' a divisão inteira é {} e a potência é {}' .format(di, e))

