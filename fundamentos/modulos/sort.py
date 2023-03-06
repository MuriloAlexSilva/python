from random import choice

primeiro    =   input('Primeiro aluno: ')
segundo     =   input('Segundo aluno: ')
terceiro    =   input('Terceiro aluno: ')
sorteio     =   choice([primeiro,segundo,terceiro])

print('O aluno escolhido foi {}'.format(sorteio))