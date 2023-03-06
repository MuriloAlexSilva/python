from random import shuffle

primeiro    =   input('Primeiro aluno: ')
segundo     =   input('Segundo aluno: ')
terceiro    =   input('Terceiro aluno: ')
quarto      =   input('Quarto aluno: ')
quinto      =   input('Quinto aluno: ')
lista       =   [primeiro,segundo,terceiro,quarto,quinto]

shuffle(lista) # Temos que colocar o shuffle separado da variavel, se não ele não funciona

print('A ordem de apresentação seria a seguinte:\n{}'.format(lista))
