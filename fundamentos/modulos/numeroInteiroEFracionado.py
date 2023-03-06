from math import trunc

# Quando utilizamos somente um metodo, é ideal importar somente ele na biblioteca

number  =   float(input('Digite um numero: '))

print('O número {} tem a parte Inteira {}.'.format(number,trunc(number)))