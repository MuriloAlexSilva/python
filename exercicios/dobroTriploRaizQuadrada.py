number  =   float(input('Digite um numero: '))
dobro   =   number * 2
triplo  =   number * 3
raiz    =   number ** (1/2)
# O ** seria o exponencial
# O :.2f seria 2 casas flutuantes
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(number,dobro,number,triplo,number,raiz))
